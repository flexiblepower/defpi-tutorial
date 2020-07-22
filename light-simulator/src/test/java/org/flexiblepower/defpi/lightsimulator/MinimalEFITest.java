/**
 * File ServiceTest.java
 *
 * Copyright 2017 TNO
 */
package org.flexiblepower.defpi.lightsimulator;

import java.time.Duration;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.UUID;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;

import org.flexiblepower.defpi.lightsimulator.inflexible_controller.InflexibleControllerConnectionManager;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.InflexibleControllerConnectionManagerImpl;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.CurtailmentProfile;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.CurtailmentProfileElement;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InflexibleCurtailmentOptions;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InflexibleInstruction;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InflexibleRegistration;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.Measurement;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.minimal_efi_20.InflexibleController_minimalEfi20ConnectionHandler;
import org.flexiblepower.defpi.lightsimulator.observation_publisher.ObservationPublisherConnectionManager;
import org.flexiblepower.defpi.lightsimulator.observation_publisher.ObservationPublisherConnectionManagerImpl;
import org.flexiblepower.defpi.lightsimulator.observation_publisher._1.proto.ObservationPublisher_1Proto.Observation;
import org.flexiblepower.proto.ConnectionProto.ConnectionState;
import org.flexiblepower.service.Connection;
import org.flexiblepower.service.DefPiParameters;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * ServiceTest
 *
 * @author coenvl
 * @version 0.1
 * @since Nov 9, 2017
 */
public class MinimalEFITest {

    private static DatatypeFactory factory;

    private final LightSimulatorConfiguration testConfig = new LightSimulatorConfiguration() {

        @Override
        public int getMinimumOffTime() {
            return 1;
        }

        @Override
        public int getMinimumOnTime() {
            return 10;
        }

        @Override
        public double getMaximumPower() {
            return 40.0;
        }

        @Override
        public double getMinimumPower() {
            return 2.0;
        }

        @Override
        public long getPublishInterval() {
            return 60;
        }

    };

    private final DefPiParameters testParameters = new DefPiParameters("",
            1,
            "",
            "test-process",
            "123",
            "test-user",
            "test@user.com");

    private final Connection testConnection = new Connection() {

        @Override
        public void send(final Object message) {
            if (message instanceof InflexibleRegistration) {
                MinimalEFITest.this.registration = (InflexibleRegistration) message;
            } else if (message instanceof InflexibleCurtailmentOptions) {
                MinimalEFITest.this.curtailmentOptions = (InflexibleCurtailmentOptions) message;
            } else if (message instanceof Observation) {
                MinimalEFITest.this.lastObservation = (Observation) message;
            } else if (message instanceof Measurement) {
                MinimalEFITest.this.lastMeasuredPower = ((Measurement) message).getElectricityMeasurement().getPower();
            }
        }

        @Override
        public boolean isConnected() {
            return true;
        }

        @Override
        public ConnectionState getState() {
            return null;
        }

        @Override
        public String remoteProcessId() {
            return null;
        }

        @Override
        public String remoteServiceId() {
            return null;
        }

        @Override
        public String remoteInterfaceId() {
            return null;
        }

        @Override
        public String remoteProcessName() {
            return null;
        }

    };

    private InflexibleController_minimalEfi20ConnectionHandler handler;

    double lastMeasuredPower;
    Observation lastObservation;
    InflexibleRegistration registration;
    InflexibleCurtailmentOptions curtailmentOptions;

    @BeforeAll
    public static void initClass() throws DatatypeConfigurationException {
        MinimalEFITest.factory = DatatypeFactory.newInstance();
    }

    @BeforeEach
    public void init() {
        final LightSimulator simulator = new LightSimulator();
        simulator.init(this.testConfig, this.testParameters);
        final InflexibleControllerConnectionManager manager = new InflexibleControllerConnectionManagerImpl(simulator);
        this.handler = manager.buildMinimalEfi20(this.testConnection);

        final ObservationPublisherConnectionManager observationManager = new ObservationPublisherConnectionManagerImpl(
                simulator);
        observationManager.build1(this.testConnection);
        this.lastObservation = null;

        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
        Assertions.assertEquals("Light Simulator", this.registration.getDeviceDescription().getLabel());
        Assertions.assertEquals(this.testConfig.getMaximumPower(),
                this.curtailmentOptions.getCurtailmentOptions()
                        .getCurtailmentOption()
                        .get(0)
                        .getCurtailmentRange()
                        .get(0)
                        .getUpperBound(),
                1e-10);
    }

    @Test
    public void runTest() throws InterruptedException {
        this.sendCurtailmentInstruction(20.0, Duration.ofMillis(100), Duration.ofSeconds(1));
        Thread.sleep(150);
        Assertions.assertEquals(20.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(20, this.lastMeasuredPower, 1e-6);
        Thread.sleep(1000);
        Assertions.assertEquals(this.testConfig.getMaximumPower(),
                this.lastObservation.getNumberDatapoints(0).getValue(),
                1e-6);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    @Test
    public void testInvalidCommands() throws InterruptedException {
        // Value too low
        this.sendCurtailmentInstruction(0, Duration.ofMillis(0), Duration.ofMillis(2));
        Thread.sleep(100);
        Assertions.assertNull(this.lastObservation);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);

        // Value too high
        this.sendCurtailmentInstruction(52.0, Duration.ofMillis(0), Duration.ofSeconds(1));
        Thread.sleep(100);
        Assertions.assertNull(this.lastObservation);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);

        // Duration too short
        this.sendCurtailmentInstruction(2.0, Duration.ofMillis(0), Duration.ofMillis(800));
        Thread.sleep(100);
        Assertions.assertNull(this.lastObservation);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    @Test
    public void runExtendTest() throws InterruptedException {
        this.sendCurtailmentInstruction(2.0, Duration.ofMillis(100), Duration.ofSeconds(1));
        Thread.sleep(150);
        Assertions.assertEquals(2.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(2, this.lastMeasuredPower, 1e-6);
        Thread.sleep(700);
        this.sendCurtailmentInstruction(10.0, Duration.ofMillis(0), Duration.ofSeconds(1));
        Thread.sleep(10);
        Assertions.assertEquals(10.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(10.0, this.lastMeasuredPower, 1e-6);
        Thread.sleep(1500);
        Assertions.assertEquals(this.testConfig.getMaximumPower(),
                this.lastObservation.getNumberDatapoints(0).getValue(),
                1e-6);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    private String sendCurtailmentInstruction(final double curtailmentValue,
            final Duration delay,
            final Duration curtailmentDuration) {
        final CurtailmentProfileElement curtailMent = new CurtailmentProfileElement().withValue(curtailmentValue)
                .withDuration(MinimalEFITest.factory.newDuration(curtailmentDuration.toMillis()));

        final GregorianCalendar startTime = new GregorianCalendar();
        startTime.add(Calendar.MILLISECOND, (int) delay.toMillis());

        final CurtailmentProfile profile = new CurtailmentProfile()
                .withStartTime(MinimalEFITest.factory.newXMLGregorianCalendar(startTime))
                .withCurtailmentProfileElement(curtailMent);

        final String instructionId = UUID.randomUUID().toString();
        final InflexibleInstruction instruction = new InflexibleInstruction().withEfiVersion("2.0")
                .withInstructionId(instructionId)
                .withCurtailmentProfile(profile);

        this.handler.handleInflexibleInstructionMessage(instruction);
        return instructionId;
    }

}
