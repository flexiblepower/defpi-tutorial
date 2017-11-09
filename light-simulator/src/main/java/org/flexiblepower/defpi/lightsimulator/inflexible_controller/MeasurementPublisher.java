/**
 * File MeasurementPublisher.java
 *
 * Copyright 2017 TNO
 */
package org.flexiblepower.defpi.lightsimulator.inflexible_controller;

import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.Measurement;

/**
 * MeasurementPublisher
 *
 * @author coenvl
 * @version 0.1
 * @since Nov 9, 2017
 */
public interface MeasurementPublisher {

    public void publishMeasurement(Measurement measurement);

}
