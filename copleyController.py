import PyTango
from time import sleep
from sardana import State, SardanaValue
from sardana.pool.controller import MotorController
from sardana.pool.controller import DefaultValue, Description, FGet, FSet, Type

class TangoDSObject(object):
    def __init__(self, device):
        self.name = device
        ser = self.connectDevice(device)
        self.ser = ser
        
    def connectDevice(self, device):    
        """ connects with the device server.
        """
        try:
            dev = PyTango.DeviceProxy(device)  
            return dev
        except:
            print "ERROR: An exception with connecting DS {} occurred. ".format(device)  
            return 
            
    def getCommandResult(self, command):
        """
        get the result of the command from the device server
        """
        ser= self.ser
        print "command: ", command 
        result = ser.WriteRead(command)
        print "getCommandResult:", result
        return result

    
    def getNodeID(self, axis):
        """
        get the node id string from db
        """
     
        db = PyTango.Database()
        dict_nodeID = db.get_device_property(str(self.name),"NodeId")
        return str(dict_nodeID["NodeId"][0])
  
        
    def setVariable(self, axis, variable_ID, value):
        """
        set variable
        """
        
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        print  "{} s r{} {}\n".format(nodeID, variable_ID, str(value))
        return self.getCommandResult("{} s r{} {}\n".format(str(nodeID), str(variable_ID), str(int(value))))
    
    def getVariable(self, axis, variable_ID):
        """
        get variable
        """
        
        ser = self.ser
        nodeID = self.getNodeID(axis) 
        return self.getCommandResult("{} g r{}\n".format(str(nodeID), str(variable_ID)))
    
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
        abort the axis.
        """
        
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        self.getCommandResult("{} t 0\n".format(str(nodeID)))   
        
    
        
class CopleyController(MotorController):

    ctrl_properties = \
        {
        
          "Device": {Type : str,
                  Description : "connected device server",
                  DefaultValue : "stepper/hhl/1"},
       
        }
    AXIS_NAMES = {1: "stepnet01", 2: "stepnet02"}
    
    STATES = {"ON": State.On, "MOVING": State.Moving}

    def __init__(self, inst, props, *args, **kwargs):
        #MotorController.__init__(self,inst, props, *args, **kwargs)
        super_class = super(CopleyController, self)
        super_class.__init__(inst, props, *args, **kwargs)
        device = self.Device
        self.copleyController = TangoDSObject(device)
     
    def __del__(self):
        del self.copleyController

    def StateOne(self, axis):
        """
        Read the axis state. asix can be 1, 2, 3, 4. One axis is defined as one motor in spock. 
      
        """
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController      
        result = copleyController.getVariable(axis, "0xA0")  
        print "status result value: ", result
        if result == "0":
            print "State ON, Motion Stopped"
            state = self.STATES["ON"]
        else:
            state = self.STATES["MOVING"]
            print "State MOVING, In Moving"
         
        limit_switches = MotorController.NoLimitSwitch
        return state, limit_switches

    def ReadOne(self, axis):
        """
        Read the position of the axis(motor). When "wa" or "wm motor_name"is called in spock, 
        this method is used. 
        """
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController
        ans = copleyController.getVariable(axis, "0xca")
      
        return float(ans)
    def DefinePosition(self, axis, position):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController     
        copleyController.setVariable(axis, "0xca", str(int(position)))

    def StartOne(self, axis, position):
        """
        Move the axis(motor) to the given position. 
        """
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController     
        self.DefinePosition(axis, position)
        copleyController.moveMotor(axis)   
        
    def GetAxisPar(self, axis, name):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController    
        name = name.lower()
        if name == "acceleration":
            ans = copleyController.getVariable(axis, "0xcc")           
            v = float(ans)          
        elif name == "deceleration":
            ans = copleyController.getVariable(axis, "0xcd")               
            v = float(ans)        
        elif name == "velocity":
            ans = copleyController.getVariable(axis, "0xcb")             
            v = float(ans)                
        elif name == "step_per_unit":
            v = 1
        return v
    
    def SetAxisPar(self, axis, name, value):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = self.copleyController    
        name = name.lower()
        if name == "acceleration":
            copleyController.setVariable(axis, "0xcc", int(value))                       
        elif name == "deceleration":
            copleyController.setVariable(axis, "0xcd", int(value))                      
        elif name == "velocity":
            copleyController.setVariable(axis, "0xcb", int(value)) 
        elif name == "step_per_unit":
            raise Exception("step_per_unit is always 1")
        
    def AbortOne(self, axis):
        """
        Abort the axis(motor).
        """
        copleyController = self.copleyController
        copleyController.abortMotor(axis)

