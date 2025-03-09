# This Python file uses the following encoding: utf-8

# Clean up any open project
if projects.primary:
	projects.primary.close()

# Create new project
projects.create("c:\\ESME_Project\\My_Configuration.project", True)

# Add a PLC
projects.primary.add("My_Configuration", 4096, "1003 009D", None, None)
plc = projects.primary.find("My_Configuration", True)[0]
controllerDeviceID =  plc.get_device_identification()
controllerVersion = controllerDeviceID.version
controllerID = controllerDeviceID.id
controllerType = controllerDeviceID.type

info = projects.primary.get_project_info()
info.description = "Application generated with Modicon PLC Configurator\r\nBy restricted restricted\r\n09/03/2025 11:17:08\r\n36455ef8-f6c2-460a-91c3-15d69cf9452f"

# No IO module for this configuration

# No Communication modules for this configuration

#This line is only for Pacdrive, to add Protocol manager
plc.add("Industrial_Ethernet_Manager", 100, "1003 0096", None, None)	#add the protocol EtherNet/IP
eip_network = projects.primary.find ("Industrial_Ethernet_Manager", True)[0]

sercos_network = plc.find("Sercos_Master")[0]

# Save the project
projects.primary.save()
