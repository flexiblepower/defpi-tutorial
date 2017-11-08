package org.flexiblepower.defpi.lightsimulator.inflexible_controller;

import javax.annotation.Generated;

import org.flexiblepower.defpi.lightsimulator.LightSimulator;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.minimal_efi_20.InflexibleController_minimalEfi20ConnectionHandler;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.InflexibleController_efi20ConnectionHandlerImpl;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.efi_20.InflexibleController_efi20ConnectionHandler;
import org.flexiblepower.defpi.lightsimulator.inflexible_controller.minimal_efi_20.InflexibleController_minimalEfi20ConnectionHandlerImpl;
import org.flexiblepower.service.Connection;

/**
 * InflexibleControllerConnectionManagerImpl
 *
 * File generated by org.flexiblepower.create-service-maven-plugin. 
 * NOTE: This file is generated as a stub, and has to be implemented by the user. Re-running the codegen plugin will
 * 		 not change the contents of this file.
 * Template by TNO, 2017
 * 
 * @author coenvl
 */
@Generated(value = "org.flexiblepower.plugin.servicegen", date = "Nov 8, 2017 4:10:46 PM")
public class InflexibleControllerConnectionManagerImpl implements InflexibleControllerConnectionManager {

	private final LightSimulator service;
	
	/**
	 * Auto-generated constructor building the factory for ConnectionHandlers of the provided service
	 *
	 * @param service The service that will be used as argument to instantiate the ConnectionHandlers
	 */
	public InflexibleControllerConnectionManagerImpl(LightSimulator service) {
		this.service = service;
	}

	@Override
	public InflexibleController_efi20ConnectionHandler buildEfi20(Connection connection) {
		return new InflexibleController_efi20ConnectionHandlerImpl(connection, this.service);
	}

	@Override
	public InflexibleController_minimalEfi20ConnectionHandler buildMinimalEfi20(Connection connection) {
		return new InflexibleController_minimalEfi20ConnectionHandlerImpl(connection, this.service);
	}

}

