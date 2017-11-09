/**
 * File InstructionStateUpdateSender.java
 *
 * Copyright 2017 TNO
 */
package org.flexiblepower.defpi.lightsimulator.inflexible_controller;

import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.xml.InstructionStatus;

/**
 * InstructionStateUpdateSender
 *
 * @author coenvl
 * @version 0.1
 * @since Nov 9, 2017
 */
public interface InstructionStatusSender {

    public void sendUpdate(InstructionStatus status);

}
