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
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.InflexibleController_efi20ConnectionHandler;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.CurtailmentProfile;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.CurtailmentProfileElement;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InflexibleCurtailmentOptions;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InflexibleInstruction;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InflexibleRegistration;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InstructionRevoke;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InstructionStatus;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InstructionStatusUpdate;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.Measurement;
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
public class ServiceTest {

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
            if (message instanceof InstructionStatusUpdate) {
                ServiceTest.this.lastStatus = ((InstructionStatusUpdate) message).getStatus();
            } else if (message instanceof InflexibleRegistration) {
                ServiceTest.this.registration = (InflexibleRegistration) message;
            } else if (message instanceof InflexibleCurtailmentOptions) {
                ServiceTest.this.curtailmentOptions = (InflexibleCurtailmentOptions) message;
            } else if (message instanceof Observation) {
                ServiceTest.this.lastObservation = (Observation) message;
            } else if (message instanceof Measurement) {
                ServiceTest.this.lastMeasuredPower = ((Measurement) message).getElectricityMeasurement().getPower();
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

    };

    private InflexibleController_efi20ConnectionHandler handler;

    double lastMeasuredPower;
    Observation lastObservation;
    InstructionStatus lastStatus;
    InflexibleRegistration registration;
    InflexibleCurtailmentOptions curtailmentOptions;

    @BeforeAll
    public static void initClass() throws DatatypeConfigurationException {
        ServiceTest.factory = DatatypeFactory.newInstance();
    }

