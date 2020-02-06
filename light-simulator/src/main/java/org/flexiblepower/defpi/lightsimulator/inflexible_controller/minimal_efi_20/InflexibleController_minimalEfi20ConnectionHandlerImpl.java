package org.flexiblepower.defpi.lightsimulator.inflexible_controller.minimal_efi_20;

import java.io.IOException;

import javax.annotation.Generated;

import org.flexiblepower.defpi.lightsimulator.inflexible_controller.InflexibleControllerConnectionManagerImpl;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.MeasurementPublisher;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InflexibleInstruction;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.Measurement;
import org.flexiblepower.service.Connection;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * InflexibleController_minimalEfi20ConnectionHandlerImpl
 *
 * File generated by org.flexiblepower.create-service-maven-plugin.
 * NOTE: This file is generated as a stub, and has to be implemented by the user. Re-running the codegen plugin will
 * not change the contents of this file.
 * Template by TNO, 2017
 *
 * @author coenvl
 */
@Generated(value = "org.flexiblepower.plugin.servicegen", date = "Nov 8, 2017 4:10:46 PM")
public class InflexibleController_minimalEfi20ConnectionHandlerImpl
        implements InflexibleController_minimalEfi20ConnectionHandler, MeasurementPublisher {

    private final Logger log = LoggerFactory.getLogger(InflexibleController_minimalEfi20ConnectionHandlerImpl.class);

    private final Connection connection;

    private final InflexibleControllerConnectionManagerImpl manager;

    /**
     * Auto-generated constructor for the ConnectionHandlers of the provided service
     *
     * @param manager The service for which to handle the connections
     */
    public InflexibleController_minimalEfi20ConnectionHandlerImpl(final Connection connection,
            final InflexibleControllerConnectionManagerImpl manager) {
        this.connection = connection;
        this.manager = manager;
    }

    @Override
    public void handleInflexibleInstructionMessage(final InflexibleInstruction message) {
        this.log.info("Received instruction {} for {}",
                message.getInstructionId(),
                message.getCurtailmentProfile().getCurtailmentQuantity());
        this.manager.handleInstruction(message, null);
    }

    @Override
    public void publishMeasurement(final Measurement measurement) {
        if (this.connection.isConnected()) {
            try {
                this.connection.send(measurement);
            } catch (final IOException e) {
                e.printStackTrace();
            }
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
        this.manager.terminate(this);
    }

}