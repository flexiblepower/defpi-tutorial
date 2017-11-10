package org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20;

import java.time.Duration;
import java.util.UUID;

import javax.annotation.Generated;
import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;

import org.flexiblepower.defpi.universaldimmer.UniversalDimmer;
import org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20.xml.CurtailmentProfile;
import org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20.xml.CurtailmentProfileElement;
import org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20.xml.CurtailmentQuantity;
import org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20.xml.InflexibleCurtailmentOptions;
import org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20.xml.InflexibleInstruction;
import org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20.xml.InflexibleRegistration;
import org.flexiblepower.defpi.universaldimmer.inflexible_controller.efi_20.xml.Measurement;
import org.flexiblepower.service.Connection;

/**
 * InflexibleController_efi20ConnectionHandlerImpl
 *
 * File generated by org.flexiblepower.create-service-maven-plugin.
 * NOTE: This file is generated as a stub, and has to be implemented by the user. Re-running the codegen plugin will
 * not change the contents of this file.
 * Template by TNO, 2017
 *
 * @author coenvl
 */
@Generated(value = "org.flexiblepower.plugin.servicegen", date = "Nov 8, 2017 4:10:47 PM")
public class InflexibleController_efi20ConnectionHandlerImpl implements InflexibleController_efi20ConnectionHandler {

    private final Connection connection;

    private final UniversalDimmer service;

    /**
     * Auto-generated constructor for the ConnectionHandlers of the provided service
     *
     * @param service The service for which to handle the connections
     */
    public InflexibleController_efi20ConnectionHandlerImpl(final Connection connection, final UniversalDimmer service) {
        this.connection = connection;
        this.service = service;
    }

    @Override
    public void handleInflexibleRegistrationMessage(final InflexibleRegistration message) {
        System.out.println("Received registration of " + message.getDeviceDescription().getLabel());

    }

    @Override
    public void handleMeasurementMessage(final Measurement message) {
        System.out.println("Measurement value received: " + message.getElectricityMeasurement().getPower());
    }

    @Override
    public void handleInflexibleCurtailmentOptionsMessage(final InflexibleCurtailmentOptions message) {
        try {
            final double minimalPower = message.getCurtailmentOptions()
                    .getCurtailmentOption()
                    .get(0)
                    .getCurtailmentRange()
                    .get(0)
                    .getLowerBound();

            final CurtailmentProfileElement curtailMent = new CurtailmentProfileElement().withValue(minimalPower)
                    .withDuration(DatatypeFactory.newInstance().newDuration(Duration.ofDays(1).toMillis()));

            final CurtailmentProfile profile = new CurtailmentProfile().withStartTime(message.getValidFrom())
                    .withCurtailmentQuantity(CurtailmentQuantity.ELECTRICITY_POWER)
                    .withCurtailmentProfileElement(curtailMent);

            final InflexibleInstruction instruction = new InflexibleInstruction().withEfiVersion("2.0")
                    .withInstructionId(UUID.randomUUID().toString())
                    .withCurtailmentProfile(profile);

            this.connection.send(instruction);
        } catch (final DatatypeConfigurationException e) {
            throw new RuntimeException(e.getMessage());
        }
    }

    @Override
    public void onSuspend() {
        // TODO Auto-generated method stub

    }

    @Override
    public void resumeAfterSuspend() {
        // TODO Auto-generated method stub

    }

    @Override
    public void onInterrupt() {
        // TODO Auto-generated method stub

    }

    @Override
    public void resumeAfterInterrupt() {
        // TODO Auto-generated method stub

    }

    @Override
    public void terminated() {
        // TODO Auto-generated method stub

    }

}