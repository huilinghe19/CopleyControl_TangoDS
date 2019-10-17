# CopleyControl_TangoDS

1. Introduction

	CopleyControl is a Device Server of copley controller to control the motors. It is based of PySerial Device Server, which transfers the ASCII message to the controllers. 

2. Operating environment and software support: 
	Debian 9 system,
	Python 2.7,
	Jive, 
	Tango, PyTango,
	CME 2 (copley control software)

3. How to use them. 

	3.1 Start jive:

 		Command: “jive”

	3.2 Start PySerial DS:

 		Command: “python PySerial.py test”

	In addition, a new device “pyserial/hhl/1” needs to be added in PySerial DS. 


	NOTE: Serial port is defined as “/dev/ttyS0” in the “__init__()” method in “PySerial.py”. If the serial port is different or the operating system is different, then the serial port should be changed manually. 

	3.3. Start CopleyControl DS:

 		Command: “python CopleyControl.py test”

	In addition, a new device “copley/hhl/1” needs to be added in CopleyControl DS. 



4. CopleyControl DS interface 

The Commands and Attributes are shown in "table_copleycontrol.docx", which is still in progress. The result is similar with OmsVme58 Tango Cpp Class: http://hasyweb.desy.de/services/computing/Tango/pogo_html_docu/OmsVme58/

5. How to create powerPMAC_TANGO DS with just xmi code in pogo? It is based on C++ code originally.
powerPMAC_TANGO DS class can not be created directly with pogo. Because the pogo version is not the same.

Frist, add pogoRevision="9.4" into the class. <classes name="PowerPMACAxes" pogoRevision="9.4">
	Then use pogo to create powerPMAC_TANGO DS CLASS with the option Makefile. Then the c++ source files can be created in the folder. Then use "make" to create the powerPMAC_TANGO DS class DS. at the end, you will see PowerPMACAxes in the folder "~/DeviceServers". The command:"DeviceServers/PowerPMACAxes test" can be used later. All my c++ DS class such as Socket DS is also using the method. 

6. Qt Designer

  Command: "taurusdesigner"
  
  The Qt Designer interface will be displayed and .ui file can be opened to show the copley controller GUI, in the GUI the states, position and acceleration and "taurustrend stepnet01/position" curve can be shown.


7. Steps to create all things from zero. the control program "CopleyController.py" is under "/controller/test".

  Terminal1: python work/sardana_practise/jive/serialLine/src/PySerial.py test
  Terminal2: python work/CopleyControl_TangoDS/CopleyControl.py test
  Terminal3: Sardana demo4
  Terminal4: spock

  In spock, "wa", "sar_demo", "lsctrllib", "Pool_demo4_1.put_property({"PoolPath":["/controllers/test"]})", "defctrl 
CopleyController copleyctrl" "defm stepnet1 copleyctrl 1" "copleyctrl.state()" "stepnet1.state()"
	
