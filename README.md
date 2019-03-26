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


	
