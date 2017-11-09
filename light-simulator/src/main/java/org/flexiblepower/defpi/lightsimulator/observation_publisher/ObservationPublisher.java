/**
 * File ObservationPublisher.java
 *
 * Copyright 2017 TNO
 */
package org.flexiblepower.defpi.lightsimulator.observation_publisher;

import org.flexiblepower.defpi.lightsimulator.observation_publisher._1.proto.ObservationPublisher_1Proto.Observation;

/**
 * ObservationPublisher
 *
 * @author coenvl
 * @version 0.1
 * @since Nov 9, 2017
 */
public interface ObservationPublisher {

    public void observe(Observation o);

}
