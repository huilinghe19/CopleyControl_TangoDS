#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        CopleyControl.py
#
#  Project :     
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      null$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["CopleyControl", "CopleyControlClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(CopleyControl.additionnal_import) ENABLED START -----#
import time
#----- PROTECTED REGION END -----#	//	CopleyControl.additionnal_import

# Device States Description
# No states for this device


class CopleyControl (PyTango.Device_4Impl):
    """"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(CopleyControl.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	CopleyControl.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        self.name = name
        CopleyControl.init_device(self)
        #----- PROTECTED REGION ID(CopleyControl.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	CopleyControl.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(CopleyControl.delete_device) ENABLED START -----#
              
        #----- PROTECTED REGION END -----#	//	CopleyControl.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_Port_read = ""
        self.attr_Acceleration_read = 0.0
        self.attr_Position_read = 0.0
        self.attr_Velocity_read = 0.0
        self.attr_NodeID_read = 0      
        self.attr_Deceleration_read = 0.0
        #----- PROTECTED REGION ID(CopleyControl.init_device) ENABLED START -----#  
        print "In ", self.get_name(), "::init_device()"
        self.dev_serial =  self.connectSerial()         
        self.attr_NodeID_read = self.getNodeID()
        #self.initControlParameters()                # In case something needs to be added in init.
        #----- PROTECTED REGION END -----#	//	Cself.attr_Timeout_read = 0opleyControl.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(CopleyControl.always_executed_hook) ENABLED START -----#
        print "In ", self.get_name(), "::always_excuted_hook()"
        #----- PROTECTED REGION END -----#	//	CopleyControl.always_executed_hook

    # -------------------------------------------------------------------------
    #    CopleyControl read/write attribute methods
    # -------------------------------------------------------------------------
              
    def read_Port(self, attr):
        self.debug_stream("In read_Port()")
        #----- PROTECTED REGION ID(CopleyControl.Port_read) ENABLED START -----#
        print "In ", self.get_name(), "::read_Port()"        
        dev = self.dev_serial
        attr_Port_read = dev.Port
        attr.set_value(attr_Port_read)       
        #----- PROTECTED REGION END -----#	//	CopleyControl.Port_read
         
    def read_Acceleration(self, attr):
        self.debug_stream("In read_Acceleration()")
        #----- PROTECTED REGION ID(CopleyControl.Acceleration_read) ENABLED START -----#
        print "In ", self.get_name(), "::read_Acceleration()"      
        command = self.getParameterCommand(self.attr_NodeID_read, "g r0xcc")
        attr_Acceleration_read =  self.SendCommandGetResult(command)
        #attr.set_value(int(self.attr_Acceleration_read))
        if attr_Acceleration_read != '':
            attr.set_value(int(attr_Acceleration_read))         
        #----- PROTECTED REGION END -----#	//	CopleyControl.Acceleration_read
        
    def write_Acceleration(self, attr):
        self.debug_stream("In write_Acceleration()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(CopleyControl.Acceleration_write) ENABLED START -----#
        print "In ", self.get_name(), "::write_Acceleration()", str(data)       
        command = self.setParameterCommand(self.attr_NodeID_read, "s r0xcc", str(int(data)))
        self.Write(command)
        #----- PROTECTED REGION END -----#	//	CopleyControl.Acceleration_write        
   
    def read_Position(self, attr):
        self.debug_stream("In read_Position()")
        #----- PROTECTED REGION ID(CopleyControl.Position_read) ENABLED START -----# 
        print "In ", self.get_name(), "::read_Position()"
        command = self.getParameterCommand(self.attr_NodeID_read, "g r0xca")
        attr_Position_read =  self.SendCommandGetResult(command)
        if attr_Position_read != '':
            attr.set_value(int(attr_Position_read))     
        #----- PROTECTED REGION END -----#	//	CopleyControl.Position_read
        
    def write_Position(self, attr):
        self.debug_stream("In write_Position()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(CopleyControl.Position_write) ENABLED START -----#
        print "In ", self.get_name(), "::write_Position()", str(data)
        command = self.setParameterCommand(self.attr_NodeID_read, "s r0xca", str(int(data)))
        self.Write(command)
        #----- PROTECTED REGION END -----#	//	CopleyControl.Position_write
        
    def read_Velocity(self, attr):
        self.debug_stream("In read_Velocity()")
        #----- PROTECTED REGION ID(CopleyControl.Velocity_read) ENABLED START -----#
        print "In ", self.get_name(), "::read_Velocity()"
        command = self.getParameterCommand(self.attr_NodeID_read, "g r0xca")
        attr_Velocity_read =  self.SendCommandGetResult(command)
        if attr_Velocity_read != '':
            attr.set_value(int(attr_Velocity_read))
        #----- PROTECTED REGION END -----#	//	CopleyControl.Velocity_read
        
    def write_Velocity(self, attr):
        self.debug_stream("In write_Velocity()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(CopleyControl.Velocity_write) ENABLED START -----#
        print "In ", self.get_name(), "::write_Velocity()", str(data) 
        command = self.setParameterCommand(self.attr_NodeID_read, "s r0xcb", str(int(data)))
        self.Write(command)
        #----- PROTECTED REGION END -----#	//	CopleyControl.Velocity_write
        
    
    def read_NodeID(self, attr):
        self.debug_stream("In read_NodeID()")
        #----- PROTECTED REGION ID(CopleyControl.NodeID_read) ENABLED START -----#
        print "In ", self.get_name(), "::read_NodeID()"
        attr.set_value(self.attr_NodeID_read)        
        #----- PROTECTED REGION END -----#	//	CopleyControl.NodeID_read
          
        
    def read_Deceleration(self, attr):
        self.debug_stream("In read_Deceleration()")
        #----- PROTECTED REGION ID(CopleyControl.Deceleration_read) ENABLED START -----#
        print "In ", self.get_name(), "::read_Deceleration()"
        command = self.getParameterCommand(self.attr_NodeID_read, "g r0xcd")
        attr_Deceleration_read =  self.SendCommandGetResult(command)
        if attr_Deceleration_read != '':
            attr.set_value(int(attr_Deceleration_read))       
        #----- PROTECTED REGION END -----#	//	CopleyControl.Deceleration_read
        
    def write_Deceleration(self, attr):       
        self.debug_stream("In write_Deceleration()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(CopleyControl.Deceleration_write) ENABLED START -----#
        print "In ", self.get_name(), "::write_Deceleration()", str(data)
        command = self.setParameterCommand(self.attr_NodeID_read, "s r0xcd", str(int(data)))
        self.Write(command)
        #----- PROTECTED REGION END -----#	//	CopleyControl.Deceleration_write
        
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(CopleyControl.read_attr_hardware) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	CopleyControl.read_attr_hardware

    # -------------------------------------------------------------------------
    #    CopleyControl command methods
    # -------------------------------------------------------------------------  
    
            
    def dev_state(self):
        """ This command gets the device state (stored in its device_state data member) and returns it to the caller.
        :return: Device state
        :rtype: PyTango.CmdArgType.DevState
        """
        self.debug_stream("In dev_state()")
        argout = PyTango.DevState.UNKNOWN
        #----- PROTECTED REGION ID(CopleyControl.State) ENABLED START -----#
        print "In ", self.get_name(), "::dev_state()"
        #----- PROTECTED REGION END -----#	//	CopleyControl.State
        if argout != PyTango.DevState.ALARM:
            PyTango.Device_4Impl.dev_state(self)
        return self.get_state()
        
    def dev_status(self):
        """ This command gets the device status (stored in its device_status data member) and returns it to the caller.
        :return: Device status
        :rtype: PyTango.ConstDevString
        """
        self.debug_stream("In dev_status()")
        argout = ""
        #----- PROTECTED REGION ID(CopleyControl.Status) ENABLED START -----#
        print "In ", self.get_name(), "::dev_status()"
        command_DriveEventStatus = self.getParameterCommand(self.attr_NodeID_read, "g r0xa0")
        DriveEventStatus = self.SendCommandGetResult(command_DriveEventStatus)   
        if DriveEventStatus == '':
            argout = "Status is OFF"
        elif DriveEventStatus != "0"  and DriveEventStatus != "":
            argout = "Status is MOVING"    
        elif DriveEventStatus == "0":
            argout = "Status is STANDBY" 
        else:
            argout = "Status is FAULT" 
        #----- PROTECTED REGION END -----#	//	CopleyControl.Status
        self.set_status(argout)
        self.__status = PyTango.Device_4Impl.dev_status(self)
        return self.__status
        
    
    def Write(self, argin):
        """ This command gets the input and write the input to the serial line. 
        :param argin: String
        :type argin: PyTango.DevString
        """
        self.debug_stream("In Write()")
        #----- PROTECTED REGION ID(CopleyControl.Write) ENABLED START -----#
        print "In ", self.get_name(), "::Write()", str(argin)       
        dev = self.dev_serial
        dev.Write(argin)
        #----- PROTECTED REGION END -----#	//	CopleyControl.Write
        
    def Stop(self):
        """ Stops the motion of the device.
        """
        self.debug_stream("In Stop()")
        #----- PROTECTED REGION ID(CopleyControl.Stop) ENABLED START -----#
        print "In ", self.get_name(), "::Stop()"
        nodeID = self.attr_NodeID_read
        self.Write("{} r\n".format(str(nodeID)))
      
        #----- PROTECTED REGION END -----#	//	CopleyControl.Stop
         
    def SendCommandGetResult(self, argin):
        """ Sends input to serial line and gets the number in the result of the input.
        :param argin: 
        :type argin: PyTango.DevString
        :rtype: PyTango.DevString
        """
        self.debug_stream("In SendCommandGetResult()")
        argout = ""
        #----- PROTECTED REGION ID(CopleyControl.SendCommandGetResult) ENABLED START -----#
        raw_result = ""
        print "In ", self.get_name(), "::SendCommandGetResult()", str(argin)    
        dev = self.dev_serial       
        dev.FlushInput()
        dev.Write(argin)
        time.sleep(1)
        while True:                      
            data = dev.Read(1) 
            if not data: # no data means errors or timeout
                break
            if data == "\n": # LF -> expected
                break
            if data == '\r': # CR -> ignored
                continue     
            raw_result += data            
        new_result = filter(str.isdigit, raw_result)
        result = ''.join(list(new_result)) 
        if result != '' and result != '033' and result != '33':
            argout = result            
        print "Result: ", str(argout)
        #----- PROTECTED REGION END -----#	//	CopleyControl.SendCommandGetResult
        return argout    
    
    
    def Move(self):
        """ Triggers the device to move.
        """
        self.debug_stream("In Move()")
        #----- PROTECTED REGION ID(CopleyControl.Move) ENABLED START -----#
        print "In ", self.get_name(), "::Move()"             
        command_move = self.setParameterCommand(self.attr_NodeID_read, "t", 1)
        self.Write(str(command_move))
        #----- PROTECTED REGION END -----#	//	CopleyControl.Move
        

    #----- PROTECTED REGION ID(CopleyControl.programmer_methods) ENABLED START -----#
    def initControlParameters(self, desired_state, trajectory_profile_mode, position_desired, velocity_desired, acceleration_desired, deceleration_desired):
        """ Sets Programmed Position Mode, Trajectory Profile Mode, position, velocity, acceleration, deceleration.       
        """
        print "In ", self.get_name(), "::initControlParameters()"
        nodeID = self.attr_NodeID_read
        command_state = self.setParameterCommand(nodeID, "s r0x24", int(desired_state))
        command_profile = self.setParameterCommand(nodeID, "s r0xc8", int(trajectory_profile_mode))
        command_pos = self.setParameterCommand(nodeID, "s r0xca", int(position_desired))
        command_vel = self.setParameterCommand(nodeID, "s r0xcb", int(velocity_desired))
        command_acc = self.setParameterCommand(nodeID, "s r0xcc", int(acceleration_desired))
        command_dec = self.setParameterCommand(nodeID, "s r0xcd", int(deceleration_desired))
        command = command_state + command_profile + command_vel + command_acc + command_dec + command_pos 
        self.Write(command)
        
    def get_state(self):
        """ gets the device state using Drive Event Status command."""
        nodeID = self.attr_NodeID_read
        command_DriveEventStatus = self.getParameterCommand(nodeID, "g r0xa0")        
        DriveEventStatus = self.SendCommandGetResult(command_DriveEventStatus)  
        if DriveEventStatus == '':
            argout = PyTango.DevState.OFF
        elif DriveEventStatus != '0' and DriveEventStatus != '':
            argout = PyTango.DevState.MOVING   
        elif DriveEventStatus == '0':
            argout = PyTango.DevState.STANDBY
        else:
            argout = PyTango.DevState.FAULT
        return argout
        self.set_state(argout)   
   
       
    def setParameterCommand(self, nodeID, command, data):
        """ return the Set Command with nodeID, command and data.
        """
        return '{} {} {}\n'.format(str(int(nodeID)), command, str(int(data)))
            
    def getParameterCommand(self, nodeID, command):
        """ return the Get Command with nodeID, command.
        """
        return '{} {}\n'.format(str(int(nodeID)), command)
       
   
    def connectSerial(self):    
        """ connects with the pyserial device and open the pyserial state.
        """
        print "In ", self.get_name(), "::connectSerial()"
        try:
            dev = PyTango.DeviceProxy("pyserial/hhl/1")            
            if dev.State() == PyTango.DevState.OFF:
                dev.Open()
                return dev
            elif dev.State() == PyTango.DevState.ON:
                return dev
            else:
                print "PyTango DevState Unknown"
        except:
            print("An exception with connectSerial() occurred")      
        
    def getNodeID(self):
        """ gets the node id from the device properties.
        """
        db = PyTango.Database()
        dict_nodeID = db.get_device_property(str(self.name),"node_id")
        return int(dict_nodeID["node_id"][0])
    

      
    #----- PROTECTED REGION END -----#	//	CopleyControl.programmer_methods

class CopleyControlClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(CopleyControl.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	CopleyControl.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
       'node_id':
            [PyTango.DevShort, 
             '',
            [] ],
        'instrument_name':
            [PyTango.DevString, 
             '',
            [] ],
        }


    #    Command definitions
    cmd_list = {
        
        'Write':
            [[PyTango.DevString, "none"],
            [PyTango.DevVoid, "none"]],
        'Stop':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'SendCommandGetResult':
            [[PyTango.DevString, "none"],
            [PyTango.DevString, "none"]],
        'Move':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'Port':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ]],
          
        'Acceleration':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE]],
        'Position':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE]],
        'Velocity':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE]],
        'NodeID':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'Deceleration':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE]],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(CopleyControlClass, CopleyControl, 'CopleyControl')
        #----- PROTECTED REGION ID(CopleyControl.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	CopleyControl.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
