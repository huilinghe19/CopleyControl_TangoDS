import PyTango
from time import sleep
from sardana import State, SardanaValue
from sardana.pool.controller import MotorController
from sardana.pool.controller import DefaultValue, Description, FGet, FSet, Type

class SerialObject(object):
    #def __init__(self, port, baudrate, readTimeout):   
        #self.ser = serial.Serial(port, baudrate, timeout=readTimeout)
    def __init__(self):
        self.ser = PyTango.DeviceProxy("pyserial/hhl/1")  
        
    def getCommandResult(self, command):
        ser= self.ser
        result =""        
        ser.Write(command)
        print "Write command:", command
        while True:
            data =ser.read(1)
            #print "Read::", data
            if not data:
                break
            if data =="\n":
                break
            if data == "\r":
                continue
            result += data
        print "getCommandResult:", result
        return result

    
    def getNodeID(self, axis):
        """
        get the node id string. Here the node id string of the first motor controller is none,
        the node id string of the second motor controller is 2. 
        """
        
        if axis == 1:
            return "0 "
        elif axis == 2:
            return "2 "
        elif axis ==3:
            return "3 "
        elif axis == 4:
            return "4 "
        
    def setVariable(self, axis, variable_ID, value):
        """
        write data into serial line.
        """
        
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        print  "{} s r{} {}\n".format(nodeID, variable_ID, str(value))
        return self.getCommandResult("{}s r{} {}\n".format(str(nodeID), str(variable_ID), str(int(value))))
    
    def getVariable(self, axis, variable_ID):
        """
        write data into serial line.
        """
        
        ser = self.ser
        nodeID = self.getNodeID(axis) 
        return self.getCommandResult("{}g r{}\n".format(str(nodeID), str(variable_ID)))
    
    def moveMotor(self, axis):
        """
        move the axis.
        """
        
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        result = self.getCommandResult("{} t 1\n".format(str(nodeID)))   
        return result
    
    def abortMotor(self, axis):
        """
        move the axis.
        """
        
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        self.getCommandResult("{} r\n".format(str(nodeID)))   
        
    def read(self,n):
        """
        read n size bytes from serial line.
        """
        
        ser= self.ser
        data =ser.Read(n)
        print "Read ::", data
        return data
    
    def write(self, data):
        """
        write data into serial line.
        """
        ser=self.ser
        print "Write data::", data
        ser.Write(data)
        
class CopleyController(MotorController):

    ctrl_properties = \
        {
         "PyserialDS": {Type : str,
                  Description : "serial device",
                  DefaultValue : "pyserial/hhl/1"},
         "Device": {Type : str,
                  Description : "device name",
                  DefaultValue : "/dev/ttyS0"},
            
         "Baudrate": {Type : int,
                  Description : "baud rate",
                  DefaultValue : 9600},
            
         "Timeout": {Type : float,
                  Description : "read timeout",
                  DefaultValue : 0.5},
        }
    AXIS_NAMES = {1: "stepnet01", 2: "stepnet02"}
    NODEID = {1: " ", 2: "2 "}
    STATES = {"ON": State.On, "MOVING": State.Moving}

    def __init__(self, inst, props, *args, **kwargs):
        #MotorController.__init__(self,inst, props, *args, **kwargs)
        super_class = super(CopleyController, self)
        super_class.__init__(inst, props, *args, **kwargs)
        device_name = self.Device
        baudrate = self.Baudrate
        readTimeout = self.Timeout
        pyserialDS = self.PyserialDS
        #self.copleyController = PyTango.DeviceProxy("stepper/hhl/1")  
        self.copleyController = SerialObject()
     
    def __del__(self):
        del self.copleyController

    def StateOne(self, axis):
        """
        Read the axis state. asix can be 1, 2, 3, 4. One axis is defined as one motor in spock. 
      
        """
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController       
        result = str(copleyController.Status())
        print result
        if result == "Status is STANDBY":
            print "State ON, Motion Stopped"
            state = self.STATES["ON"]
        elif result == "Status is MOVING":
            print "State MOVING, In Moving"
            state = self.STATES["MOVING"]
        else:
            print "State in Fault"
            state = self.STATES["FAULT"]
        limit_switches = MotorController.NoLimitSwitch
        return state, limit_switches

    def ReadOne(self, axis):
        """
        Read the position of the axis(motor). When "wa" or "wm motor_name"is called in spock, 
        this method is used. 
        """
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController
        position = float(copleyController.position)
       
        return position
    
    def DefinePosition(self, axis, position):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController  
        print "pos1: ",position
        if position >=  0:
            print "ok"
            copleyController.WriteRead("{} s r0xc2 512\n {} s r0xca {}".format(str(nodeID), int(position), str(nodeID)))
        elif position < 0: 
            print "no"
            print(" s r0xc2 529 s r0xca {}".format(int(position)))
            copleyController.WriteRead("{} s r0xc2 529\n {} s r0xca {}".format(str(nodeID), int(position), str(nodeID)))
    def StartOne(self, axis, position):
        """
        Move the axis(motor) to the given position. 
        """
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController    
        nodeID = self.NODEID[axis]
        print "pos2: ",position 
        self.DefinePosition(axis, position)
        print "pos3: ",position 
        copleyController.WriteRead(str(nodeID) + "t 1 ")
       
           
        
    def GetAxisPar(self, axis, name):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController    
        name = name.lower()
        if name == "acceleration":
            ans = str(int(copleyController.acceleration))          
           
            v = float(ans)
        elif name == "deceleration":
            ans = str(int(copleyController.deceleration))     
            
            v = float(ans)
        elif name == "velocity":
            ans = str(int(copleyController.velocity))
            
            v = float(ans)       

        return v
    
    def SetAxisPar(self, axis, name, value):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController    
        name = name.lower()
        nodeID = self.NODEID[axis]
        if name == "acceleration":
            copleyController.Write(str(nodeID) + " s r0xcc " + str(int(value)))           
            
        elif name == "deceleration":
            copleyController.Write(str(nodeID) + " s r0xcd " + str(int(value)))             
           
        elif name == "velocity":
            copleyController.Write(str(nodeID) + " s r0xcb " + str(int(value)))      
            
       
    
    def AbortOne(self, axis):
        """
        Abort the axis(motor).
        """
        copleyController = self.copleyController
        copleyController.StopMove()

