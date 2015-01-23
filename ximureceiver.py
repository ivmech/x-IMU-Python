# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ximureceiver', [dirname(__file__)])
        except ImportError:
            import _ximureceiver
            return _ximureceiver
        if fp is not None:
            try:
                _mod = imp.load_module('_ximureceiver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ximureceiver = swig_import_helper()
    del swig_import_helper
else:
    import _ximureceiver
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


ERR_NO_ERROR = _ximureceiver.ERR_NO_ERROR
ERR_FACTORY_RESET_FAILED = _ximureceiver.ERR_FACTORY_RESET_FAILED
ERR_LOW_BATTERY = _ximureceiver.ERR_LOW_BATTERY
ERR_USB_RECEIVE_BUFFER_OVERRUN = _ximureceiver.ERR_USB_RECEIVE_BUFFER_OVERRUN
ERR_USB_TRANSMIT_BUFFER_OVERRUN = _ximureceiver.ERR_USB_TRANSMIT_BUFFER_OVERRUN
ERR_BLUETOOTH_RECEIVE_BUFFER_OVERRUN = _ximureceiver.ERR_BLUETOOTH_RECEIVE_BUFFER_OVERRUN
ERR_BLUETOOTH_TRANSMIT_BUFFER_OVERRUN = _ximureceiver.ERR_BLUETOOTH_TRANSMIT_BUFFER_OVERRUN
ERR_SD_CARD_WRITE_BUFFER_OVERRUN = _ximureceiver.ERR_SD_CARD_WRITE_BUFFER_OVERRUN
ERR_TOO_FEW_BYTES_IN_PACKET = _ximureceiver.ERR_TOO_FEW_BYTES_IN_PACKET
ERR_TOO_MANY_BYTES_IN_PACKET = _ximureceiver.ERR_TOO_MANY_BYTES_IN_PACKET
ERR_INVALID_CHECKSUM = _ximureceiver.ERR_INVALID_CHECKSUM
ERR_UNKNOWN_HEADER = _ximureceiver.ERR_UNKNOWN_HEADER
ERR_INVALID_NUM_BYTES_FOR_PACKET_HEADER = _ximureceiver.ERR_INVALID_NUM_BYTES_FOR_PACKET_HEADER
ERR_INVALID_REGISTER_ADDRESS = _ximureceiver.ERR_INVALID_REGISTER_ADDRESS
ERR_REGISTER_READ_ONLY = _ximureceiver.ERR_REGISTER_READ_ONLY
ERR_INVALID_REGSITER_VALUE = _ximureceiver.ERR_INVALID_REGSITER_VALUE
ERR_INVALID_COMMAND = _ximureceiver.ERR_INVALID_COMMAND
ERR_GYROSCOPE_AXIS_NOT_AT_200DPS = _ximureceiver.ERR_GYROSCOPE_AXIS_NOT_AT_200DPS
ERR_GYROSCOPE_NOT_STATIONARY = _ximureceiver.ERR_GYROSCOPE_NOT_STATIONARY
ERR_ACCELEROMETER_AXIS_NOT_AT_1G = _ximureceiver.ERR_ACCELEROMETER_AXIS_NOT_AT_1G
ERR_MMAGNETOMETER_SATURATION = _ximureceiver.ERR_MMAGNETOMETER_SATURATION
ERR_INCORRECT_AUXILIARY_PORT_MODE = _ximureceiver.ERR_INCORRECT_AUXILIARY_PORT_MODE
ERR_UART_RECEIVE_BUFFER_OVERRUN = _ximureceiver.ERR_UART_RECEIVE_BUFFER_OVERRUN
ERR_UART_TRANSMIT_BUFFER_OVERRUN = _ximureceiver.ERR_UART_TRANSMIT_BUFFER_OVERRUN
class BattAndThermStruct(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BattAndThermStruct, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BattAndThermStruct, name)
    __repr__ = _swig_repr
    __swig_setmethods__["battery"] = _ximureceiver.BattAndThermStruct_battery_set
    __swig_getmethods__["battery"] = _ximureceiver.BattAndThermStruct_battery_get
    if _newclass:battery = _swig_property(_ximureceiver.BattAndThermStruct_battery_get, _ximureceiver.BattAndThermStruct_battery_set)
    __swig_setmethods__["thermometer"] = _ximureceiver.BattAndThermStruct_thermometer_set
    __swig_getmethods__["thermometer"] = _ximureceiver.BattAndThermStruct_thermometer_get
    if _newclass:thermometer = _swig_property(_ximureceiver.BattAndThermStruct_thermometer_get, _ximureceiver.BattAndThermStruct_thermometer_set)
    def __init__(self): 
        this = _ximureceiver.new_BattAndThermStruct()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ximureceiver.delete_BattAndThermStruct
    __del__ = lambda self : None;
BattAndThermStruct_swigregister = _ximureceiver.BattAndThermStruct_swigregister
BattAndThermStruct_swigregister(BattAndThermStruct)

class InertialAndMagStruct(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InertialAndMagStruct, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InertialAndMagStruct, name)
    __repr__ = _swig_repr
    __swig_setmethods__["gyrX"] = _ximureceiver.InertialAndMagStruct_gyrX_set
    __swig_getmethods__["gyrX"] = _ximureceiver.InertialAndMagStruct_gyrX_get
    if _newclass:gyrX = _swig_property(_ximureceiver.InertialAndMagStruct_gyrX_get, _ximureceiver.InertialAndMagStruct_gyrX_set)
    __swig_setmethods__["gyrY"] = _ximureceiver.InertialAndMagStruct_gyrY_set
    __swig_getmethods__["gyrY"] = _ximureceiver.InertialAndMagStruct_gyrY_get
    if _newclass:gyrY = _swig_property(_ximureceiver.InertialAndMagStruct_gyrY_get, _ximureceiver.InertialAndMagStruct_gyrY_set)
    __swig_setmethods__["gyrZ"] = _ximureceiver.InertialAndMagStruct_gyrZ_set
    __swig_getmethods__["gyrZ"] = _ximureceiver.InertialAndMagStruct_gyrZ_get
    if _newclass:gyrZ = _swig_property(_ximureceiver.InertialAndMagStruct_gyrZ_get, _ximureceiver.InertialAndMagStruct_gyrZ_set)
    __swig_setmethods__["accX"] = _ximureceiver.InertialAndMagStruct_accX_set
    __swig_getmethods__["accX"] = _ximureceiver.InertialAndMagStruct_accX_get
    if _newclass:accX = _swig_property(_ximureceiver.InertialAndMagStruct_accX_get, _ximureceiver.InertialAndMagStruct_accX_set)
    __swig_setmethods__["accY"] = _ximureceiver.InertialAndMagStruct_accY_set
    __swig_getmethods__["accY"] = _ximureceiver.InertialAndMagStruct_accY_get
    if _newclass:accY = _swig_property(_ximureceiver.InertialAndMagStruct_accY_get, _ximureceiver.InertialAndMagStruct_accY_set)
    __swig_setmethods__["accZ"] = _ximureceiver.InertialAndMagStruct_accZ_set
    __swig_getmethods__["accZ"] = _ximureceiver.InertialAndMagStruct_accZ_get
    if _newclass:accZ = _swig_property(_ximureceiver.InertialAndMagStruct_accZ_get, _ximureceiver.InertialAndMagStruct_accZ_set)
    __swig_setmethods__["magX"] = _ximureceiver.InertialAndMagStruct_magX_set
    __swig_getmethods__["magX"] = _ximureceiver.InertialAndMagStruct_magX_get
    if _newclass:magX = _swig_property(_ximureceiver.InertialAndMagStruct_magX_get, _ximureceiver.InertialAndMagStruct_magX_set)
    __swig_setmethods__["magY"] = _ximureceiver.InertialAndMagStruct_magY_set
    __swig_getmethods__["magY"] = _ximureceiver.InertialAndMagStruct_magY_get
    if _newclass:magY = _swig_property(_ximureceiver.InertialAndMagStruct_magY_get, _ximureceiver.InertialAndMagStruct_magY_set)
    __swig_setmethods__["magZ"] = _ximureceiver.InertialAndMagStruct_magZ_set
    __swig_getmethods__["magZ"] = _ximureceiver.InertialAndMagStruct_magZ_get
    if _newclass:magZ = _swig_property(_ximureceiver.InertialAndMagStruct_magZ_get, _ximureceiver.InertialAndMagStruct_magZ_set)
    def __init__(self): 
        this = _ximureceiver.new_InertialAndMagStruct()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ximureceiver.delete_InertialAndMagStruct
    __del__ = lambda self : None;
InertialAndMagStruct_swigregister = _ximureceiver.InertialAndMagStruct_swigregister
InertialAndMagStruct_swigregister(InertialAndMagStruct)

class QuaternionStruct(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QuaternionStruct, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QuaternionStruct, name)
    __repr__ = _swig_repr
    __swig_setmethods__["w"] = _ximureceiver.QuaternionStruct_w_set
    __swig_getmethods__["w"] = _ximureceiver.QuaternionStruct_w_get
    if _newclass:w = _swig_property(_ximureceiver.QuaternionStruct_w_get, _ximureceiver.QuaternionStruct_w_set)
    __swig_setmethods__["x"] = _ximureceiver.QuaternionStruct_x_set
    __swig_getmethods__["x"] = _ximureceiver.QuaternionStruct_x_get
    if _newclass:x = _swig_property(_ximureceiver.QuaternionStruct_x_get, _ximureceiver.QuaternionStruct_x_set)
    __swig_setmethods__["y"] = _ximureceiver.QuaternionStruct_y_set
    __swig_getmethods__["y"] = _ximureceiver.QuaternionStruct_y_get
    if _newclass:y = _swig_property(_ximureceiver.QuaternionStruct_y_get, _ximureceiver.QuaternionStruct_y_set)
    __swig_setmethods__["z"] = _ximureceiver.QuaternionStruct_z_set
    __swig_getmethods__["z"] = _ximureceiver.QuaternionStruct_z_get
    if _newclass:z = _swig_property(_ximureceiver.QuaternionStruct_z_get, _ximureceiver.QuaternionStruct_z_set)
    def __init__(self): 
        this = _ximureceiver.new_QuaternionStruct()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ximureceiver.delete_QuaternionStruct
    __del__ = lambda self : None;
QuaternionStruct_swigregister = _ximureceiver.QuaternionStruct_swigregister
QuaternionStruct_swigregister(QuaternionStruct)

class XimuReceiver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, XimuReceiver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, XimuReceiver, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _ximureceiver.new_XimuReceiver()
        try: self.this.append(this)
        except: self.this = this
    def processNewChar(self, *args): return _ximureceiver.XimuReceiver_processNewChar(self, *args)
    def isBattAndThermGetReady(self): return _ximureceiver.XimuReceiver_isBattAndThermGetReady(self)
    def isInertialAndMagGetReady(self): return _ximureceiver.XimuReceiver_isInertialAndMagGetReady(self)
    def isQuaternionGetReady(self): return _ximureceiver.XimuReceiver_isQuaternionGetReady(self)
    def getBattAndTherm(self): return _ximureceiver.XimuReceiver_getBattAndTherm(self)
    def getInertialAndMag(self): return _ximureceiver.XimuReceiver_getInertialAndMag(self)
    def getQuaternion(self): return _ximureceiver.XimuReceiver_getQuaternion(self)
    __swig_destroy__ = _ximureceiver.delete_XimuReceiver
    __del__ = lambda self : None;
XimuReceiver_swigregister = _ximureceiver.XimuReceiver_swigregister
XimuReceiver_swigregister(XimuReceiver)

# This file is compatible with both classic and new-style classes.