    @BeforeEach
    public void init() {
        final LightSimulator simulator = new LightSimulator();
        simulator.init(this.testConfig, this.testParameters);
        final InflexibleControllerConnectionManager manager = new InflexibleControllerConnectionManagerImpl(simulator);
        this.handler = manager.buildEfi20(this.testConnection);

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
        Assertions.assertEquals(InstructionStatus.ACCEPTED, this.lastStatus);
        Thread.sleep(150);
        Assertions.assertEquals(InstructionStatus.STARTED, this.lastStatus);
        Assertions.assertEquals(20.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(20, this.lastMeasuredPower, 1e-6);
        Thread.sleep(1000);
        Assertions.assertEquals(InstructionStatus.SUCCEEDED, this.lastStatus);
        Assertions.assertEquals(this.testConfig.getMaximumPower(),
                this.lastObservation.getNumberDatapoints(0).getValue(),
                1e-6);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    @Test
    public void testInvalidCommands() {
        // Value too low
        this.lastStatus = null;
        this.sendCurtailmentInstruction(0, Duration.ofMillis(0), Duration.ofMillis(2));
        Assertions.assertEquals(InstructionStatus.REJECTED, this.lastStatus);

        // Value too high
        this.lastStatus = null;
        this.sendCurtailmentInstruction(52.0, Duration.ofMillis(0), Duration.ofSeconds(1));
        Assertions.assertEquals(InstructionStatus.REJECTED, this.lastStatus);

        // Duration too short
        this.lastStatus = null;
        this.sendCurtailmentInstruction(2.0, Duration.ofMillis(0), Duration.ofMillis(800));
        Assertions.assertEquals(InstructionStatus.REJECTED, this.lastStatus);

        // No changes since init...
        Assertions.assertNull(this.lastObservation);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    @Test
    public void runPreemptiveRevokeTest() throws InterruptedException {
        final String instructionId = this
                .sendCurtailmentInstruction(2.0, Duration.ofMillis(100), Duration.ofSeconds(1));
        Assertions.assertEquals(InstructionStatus.ACCEPTED, this.lastStatus);
        this.sendRevokeInstruction(instructionId);
        Thread.sleep(10);
        Assertions.assertEquals(InstructionStatus.ABORTED, this.lastStatus);
        this.lastStatus = null;
        Thread.sleep(1000);
        Assertions.assertNull(this.lastStatus);
        Assertions.assertNull(this.lastObservation);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    @Test
    public void runInvalidRevokeTest() throws InterruptedException {
        this.sendCurtailmentInstruction(12.0, Duration.ofMillis(100), Duration.ofSeconds(1));
        Assertions.assertEquals(InstructionStatus.ACCEPTED, this.lastStatus);
        this.sendRevokeInstruction("123456");
        Assertions.assertEquals(InstructionStatus.ACCEPTED, this.lastStatus);
        Thread.sleep(150);
        Assertions.assertEquals(InstructionStatus.STARTED, this.lastStatus);
        Assertions.assertEquals(12.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(12, this.lastMeasuredPower, 1e-6);
        Thread.sleep(1000);
        Assertions.assertEquals(InstructionStatus.SUCCEEDED, this.lastStatus);
        Assertions.assertEquals(this.testConfig.getMaximumPower(),
                this.lastObservation.getNumberDatapoints(0).getValue(),
                1e-6);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    @Test
    public void runRunningRevokeTest() throws InterruptedException {
        final String instructionId = this
                .sendCurtailmentInstruction(5.0, Duration.ofMillis(100), Duration.ofSeconds(1));
        Assertions.assertEquals(InstructionStatus.ACCEPTED, this.lastStatus);
        Thread.sleep(150);
        Assertions.assertEquals(InstructionStatus.STARTED, this.lastStatus);
        Assertions.assertEquals(5.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(5, this.lastMeasuredPower, 1e-6);
        this.sendRevokeInstruction(instructionId);
        Thread.sleep(10);
        Assertions.assertEquals(InstructionStatus.ABORTED, this.lastStatus);
        this.lastStatus = null;
        Thread.sleep(1000);
        Assertions.assertNull(this.lastStatus);
        Assertions.assertEquals(this.testConfig.getMaximumPower(),
                this.lastObservation.getNumberDatapoints(0).getValue(),
                1e-6);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    @Test
    public void runExtendTest() throws InterruptedException {
        this.sendCurtailmentInstruction(2.0, Duration.ofMillis(100), Duration.ofSeconds(1));
        Assertions.assertEquals(InstructionStatus.ACCEPTED, this.lastStatus);
        Thread.sleep(150);
        Assertions.assertEquals(InstructionStatus.STARTED, this.lastStatus);
        Assertions.assertEquals(2.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(2, this.lastMeasuredPower, 1e-6);
        Thread.sleep(700);
        this.sendCurtailmentInstruction(10.0, Duration.ofMillis(0), Duration.ofSeconds(1));
        Assertions.assertEquals(InstructionStatus.ACCEPTED, this.lastStatus);
        Thread.sleep(10);
        Assertions.assertEquals(InstructionStatus.STARTED, this.lastStatus);
        Assertions.assertEquals(10.0, this.lastObservation.getNumberDatapoints(0).getValue(), 1e-6);
        Assertions.assertEquals(10.0, this.lastMeasuredPower, 1e-6);
        this.lastStatus = null;
        Thread.sleep(500);
        Assertions.assertNull(this.lastStatus);
        Thread.sleep(1000);
        Assertions.assertEquals(InstructionStatus.SUCCEEDED, this.lastStatus);
        Assertions.assertEquals(this.testConfig.getMaximumPower(),
                this.lastObservation.getNumberDatapoints(0).getValue(),
                1e-6);
        Assertions.assertEquals(this.testConfig.getMaximumPower(), this.lastMeasuredPower, 1e-6);
    }

    private String sendCurtailmentInstruction(final double curtailmentValue,
            final Duration delay,
            final Duration curtailmentDuration) {
        final CurtailmentProfileElement curtailMent = new CurtailmentProfileElement().withValue(curtailmentValue)
                .withDuration(ServiceTest.factory.newDuration(curtailmentDuration.toMillis()));

        final GregorianCalendar startTime = new GregorianCalendar();
        startTime.add(Calendar.MILLISECOND, (int) delay.toMillis());

        final CurtailmentProfile profile = new CurtailmentProfile()
                .withStartTime(ServiceTest.factory.newXMLGregorianCalendar(startTime))
                .withCurtailmentProfileElement(curtailMent);

        final String instructionId = UUID.randomUUID().toString();
        final InflexibleInstruction instruction = new InflexibleInstruction().withEfiVersion("2.0")
                .withInstructionId(instructionId)
                .withCurtailmentProfile(profile);

        this.handler.handleInflexibleInstructionMessage(instruction);
        return instructionId;
    }

    /**
     * @param instructionId
     */
    private void sendRevokeInstruction(final String instructionId) {
        final InstructionRevoke revoke = new InstructionRevoke().withInstructionId(instructionId);
        this.handler.handleInstructionRevokeMessage(revoke);
    }

}
