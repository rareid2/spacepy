# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cdfpy_interface', [dirname(__file__)])
        except ImportError:
            import _cdfpy_interface
            return _cdfpy_interface
        if fp is not None:
            try:
                _mod = imp.load_module('_cdfpy_interface', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cdfpy_interface = swig_import_helper()
    del swig_import_helper
else:
    import _cdfpy_interface
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
    if (not static) or hasattr(self,name):
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



def cdata(*args):
  return _cdfpy_interface.cdata(*args)
cdata = _cdfpy_interface.cdata

def memmove(*args):
  return _cdfpy_interface.memmove(*args)
memmove = _cdfpy_interface.memmove

def new_intArray(*args):
  return _cdfpy_interface.new_intArray(*args)
new_intArray = _cdfpy_interface.new_intArray

def delete_intArray(*args):
  return _cdfpy_interface.delete_intArray(*args)
delete_intArray = _cdfpy_interface.delete_intArray

def intArray_getitem(*args):
  return _cdfpy_interface.intArray_getitem(*args)
intArray_getitem = _cdfpy_interface.intArray_getitem

def intArray_setitem(*args):
  return _cdfpy_interface.intArray_setitem(*args)
intArray_setitem = _cdfpy_interface.intArray_setitem

def new_charArray(*args):
  return _cdfpy_interface.new_charArray(*args)
new_charArray = _cdfpy_interface.new_charArray

def delete_charArray(*args):
  return _cdfpy_interface.delete_charArray(*args)
delete_charArray = _cdfpy_interface.delete_charArray

def charArray_getitem(*args):
  return _cdfpy_interface.charArray_getitem(*args)
charArray_getitem = _cdfpy_interface.charArray_getitem

def charArray_setitem(*args):
  return _cdfpy_interface.charArray_setitem(*args)
charArray_setitem = _cdfpy_interface.charArray_setitem

def new_longArray(*args):
  return _cdfpy_interface.new_longArray(*args)
new_longArray = _cdfpy_interface.new_longArray

def delete_longArray(*args):
  return _cdfpy_interface.delete_longArray(*args)
delete_longArray = _cdfpy_interface.delete_longArray

def longArray_getitem(*args):
  return _cdfpy_interface.longArray_getitem(*args)
longArray_getitem = _cdfpy_interface.longArray_getitem

def longArray_setitem(*args):
  return _cdfpy_interface.longArray_setitem(*args)
longArray_setitem = _cdfpy_interface.longArray_setitem

def new_floatArray(*args):
  return _cdfpy_interface.new_floatArray(*args)
new_floatArray = _cdfpy_interface.new_floatArray

def delete_floatArray(*args):
  return _cdfpy_interface.delete_floatArray(*args)
delete_floatArray = _cdfpy_interface.delete_floatArray

def floatArray_getitem(*args):
  return _cdfpy_interface.floatArray_getitem(*args)
floatArray_getitem = _cdfpy_interface.floatArray_getitem

def floatArray_setitem(*args):
  return _cdfpy_interface.floatArray_setitem(*args)
floatArray_setitem = _cdfpy_interface.floatArray_setitem

def new_CDF_INT2Array(*args):
  return _cdfpy_interface.new_CDF_INT2Array(*args)
new_CDF_INT2Array = _cdfpy_interface.new_CDF_INT2Array

def delete_CDF_INT2Array(*args):
  return _cdfpy_interface.delete_CDF_INT2Array(*args)
delete_CDF_INT2Array = _cdfpy_interface.delete_CDF_INT2Array

def CDF_INT2Array_getitem(*args):
  return _cdfpy_interface.CDF_INT2Array_getitem(*args)
CDF_INT2Array_getitem = _cdfpy_interface.CDF_INT2Array_getitem

def CDF_INT2Array_setitem(*args):
  return _cdfpy_interface.CDF_INT2Array_setitem(*args)
CDF_INT2Array_setitem = _cdfpy_interface.CDF_INT2Array_setitem

def new_CDF_REAL4Array(*args):
  return _cdfpy_interface.new_CDF_REAL4Array(*args)
new_CDF_REAL4Array = _cdfpy_interface.new_CDF_REAL4Array

def delete_CDF_REAL4Array(*args):
  return _cdfpy_interface.delete_CDF_REAL4Array(*args)
delete_CDF_REAL4Array = _cdfpy_interface.delete_CDF_REAL4Array

def CDF_REAL4Array_getitem(*args):
  return _cdfpy_interface.CDF_REAL4Array_getitem(*args)
CDF_REAL4Array_getitem = _cdfpy_interface.CDF_REAL4Array_getitem

def CDF_REAL4Array_setitem(*args):
  return _cdfpy_interface.CDF_REAL4Array_setitem(*args)
CDF_REAL4Array_setitem = _cdfpy_interface.CDF_REAL4Array_setitem

def new_CDF_FLOATArray(*args):
  return _cdfpy_interface.new_CDF_FLOATArray(*args)
new_CDF_FLOATArray = _cdfpy_interface.new_CDF_FLOATArray

def delete_CDF_FLOATArray(*args):
  return _cdfpy_interface.delete_CDF_FLOATArray(*args)
delete_CDF_FLOATArray = _cdfpy_interface.delete_CDF_FLOATArray

def CDF_FLOATArray_getitem(*args):
  return _cdfpy_interface.CDF_FLOATArray_getitem(*args)
CDF_FLOATArray_getitem = _cdfpy_interface.CDF_FLOATArray_getitem

def CDF_FLOATArray_setitem(*args):
  return _cdfpy_interface.CDF_FLOATArray_setitem(*args)
CDF_FLOATArray_setitem = _cdfpy_interface.CDF_FLOATArray_setitem

def new_CDF_INT4Array(*args):
  return _cdfpy_interface.new_CDF_INT4Array(*args)
new_CDF_INT4Array = _cdfpy_interface.new_CDF_INT4Array

def delete_CDF_INT4Array(*args):
  return _cdfpy_interface.delete_CDF_INT4Array(*args)
delete_CDF_INT4Array = _cdfpy_interface.delete_CDF_INT4Array

def CDF_INT4Array_getitem(*args):
  return _cdfpy_interface.CDF_INT4Array_getitem(*args)
CDF_INT4Array_getitem = _cdfpy_interface.CDF_INT4Array_getitem

def CDF_INT4Array_setitem(*args):
  return _cdfpy_interface.CDF_INT4Array_setitem(*args)
CDF_INT4Array_setitem = _cdfpy_interface.CDF_INT4Array_setitem

def new_CDF_EPOCHArray(*args):
  return _cdfpy_interface.new_CDF_EPOCHArray(*args)
new_CDF_EPOCHArray = _cdfpy_interface.new_CDF_EPOCHArray

def delete_CDF_EPOCHArray(*args):
  return _cdfpy_interface.delete_CDF_EPOCHArray(*args)
delete_CDF_EPOCHArray = _cdfpy_interface.delete_CDF_EPOCHArray

def CDF_EPOCHArray_getitem(*args):
  return _cdfpy_interface.CDF_EPOCHArray_getitem(*args)
CDF_EPOCHArray_getitem = _cdfpy_interface.CDF_EPOCHArray_getitem

def CDF_EPOCHArray_setitem(*args):
  return _cdfpy_interface.CDF_EPOCHArray_setitem(*args)
CDF_EPOCHArray_setitem = _cdfpy_interface.CDF_EPOCHArray_setitem

def new_CDF_REAL8Array(*args):
  return _cdfpy_interface.new_CDF_REAL8Array(*args)
new_CDF_REAL8Array = _cdfpy_interface.new_CDF_REAL8Array

def delete_CDF_REAL8Array(*args):
  return _cdfpy_interface.delete_CDF_REAL8Array(*args)
delete_CDF_REAL8Array = _cdfpy_interface.delete_CDF_REAL8Array

def CDF_REAL8Array_getitem(*args):
  return _cdfpy_interface.CDF_REAL8Array_getitem(*args)
CDF_REAL8Array_getitem = _cdfpy_interface.CDF_REAL8Array_getitem

def CDF_REAL8Array_setitem(*args):
  return _cdfpy_interface.CDF_REAL8Array_setitem(*args)
CDF_REAL8Array_setitem = _cdfpy_interface.CDF_REAL8Array_setitem

def new_CDF_DOUBLEArray(*args):
  return _cdfpy_interface.new_CDF_DOUBLEArray(*args)
new_CDF_DOUBLEArray = _cdfpy_interface.new_CDF_DOUBLEArray

def delete_CDF_DOUBLEArray(*args):
  return _cdfpy_interface.delete_CDF_DOUBLEArray(*args)
delete_CDF_DOUBLEArray = _cdfpy_interface.delete_CDF_DOUBLEArray

def CDF_DOUBLEArray_getitem(*args):
  return _cdfpy_interface.CDF_DOUBLEArray_getitem(*args)
CDF_DOUBLEArray_getitem = _cdfpy_interface.CDF_DOUBLEArray_getitem

def CDF_DOUBLEArray_setitem(*args):
  return _cdfpy_interface.CDF_DOUBLEArray_setitem(*args)
CDF_DOUBLEArray_setitem = _cdfpy_interface.CDF_DOUBLEArray_setitem

def new_CDF_BYTEArray(*args):
  return _cdfpy_interface.new_CDF_BYTEArray(*args)
new_CDF_BYTEArray = _cdfpy_interface.new_CDF_BYTEArray

def delete_CDF_BYTEArray(*args):
  return _cdfpy_interface.delete_CDF_BYTEArray(*args)
delete_CDF_BYTEArray = _cdfpy_interface.delete_CDF_BYTEArray

def CDF_BYTEArray_getitem(*args):
  return _cdfpy_interface.CDF_BYTEArray_getitem(*args)
CDF_BYTEArray_getitem = _cdfpy_interface.CDF_BYTEArray_getitem

def CDF_BYTEArray_setitem(*args):
  return _cdfpy_interface.CDF_BYTEArray_setitem(*args)
CDF_BYTEArray_setitem = _cdfpy_interface.CDF_BYTEArray_setitem

def new_CDF_CHARArray(*args):
  return _cdfpy_interface.new_CDF_CHARArray(*args)
new_CDF_CHARArray = _cdfpy_interface.new_CDF_CHARArray

def delete_CDF_CHARArray(*args):
  return _cdfpy_interface.delete_CDF_CHARArray(*args)
delete_CDF_CHARArray = _cdfpy_interface.delete_CDF_CHARArray

def CDF_CHARArray_getitem(*args):
  return _cdfpy_interface.CDF_CHARArray_getitem(*args)
CDF_CHARArray_getitem = _cdfpy_interface.CDF_CHARArray_getitem

def CDF_CHARArray_setitem(*args):
  return _cdfpy_interface.CDF_CHARArray_setitem(*args)
CDF_CHARArray_setitem = _cdfpy_interface.CDF_CHARArray_setitem

def new_CDF_UCHARArray(*args):
  return _cdfpy_interface.new_CDF_UCHARArray(*args)
new_CDF_UCHARArray = _cdfpy_interface.new_CDF_UCHARArray

def delete_CDF_UCHARArray(*args):
  return _cdfpy_interface.delete_CDF_UCHARArray(*args)
delete_CDF_UCHARArray = _cdfpy_interface.delete_CDF_UCHARArray

def CDF_UCHARArray_getitem(*args):
  return _cdfpy_interface.CDF_UCHARArray_getitem(*args)
CDF_UCHARArray_getitem = _cdfpy_interface.CDF_UCHARArray_getitem

def CDF_UCHARArray_setitem(*args):
  return _cdfpy_interface.CDF_UCHARArray_setitem(*args)
CDF_UCHARArray_setitem = _cdfpy_interface.CDF_UCHARArray_setitem

def calloc_void(*args):
  return _cdfpy_interface.calloc_void(*args)
calloc_void = _cdfpy_interface.calloc_void

def free_void(*args):
  return _cdfpy_interface.free_void(*args)
free_void = _cdfpy_interface.free_void
CDF_MIN_DIMS = _cdfpy_interface.CDF_MIN_DIMS
CDF_MAX_DIMS = _cdfpy_interface.CDF_MAX_DIMS
CDF_VAR_NAME_LEN = _cdfpy_interface.CDF_VAR_NAME_LEN
CDF_ATTR_NAME_LEN = _cdfpy_interface.CDF_ATTR_NAME_LEN
CDF_VAR_NAME_LEN256 = _cdfpy_interface.CDF_VAR_NAME_LEN256
CDF_ATTR_NAME_LEN256 = _cdfpy_interface.CDF_ATTR_NAME_LEN256
CDF_COPYRIGHT_LEN = _cdfpy_interface.CDF_COPYRIGHT_LEN
CDF_STATUSTEXT_LEN = _cdfpy_interface.CDF_STATUSTEXT_LEN
CDF_PATHNAME_LEN = _cdfpy_interface.CDF_PATHNAME_LEN
EPOCH_STRING_LEN = _cdfpy_interface.EPOCH_STRING_LEN
EPOCH1_STRING_LEN = _cdfpy_interface.EPOCH1_STRING_LEN
EPOCH2_STRING_LEN = _cdfpy_interface.EPOCH2_STRING_LEN
EPOCH3_STRING_LEN = _cdfpy_interface.EPOCH3_STRING_LEN
EPOCH16_STRING_LEN = _cdfpy_interface.EPOCH16_STRING_LEN
EPOCH16_1_STRING_LEN = _cdfpy_interface.EPOCH16_1_STRING_LEN
EPOCH16_2_STRING_LEN = _cdfpy_interface.EPOCH16_2_STRING_LEN
EPOCH16_3_STRING_LEN = _cdfpy_interface.EPOCH16_3_STRING_LEN
EPOCHx_STRING_MAX = _cdfpy_interface.EPOCHx_STRING_MAX
EPOCHx_FORMAT_MAX = _cdfpy_interface.EPOCHx_FORMAT_MAX
CDF_INT1 = _cdfpy_interface.CDF_INT1
CDF_INT2 = _cdfpy_interface.CDF_INT2
CDF_INT4 = _cdfpy_interface.CDF_INT4
CDF_UINT1 = _cdfpy_interface.CDF_UINT1
CDF_UINT2 = _cdfpy_interface.CDF_UINT2
CDF_UINT4 = _cdfpy_interface.CDF_UINT4
CDF_REAL4 = _cdfpy_interface.CDF_REAL4
CDF_REAL8 = _cdfpy_interface.CDF_REAL8
CDF_EPOCH = _cdfpy_interface.CDF_EPOCH
CDF_EPOCH16 = _cdfpy_interface.CDF_EPOCH16
CDF_BYTE = _cdfpy_interface.CDF_BYTE
CDF_FLOAT = _cdfpy_interface.CDF_FLOAT
CDF_DOUBLE = _cdfpy_interface.CDF_DOUBLE
CDF_CHAR = _cdfpy_interface.CDF_CHAR
CDF_UCHAR = _cdfpy_interface.CDF_UCHAR
NETWORK_ENCODING = _cdfpy_interface.NETWORK_ENCODING
SUN_ENCODING = _cdfpy_interface.SUN_ENCODING
VAX_ENCODING = _cdfpy_interface.VAX_ENCODING
DECSTATION_ENCODING = _cdfpy_interface.DECSTATION_ENCODING
SGi_ENCODING = _cdfpy_interface.SGi_ENCODING
IBMPC_ENCODING = _cdfpy_interface.IBMPC_ENCODING
IBMRS_ENCODING = _cdfpy_interface.IBMRS_ENCODING
HOST_ENCODING = _cdfpy_interface.HOST_ENCODING
PPC_ENCODING = _cdfpy_interface.PPC_ENCODING
HP_ENCODING = _cdfpy_interface.HP_ENCODING
NeXT_ENCODING = _cdfpy_interface.NeXT_ENCODING
ALPHAOSF1_ENCODING = _cdfpy_interface.ALPHAOSF1_ENCODING
ALPHAVMSd_ENCODING = _cdfpy_interface.ALPHAVMSd_ENCODING
ALPHAVMSg_ENCODING = _cdfpy_interface.ALPHAVMSg_ENCODING
ALPHAVMSi_ENCODING = _cdfpy_interface.ALPHAVMSi_ENCODING
NETWORK_DECODING = _cdfpy_interface.NETWORK_DECODING
SUN_DECODING = _cdfpy_interface.SUN_DECODING
VAX_DECODING = _cdfpy_interface.VAX_DECODING
DECSTATION_DECODING = _cdfpy_interface.DECSTATION_DECODING
SGi_DECODING = _cdfpy_interface.SGi_DECODING
IBMPC_DECODING = _cdfpy_interface.IBMPC_DECODING
IBMRS_DECODING = _cdfpy_interface.IBMRS_DECODING
HOST_DECODING = _cdfpy_interface.HOST_DECODING
PPC_DECODING = _cdfpy_interface.PPC_DECODING
MAC_ENCODING = _cdfpy_interface.MAC_ENCODING
MAC_DECODING = _cdfpy_interface.MAC_DECODING
HP_DECODING = _cdfpy_interface.HP_DECODING
NeXT_DECODING = _cdfpy_interface.NeXT_DECODING
ALPHAOSF1_DECODING = _cdfpy_interface.ALPHAOSF1_DECODING
ALPHAVMSd_DECODING = _cdfpy_interface.ALPHAVMSd_DECODING
ALPHAVMSg_DECODING = _cdfpy_interface.ALPHAVMSg_DECODING
ALPHAVMSi_DECODING = _cdfpy_interface.ALPHAVMSi_DECODING
VARY = _cdfpy_interface.VARY
NOVARY = _cdfpy_interface.NOVARY
ROW_MAJOR = _cdfpy_interface.ROW_MAJOR
COLUMN_MAJOR = _cdfpy_interface.COLUMN_MAJOR
SINGLE_FILE = _cdfpy_interface.SINGLE_FILE
MULTI_FILE = _cdfpy_interface.MULTI_FILE
NO_CHECKSUM = _cdfpy_interface.NO_CHECKSUM
MD5_CHECKSUM = _cdfpy_interface.MD5_CHECKSUM
OTHER_CHECKSUM = _cdfpy_interface.OTHER_CHECKSUM
GLOBAL_SCOPE = _cdfpy_interface.GLOBAL_SCOPE
VARIABLE_SCOPE = _cdfpy_interface.VARIABLE_SCOPE
READONLYon = _cdfpy_interface.READONLYon
READONLYoff = _cdfpy_interface.READONLYoff
VALIDATEFILEon = _cdfpy_interface.VALIDATEFILEon
VALIDATEFILEoff = _cdfpy_interface.VALIDATEFILEoff
zMODEoff = _cdfpy_interface.zMODEoff
zMODEon1 = _cdfpy_interface.zMODEon1
zMODEon2 = _cdfpy_interface.zMODEon2
NEGtoPOSfp0on = _cdfpy_interface.NEGtoPOSfp0on
NEGtoPOSfp0off = _cdfpy_interface.NEGtoPOSfp0off
BACKWARDFILEon = _cdfpy_interface.BACKWARDFILEon
BACKWARDFILEoff = _cdfpy_interface.BACKWARDFILEoff
CDF_MAX_PARMS = _cdfpy_interface.CDF_MAX_PARMS
NO_COMPRESSION = _cdfpy_interface.NO_COMPRESSION
RLE_COMPRESSION = _cdfpy_interface.RLE_COMPRESSION
HUFF_COMPRESSION = _cdfpy_interface.HUFF_COMPRESSION
AHUFF_COMPRESSION = _cdfpy_interface.AHUFF_COMPRESSION
GZIP_COMPRESSION = _cdfpy_interface.GZIP_COMPRESSION
RLE_OF_ZEROs = _cdfpy_interface.RLE_OF_ZEROs
OPTIMAL_ENCODING_TREES = _cdfpy_interface.OPTIMAL_ENCODING_TREES
NO_SPARSEARRAYS = _cdfpy_interface.NO_SPARSEARRAYS
NO_SPARSERECORDS = _cdfpy_interface.NO_SPARSERECORDS
PAD_SPARSERECORDS = _cdfpy_interface.PAD_SPARSERECORDS
PREV_SPARSERECORDS = _cdfpy_interface.PREV_SPARSERECORDS
ILLEGAL_EPOCH_VALUE = _cdfpy_interface.ILLEGAL_EPOCH_VALUE
CREATE_ = _cdfpy_interface.CREATE_
OPEN_ = _cdfpy_interface.OPEN_
DELETE_ = _cdfpy_interface.DELETE_
CLOSE_ = _cdfpy_interface.CLOSE_
SELECT_ = _cdfpy_interface.SELECT_
CONFIRM_ = _cdfpy_interface.CONFIRM_
GET_ = _cdfpy_interface.GET_
PUT_ = _cdfpy_interface.PUT_
SAVE_ = _cdfpy_interface.SAVE_
BACKWARD_ = _cdfpy_interface.BACKWARD_
GETCDFFILEBACKWARD_ = _cdfpy_interface.GETCDFFILEBACKWARD_
CHECKSUM_ = _cdfpy_interface.CHECKSUM_
GETCDFCHECKSUM_ = _cdfpy_interface.GETCDFCHECKSUM_
VALIDATE_ = _cdfpy_interface.VALIDATE_
GETCDFVALIDATE_ = _cdfpy_interface.GETCDFVALIDATE_
NULL_ = _cdfpy_interface.NULL_
CDF_ = _cdfpy_interface.CDF_
CDF_NAME_ = _cdfpy_interface.CDF_NAME_
CDF_ENCODING_ = _cdfpy_interface.CDF_ENCODING_
CDF_DECODING_ = _cdfpy_interface.CDF_DECODING_
CDF_MAJORITY_ = _cdfpy_interface.CDF_MAJORITY_
CDF_FORMAT_ = _cdfpy_interface.CDF_FORMAT_
CDF_COPYRIGHT_ = _cdfpy_interface.CDF_COPYRIGHT_
CDF_NUMrVARS_ = _cdfpy_interface.CDF_NUMrVARS_
CDF_NUMzVARS_ = _cdfpy_interface.CDF_NUMzVARS_
CDF_NUMATTRS_ = _cdfpy_interface.CDF_NUMATTRS_
CDF_NUMgATTRS_ = _cdfpy_interface.CDF_NUMgATTRS_
CDF_NUMvATTRS_ = _cdfpy_interface.CDF_NUMvATTRS_
CDF_VERSION_ = _cdfpy_interface.CDF_VERSION_
CDF_RELEASE_ = _cdfpy_interface.CDF_RELEASE_
CDF_INCREMENT_ = _cdfpy_interface.CDF_INCREMENT_
CDF_STATUS_ = _cdfpy_interface.CDF_STATUS_
CDF_READONLY_MODE_ = _cdfpy_interface.CDF_READONLY_MODE_
CDF_zMODE_ = _cdfpy_interface.CDF_zMODE_
CDF_NEGtoPOSfp0_MODE_ = _cdfpy_interface.CDF_NEGtoPOSfp0_MODE_
LIB_COPYRIGHT_ = _cdfpy_interface.LIB_COPYRIGHT_
LIB_VERSION_ = _cdfpy_interface.LIB_VERSION_
LIB_RELEASE_ = _cdfpy_interface.LIB_RELEASE_
LIB_INCREMENT_ = _cdfpy_interface.LIB_INCREMENT_
LIB_subINCREMENT_ = _cdfpy_interface.LIB_subINCREMENT_
rVARs_NUMDIMS_ = _cdfpy_interface.rVARs_NUMDIMS_
rVARs_DIMSIZES_ = _cdfpy_interface.rVARs_DIMSIZES_
rVARs_MAXREC_ = _cdfpy_interface.rVARs_MAXREC_
rVARs_RECDATA_ = _cdfpy_interface.rVARs_RECDATA_
rVARs_RECNUMBER_ = _cdfpy_interface.rVARs_RECNUMBER_
rVARs_RECCOUNT_ = _cdfpy_interface.rVARs_RECCOUNT_
rVARs_RECINTERVAL_ = _cdfpy_interface.rVARs_RECINTERVAL_
rVARs_DIMINDICES_ = _cdfpy_interface.rVARs_DIMINDICES_
rVARs_DIMCOUNTS_ = _cdfpy_interface.rVARs_DIMCOUNTS_
rVARs_DIMINTERVALS_ = _cdfpy_interface.rVARs_DIMINTERVALS_
rVAR_ = _cdfpy_interface.rVAR_
rVAR_NAME_ = _cdfpy_interface.rVAR_NAME_
rVAR_DATATYPE_ = _cdfpy_interface.rVAR_DATATYPE_
rVAR_NUMELEMS_ = _cdfpy_interface.rVAR_NUMELEMS_
rVAR_RECVARY_ = _cdfpy_interface.rVAR_RECVARY_
rVAR_DIMVARYS_ = _cdfpy_interface.rVAR_DIMVARYS_
rVAR_NUMBER_ = _cdfpy_interface.rVAR_NUMBER_
rVAR_DATA_ = _cdfpy_interface.rVAR_DATA_
rVAR_HYPERDATA_ = _cdfpy_interface.rVAR_HYPERDATA_
rVAR_SEQDATA_ = _cdfpy_interface.rVAR_SEQDATA_
rVAR_SEQPOS_ = _cdfpy_interface.rVAR_SEQPOS_
rVAR_MAXREC_ = _cdfpy_interface.rVAR_MAXREC_
rVAR_MAXallocREC_ = _cdfpy_interface.rVAR_MAXallocREC_
rVAR_DATASPEC_ = _cdfpy_interface.rVAR_DATASPEC_
rVAR_PADVALUE_ = _cdfpy_interface.rVAR_PADVALUE_
rVAR_INITIALRECS_ = _cdfpy_interface.rVAR_INITIALRECS_
rVAR_BLOCKINGFACTOR_ = _cdfpy_interface.rVAR_BLOCKINGFACTOR_
rVAR_nINDEXRECORDS_ = _cdfpy_interface.rVAR_nINDEXRECORDS_
rVAR_nINDEXENTRIES_ = _cdfpy_interface.rVAR_nINDEXENTRIES_
rVAR_EXISTENCE_ = _cdfpy_interface.rVAR_EXISTENCE_
zVARs_MAXREC_ = _cdfpy_interface.zVARs_MAXREC_
zVARs_RECDATA_ = _cdfpy_interface.zVARs_RECDATA_
zVAR_ = _cdfpy_interface.zVAR_
zVAR_NAME_ = _cdfpy_interface.zVAR_NAME_
zVAR_DATATYPE_ = _cdfpy_interface.zVAR_DATATYPE_
zVAR_NUMELEMS_ = _cdfpy_interface.zVAR_NUMELEMS_
zVAR_NUMDIMS_ = _cdfpy_interface.zVAR_NUMDIMS_
zVAR_DIMSIZES_ = _cdfpy_interface.zVAR_DIMSIZES_
zVAR_RECVARY_ = _cdfpy_interface.zVAR_RECVARY_
zVAR_DIMVARYS_ = _cdfpy_interface.zVAR_DIMVARYS_
zVAR_NUMBER_ = _cdfpy_interface.zVAR_NUMBER_
zVAR_DATA_ = _cdfpy_interface.zVAR_DATA_
zVAR_HYPERDATA_ = _cdfpy_interface.zVAR_HYPERDATA_
zVAR_SEQDATA_ = _cdfpy_interface.zVAR_SEQDATA_
zVAR_SEQPOS_ = _cdfpy_interface.zVAR_SEQPOS_
zVAR_MAXREC_ = _cdfpy_interface.zVAR_MAXREC_
zVAR_MAXallocREC_ = _cdfpy_interface.zVAR_MAXallocREC_
zVAR_DATASPEC_ = _cdfpy_interface.zVAR_DATASPEC_
zVAR_PADVALUE_ = _cdfpy_interface.zVAR_PADVALUE_
zVAR_INITIALRECS_ = _cdfpy_interface.zVAR_INITIALRECS_
zVAR_BLOCKINGFACTOR_ = _cdfpy_interface.zVAR_BLOCKINGFACTOR_
zVAR_nINDEXRECORDS_ = _cdfpy_interface.zVAR_nINDEXRECORDS_
zVAR_nINDEXENTRIES_ = _cdfpy_interface.zVAR_nINDEXENTRIES_
zVAR_EXISTENCE_ = _cdfpy_interface.zVAR_EXISTENCE_
zVAR_RECNUMBER_ = _cdfpy_interface.zVAR_RECNUMBER_
zVAR_RECCOUNT_ = _cdfpy_interface.zVAR_RECCOUNT_
zVAR_RECINTERVAL_ = _cdfpy_interface.zVAR_RECINTERVAL_
zVAR_DIMINDICES_ = _cdfpy_interface.zVAR_DIMINDICES_
zVAR_DIMCOUNTS_ = _cdfpy_interface.zVAR_DIMCOUNTS_
zVAR_DIMINTERVALS_ = _cdfpy_interface.zVAR_DIMINTERVALS_
ATTR_ = _cdfpy_interface.ATTR_
ATTR_SCOPE_ = _cdfpy_interface.ATTR_SCOPE_
ATTR_NAME_ = _cdfpy_interface.ATTR_NAME_
ATTR_NUMBER_ = _cdfpy_interface.ATTR_NUMBER_
ATTR_MAXgENTRY_ = _cdfpy_interface.ATTR_MAXgENTRY_
ATTR_NUMgENTRIES_ = _cdfpy_interface.ATTR_NUMgENTRIES_
ATTR_MAXrENTRY_ = _cdfpy_interface.ATTR_MAXrENTRY_
ATTR_NUMrENTRIES_ = _cdfpy_interface.ATTR_NUMrENTRIES_
ATTR_MAXzENTRY_ = _cdfpy_interface.ATTR_MAXzENTRY_
ATTR_NUMzENTRIES_ = _cdfpy_interface.ATTR_NUMzENTRIES_
ATTR_EXISTENCE_ = _cdfpy_interface.ATTR_EXISTENCE_
gENTRY_ = _cdfpy_interface.gENTRY_
gENTRY_EXISTENCE_ = _cdfpy_interface.gENTRY_EXISTENCE_
gENTRY_DATATYPE_ = _cdfpy_interface.gENTRY_DATATYPE_
gENTRY_NUMELEMS_ = _cdfpy_interface.gENTRY_NUMELEMS_
gENTRY_DATASPEC_ = _cdfpy_interface.gENTRY_DATASPEC_
gENTRY_DATA_ = _cdfpy_interface.gENTRY_DATA_
rENTRY_ = _cdfpy_interface.rENTRY_
rENTRY_NAME_ = _cdfpy_interface.rENTRY_NAME_
rENTRY_EXISTENCE_ = _cdfpy_interface.rENTRY_EXISTENCE_
rENTRY_DATATYPE_ = _cdfpy_interface.rENTRY_DATATYPE_
rENTRY_NUMELEMS_ = _cdfpy_interface.rENTRY_NUMELEMS_
rENTRY_DATASPEC_ = _cdfpy_interface.rENTRY_DATASPEC_
rENTRY_DATA_ = _cdfpy_interface.rENTRY_DATA_
zENTRY_ = _cdfpy_interface.zENTRY_
zENTRY_NAME_ = _cdfpy_interface.zENTRY_NAME_
zENTRY_EXISTENCE_ = _cdfpy_interface.zENTRY_EXISTENCE_
zENTRY_DATATYPE_ = _cdfpy_interface.zENTRY_DATATYPE_
zENTRY_NUMELEMS_ = _cdfpy_interface.zENTRY_NUMELEMS_
zENTRY_DATASPEC_ = _cdfpy_interface.zENTRY_DATASPEC_
zENTRY_DATA_ = _cdfpy_interface.zENTRY_DATA_
STATUS_TEXT_ = _cdfpy_interface.STATUS_TEXT_
CDF_CACHESIZE_ = _cdfpy_interface.CDF_CACHESIZE_
rVARs_CACHESIZE_ = _cdfpy_interface.rVARs_CACHESIZE_
zVARs_CACHESIZE_ = _cdfpy_interface.zVARs_CACHESIZE_
rVAR_CACHESIZE_ = _cdfpy_interface.rVAR_CACHESIZE_
zVAR_CACHESIZE_ = _cdfpy_interface.zVAR_CACHESIZE_
zVARs_RECNUMBER_ = _cdfpy_interface.zVARs_RECNUMBER_
rVAR_ALLOCATERECS_ = _cdfpy_interface.rVAR_ALLOCATERECS_
zVAR_ALLOCATERECS_ = _cdfpy_interface.zVAR_ALLOCATERECS_
DATATYPE_SIZE_ = _cdfpy_interface.DATATYPE_SIZE_
CURgENTRY_EXISTENCE_ = _cdfpy_interface.CURgENTRY_EXISTENCE_
CURrENTRY_EXISTENCE_ = _cdfpy_interface.CURrENTRY_EXISTENCE_
CURzENTRY_EXISTENCE_ = _cdfpy_interface.CURzENTRY_EXISTENCE_
CDF_INFO_ = _cdfpy_interface.CDF_INFO_
CDF_COMPRESSION_ = _cdfpy_interface.CDF_COMPRESSION_
zVAR_COMPRESSION_ = _cdfpy_interface.zVAR_COMPRESSION_
zVAR_SPARSERECORDS_ = _cdfpy_interface.zVAR_SPARSERECORDS_
zVAR_SPARSEARRAYS_ = _cdfpy_interface.zVAR_SPARSEARRAYS_
zVAR_ALLOCATEBLOCK_ = _cdfpy_interface.zVAR_ALLOCATEBLOCK_
zVAR_NUMRECS_ = _cdfpy_interface.zVAR_NUMRECS_
zVAR_NUMallocRECS_ = _cdfpy_interface.zVAR_NUMallocRECS_
rVAR_COMPRESSION_ = _cdfpy_interface.rVAR_COMPRESSION_
rVAR_SPARSERECORDS_ = _cdfpy_interface.rVAR_SPARSERECORDS_
rVAR_SPARSEARRAYS_ = _cdfpy_interface.rVAR_SPARSEARRAYS_
rVAR_ALLOCATEBLOCK_ = _cdfpy_interface.rVAR_ALLOCATEBLOCK_
rVAR_NUMRECS_ = _cdfpy_interface.rVAR_NUMRECS_
rVAR_NUMallocRECS_ = _cdfpy_interface.rVAR_NUMallocRECS_
rVAR_ALLOCATEDFROM_ = _cdfpy_interface.rVAR_ALLOCATEDFROM_
rVAR_ALLOCATEDTO_ = _cdfpy_interface.rVAR_ALLOCATEDTO_
zVAR_ALLOCATEDFROM_ = _cdfpy_interface.zVAR_ALLOCATEDFROM_
zVAR_ALLOCATEDTO_ = _cdfpy_interface.zVAR_ALLOCATEDTO_
zVAR_nINDEXLEVELS_ = _cdfpy_interface.zVAR_nINDEXLEVELS_
rVAR_nINDEXLEVELS_ = _cdfpy_interface.rVAR_nINDEXLEVELS_
CDF_SCRATCHDIR_ = _cdfpy_interface.CDF_SCRATCHDIR_
rVAR_RESERVEPERCENT_ = _cdfpy_interface.rVAR_RESERVEPERCENT_
zVAR_RESERVEPERCENT_ = _cdfpy_interface.zVAR_RESERVEPERCENT_
rVAR_RECORDS_ = _cdfpy_interface.rVAR_RECORDS_
zVAR_RECORDS_ = _cdfpy_interface.zVAR_RECORDS_
STAGE_CACHESIZE_ = _cdfpy_interface.STAGE_CACHESIZE_
COMPRESS_CACHESIZE_ = _cdfpy_interface.COMPRESS_CACHESIZE_
CDF_CHECKSUM_ = _cdfpy_interface.CDF_CHECKSUM_
CDFwithSTATS_ = _cdfpy_interface.CDFwithSTATS_
CDF_ACCESS_ = _cdfpy_interface.CDF_ACCESS_

def CDFlib(*args):
  return _cdfpy_interface.CDFlib(*args)
CDFlib = _cdfpy_interface.CDFlib

def CDFcreateCDF(*args):
  return _cdfpy_interface.CDFcreateCDF(*args)
CDFcreateCDF = _cdfpy_interface.CDFcreateCDF

def CDFattrInquire(*args):
  return _cdfpy_interface.CDFattrInquire(*args)
CDFattrInquire = _cdfpy_interface.CDFattrInquire

def CDFinquireAttr(*args):
  return _cdfpy_interface.CDFinquireAttr(*args)
CDFinquireAttr = _cdfpy_interface.CDFinquireAttr

def CDFinquireAttrEntry(*args):
  return _cdfpy_interface.CDFinquireAttrEntry(*args)
CDFinquireAttrEntry = _cdfpy_interface.CDFinquireAttrEntry

def CDFinquireAttrInfo(*args):
  return _cdfpy_interface.CDFinquireAttrInfo(*args)
CDFinquireAttrInfo = _cdfpy_interface.CDFinquireAttrInfo

def CDFputAttrEntry(*args):
  return _cdfpy_interface.CDFputAttrEntry(*args)
CDFputAttrEntry = _cdfpy_interface.CDFputAttrEntry

def CDFgetAttrEntry(*args):
  return _cdfpy_interface.CDFgetAttrEntry(*args)
CDFgetAttrEntry = _cdfpy_interface.CDFgetAttrEntry

def CDFdeleteAttrEntry(*args):
  return _cdfpy_interface.CDFdeleteAttrEntry(*args)
CDFdeleteAttrEntry = _cdfpy_interface.CDFdeleteAttrEntry

def CDFsetAttrEntryDataSpec(*args):
  return _cdfpy_interface.CDFsetAttrEntryDataSpec(*args)
CDFsetAttrEntryDataSpec = _cdfpy_interface.CDFsetAttrEntryDataSpec

def CDFgetAttrNum(*args):
  return _cdfpy_interface.CDFgetAttrNum(*args)
CDFgetAttrNum = _cdfpy_interface.CDFgetAttrNum

def CDFgetVarNum(*args):
  return _cdfpy_interface.CDFgetVarNum(*args)
CDFgetVarNum = _cdfpy_interface.CDFgetVarNum

def CDFgetNumAttrEntries(*args):
  return _cdfpy_interface.CDFgetNumAttrEntries(*args)
CDFgetNumAttrEntries = _cdfpy_interface.CDFgetNumAttrEntries

def CDFgetAttrMaxEntry(*args):
  return _cdfpy_interface.CDFgetAttrMaxEntry(*args)
CDFgetAttrMaxEntry = _cdfpy_interface.CDFgetAttrMaxEntry

def CDFgetAttrEntryDataType(*args):
  return _cdfpy_interface.CDFgetAttrEntryDataType(*args)
CDFgetAttrEntryDataType = _cdfpy_interface.CDFgetAttrEntryDataType

def CDFgetAttrEntryNumElements(*args):
  return _cdfpy_interface.CDFgetAttrEntryNumElements(*args)
CDFgetAttrEntryNumElements = _cdfpy_interface.CDFgetAttrEntryNumElements

def CDFgetVarRecordData(*args):
  return _cdfpy_interface.CDFgetVarRecordData(*args)
CDFgetVarRecordData = _cdfpy_interface.CDFgetVarRecordData

def CDFputVarRecordData(*args):
  return _cdfpy_interface.CDFputVarRecordData(*args)
CDFputVarRecordData = _cdfpy_interface.CDFputVarRecordData

def CDFgetVarsRecordDatabyNames(*args):
  return _cdfpy_interface.CDFgetVarsRecordDatabyNames(*args)
CDFgetVarsRecordDatabyNames = _cdfpy_interface.CDFgetVarsRecordDatabyNames

def CDFputVarsRecordDatabyNames(*args):
  return _cdfpy_interface.CDFputVarsRecordDatabyNames(*args)
CDFputVarsRecordDatabyNames = _cdfpy_interface.CDFputVarsRecordDatabyNames

def CDFsetFileBackward(*args):
  return _cdfpy_interface.CDFsetFileBackward(*args)
CDFsetFileBackward = _cdfpy_interface.CDFsetFileBackward

def CDFsetFileBackwardFlag(*args):
  return _cdfpy_interface.CDFsetFileBackwardFlag(*args)
CDFsetFileBackwardFlag = _cdfpy_interface.CDFsetFileBackwardFlag

def CDFgetFileBackward():
  return _cdfpy_interface.CDFgetFileBackward()
CDFgetFileBackward = _cdfpy_interface.CDFgetFileBackward

def CDFgetFileBackwardFlag():
  return _cdfpy_interface.CDFgetFileBackwardFlag()
CDFgetFileBackwardFlag = _cdfpy_interface.CDFgetFileBackwardFlag

def CDFsetChecksumMode(*args):
  return _cdfpy_interface.CDFsetChecksumMode(*args)
CDFsetChecksumMode = _cdfpy_interface.CDFsetChecksumMode

def CDFgetChecksumMode():
  return _cdfpy_interface.CDFgetChecksumMode()
CDFgetChecksumMode = _cdfpy_interface.CDFgetChecksumMode

def CDFgetFileBackwardEnvVar():
  return _cdfpy_interface.CDFgetFileBackwardEnvVar()
CDFgetFileBackwardEnvVar = _cdfpy_interface.CDFgetFileBackwardEnvVar

def CDFsetValidate(*args):
  return _cdfpy_interface.CDFsetValidate(*args)
CDFsetValidate = _cdfpy_interface.CDFsetValidate

def CDFgetValidate():
  return _cdfpy_interface.CDFgetValidate()
CDFgetValidate = _cdfpy_interface.CDFgetValidate

def CDFgetValidateDebug():
  return _cdfpy_interface.CDFgetValidateDebug()
CDFgetValidateDebug = _cdfpy_interface.CDFgetValidateDebug

def EPOCHbreakdown(*args):
  return _cdfpy_interface.EPOCHbreakdown(*args)
EPOCHbreakdown = _cdfpy_interface.EPOCHbreakdown

def computeEPOCH(*args):
  return _cdfpy_interface.computeEPOCH(*args)
computeEPOCH = _cdfpy_interface.computeEPOCH

def parseEPOCH(*args):
  return _cdfpy_interface.parseEPOCH(*args)
parseEPOCH = _cdfpy_interface.parseEPOCH

def parseEPOCH1(*args):
  return _cdfpy_interface.parseEPOCH1(*args)
parseEPOCH1 = _cdfpy_interface.parseEPOCH1

def parseEPOCH2(*args):
  return _cdfpy_interface.parseEPOCH2(*args)
parseEPOCH2 = _cdfpy_interface.parseEPOCH2

def parseEPOCH3(*args):
  return _cdfpy_interface.parseEPOCH3(*args)
parseEPOCH3 = _cdfpy_interface.parseEPOCH3

def encodeEPOCH(*args):
  return _cdfpy_interface.encodeEPOCH(*args)
encodeEPOCH = _cdfpy_interface.encodeEPOCH

def encodeEPOCH1(*args):
  return _cdfpy_interface.encodeEPOCH1(*args)
encodeEPOCH1 = _cdfpy_interface.encodeEPOCH1

def encodeEPOCH2(*args):
  return _cdfpy_interface.encodeEPOCH2(*args)
encodeEPOCH2 = _cdfpy_interface.encodeEPOCH2

def encodeEPOCH3(*args):
  return _cdfpy_interface.encodeEPOCH3(*args)
encodeEPOCH3 = _cdfpy_interface.encodeEPOCH3

def encodeEPOCHx(*args):
  return _cdfpy_interface.encodeEPOCHx(*args)
encodeEPOCHx = _cdfpy_interface.encodeEPOCHx

def EPOCH16breakdown(*args):
  return _cdfpy_interface.EPOCH16breakdown(*args)
EPOCH16breakdown = _cdfpy_interface.EPOCH16breakdown

def computeEPOCH16(*args):
  return _cdfpy_interface.computeEPOCH16(*args)
computeEPOCH16 = _cdfpy_interface.computeEPOCH16

def parseEPOCH16(*args):
  return _cdfpy_interface.parseEPOCH16(*args)
parseEPOCH16 = _cdfpy_interface.parseEPOCH16

def parseEPOCH16_1(*args):
  return _cdfpy_interface.parseEPOCH16_1(*args)
parseEPOCH16_1 = _cdfpy_interface.parseEPOCH16_1

def parseEPOCH16_2(*args):
  return _cdfpy_interface.parseEPOCH16_2(*args)
parseEPOCH16_2 = _cdfpy_interface.parseEPOCH16_2

def parseEPOCH16_3(*args):
  return _cdfpy_interface.parseEPOCH16_3(*args)
parseEPOCH16_3 = _cdfpy_interface.parseEPOCH16_3

def encodeEPOCH16(*args):
  return _cdfpy_interface.encodeEPOCH16(*args)
encodeEPOCH16 = _cdfpy_interface.encodeEPOCH16

def encodeEPOCH16_1(*args):
  return _cdfpy_interface.encodeEPOCH16_1(*args)
encodeEPOCH16_1 = _cdfpy_interface.encodeEPOCH16_1

def encodeEPOCH16_2(*args):
  return _cdfpy_interface.encodeEPOCH16_2(*args)
encodeEPOCH16_2 = _cdfpy_interface.encodeEPOCH16_2

def encodeEPOCH16_3(*args):
  return _cdfpy_interface.encodeEPOCH16_3(*args)
encodeEPOCH16_3 = _cdfpy_interface.encodeEPOCH16_3

def encodeEPOCH16_x(*args):
  return _cdfpy_interface.encodeEPOCH16_x(*args)
encodeEPOCH16_x = _cdfpy_interface.encodeEPOCH16_x
CDF_DOCUMENT_LEN = _cdfpy_interface.CDF_DOCUMENT_LEN
CDF_ERRTEXT_LEN = _cdfpy_interface.CDF_ERRTEXT_LEN
CDF_NUMDIMS_ = _cdfpy_interface.CDF_NUMDIMS_
CDF_DIMSIZES_ = _cdfpy_interface.CDF_DIMSIZES_
CDF_MAXREC_ = _cdfpy_interface.CDF_MAXREC_
CDF_RECNUMBER_ = _cdfpy_interface.CDF_RECNUMBER_
CDF_RECCOUNT_ = _cdfpy_interface.CDF_RECCOUNT_
CDF_RECINTERVAL_ = _cdfpy_interface.CDF_RECINTERVAL_
CDF_DIMINDICES_ = _cdfpy_interface.CDF_DIMINDICES_
CDF_DIMCOUNTS_ = _cdfpy_interface.CDF_DIMCOUNTS_
CDF_DIMINTERVALS_ = _cdfpy_interface.CDF_DIMINTERVALS_
CDF_NUMVARS_ = _cdfpy_interface.CDF_NUMVARS_
VAR_ = _cdfpy_interface.VAR_
VAR_NAME_ = _cdfpy_interface.VAR_NAME_
VAR_DATATYPE_ = _cdfpy_interface.VAR_DATATYPE_
VAR_NUMELEMS_ = _cdfpy_interface.VAR_NUMELEMS_
VAR_RECVARY_ = _cdfpy_interface.VAR_RECVARY_
VAR_DIMVARYS_ = _cdfpy_interface.VAR_DIMVARYS_
VAR_NUMBER_ = _cdfpy_interface.VAR_NUMBER_
VAR_DATA_ = _cdfpy_interface.VAR_DATA_
VAR_HYPERDATA_ = _cdfpy_interface.VAR_HYPERDATA_
VAR_SEQDATA_ = _cdfpy_interface.VAR_SEQDATA_
VAR_SEQPOS_ = _cdfpy_interface.VAR_SEQPOS_
VAR_MAXREC_ = _cdfpy_interface.VAR_MAXREC_
VAR_DATASPEC_ = _cdfpy_interface.VAR_DATASPEC_
VAR_FILLVALUE_ = _cdfpy_interface.VAR_FILLVALUE_
VAR_INITIALRECS_ = _cdfpy_interface.VAR_INITIALRECS_
VAR_EXTENDRECS_ = _cdfpy_interface.VAR_EXTENDRECS_
ATTR_MAXENTRY_ = _cdfpy_interface.ATTR_MAXENTRY_
ATTR_NUMENTRIES_ = _cdfpy_interface.ATTR_NUMENTRIES_
ENTRY_ = _cdfpy_interface.ENTRY_
ENTRY_DATATYPE_ = _cdfpy_interface.ENTRY_DATATYPE_
ENTRY_NUMELEMS_ = _cdfpy_interface.ENTRY_NUMELEMS_
ENTRY_DATA_ = _cdfpy_interface.ENTRY_DATA_
MIPSEL_ENCODING = _cdfpy_interface.MIPSEL_ENCODING
MIPSEB_ENCODING = _cdfpy_interface.MIPSEB_ENCODING
rVAR_EXISTANCE_ = _cdfpy_interface.rVAR_EXISTANCE_
zVAR_EXISTANCE_ = _cdfpy_interface.zVAR_EXISTANCE_
ATTR_EXISTANCE_ = _cdfpy_interface.ATTR_EXISTANCE_
gENTRY_EXISTANCE_ = _cdfpy_interface.gENTRY_EXISTANCE_
rENTRY_EXISTANCE_ = _cdfpy_interface.rENTRY_EXISTANCE_
zENTRY_EXISTANCE_ = _cdfpy_interface.zENTRY_EXISTANCE_
GLOBAL_SCOPE_ASSUMED = _cdfpy_interface.GLOBAL_SCOPE_ASSUMED
VARIABLE_SCOPE_ASSUMED = _cdfpy_interface.VARIABLE_SCOPE_ASSUMED
rVAR_EXTENDRECS_ = _cdfpy_interface.rVAR_EXTENDRECS_
zVAR_EXTENDRECS_ = _cdfpy_interface.zVAR_EXTENDRECS_
COL_MAJOR = _cdfpy_interface.COL_MAJOR
NONE_CHECKSUM = _cdfpy_interface.NONE_CHECKSUM

def new_intp():
  return _cdfpy_interface.new_intp()
new_intp = _cdfpy_interface.new_intp

def copy_intp(*args):
  return _cdfpy_interface.copy_intp(*args)
copy_intp = _cdfpy_interface.copy_intp

def delete_intp(*args):
  return _cdfpy_interface.delete_intp(*args)
delete_intp = _cdfpy_interface.delete_intp

def intp_assign(*args):
  return _cdfpy_interface.intp_assign(*args)
intp_assign = _cdfpy_interface.intp_assign

def intp_value(*args):
  return _cdfpy_interface.intp_value(*args)
intp_value = _cdfpy_interface.intp_value

def new_doublep():
  return _cdfpy_interface.new_doublep()
new_doublep = _cdfpy_interface.new_doublep

def copy_doublep(*args):
  return _cdfpy_interface.copy_doublep(*args)
copy_doublep = _cdfpy_interface.copy_doublep

def delete_doublep(*args):
  return _cdfpy_interface.delete_doublep(*args)
delete_doublep = _cdfpy_interface.delete_doublep

def doublep_assign(*args):
  return _cdfpy_interface.doublep_assign(*args)
doublep_assign = _cdfpy_interface.doublep_assign

def doublep_value(*args):
  return _cdfpy_interface.doublep_value(*args)
doublep_value = _cdfpy_interface.doublep_value

def new_charp():
  return _cdfpy_interface.new_charp()
new_charp = _cdfpy_interface.new_charp

def copy_charp(*args):
  return _cdfpy_interface.copy_charp(*args)
copy_charp = _cdfpy_interface.copy_charp

def delete_charp(*args):
  return _cdfpy_interface.delete_charp(*args)
delete_charp = _cdfpy_interface.delete_charp

def charp_assign(*args):
  return _cdfpy_interface.charp_assign(*args)
charp_assign = _cdfpy_interface.charp_assign

def charp_value(*args):
  return _cdfpy_interface.charp_value(*args)
charp_value = _cdfpy_interface.charp_value

def new_longp():
  return _cdfpy_interface.new_longp()
new_longp = _cdfpy_interface.new_longp

def copy_longp(*args):
  return _cdfpy_interface.copy_longp(*args)
copy_longp = _cdfpy_interface.copy_longp

def delete_longp(*args):
  return _cdfpy_interface.delete_longp(*args)
delete_longp = _cdfpy_interface.delete_longp

def longp_assign(*args):
  return _cdfpy_interface.longp_assign(*args)
longp_assign = _cdfpy_interface.longp_assign

def longp_value(*args):
  return _cdfpy_interface.longp_value(*args)
longp_value = _cdfpy_interface.longp_value

def new_CDFidp():
  return _cdfpy_interface.new_CDFidp()
new_CDFidp = _cdfpy_interface.new_CDFidp

def copy_CDFidp(*args):
  return _cdfpy_interface.copy_CDFidp(*args)
copy_CDFidp = _cdfpy_interface.copy_CDFidp

def delete_CDFidp(*args):
  return _cdfpy_interface.delete_CDFidp(*args)
delete_CDFidp = _cdfpy_interface.delete_CDFidp

def CDFidp_assign(*args):
  return _cdfpy_interface.CDFidp_assign(*args)
CDFidp_assign = _cdfpy_interface.CDFidp_assign

def CDFidp_value(*args):
  return _cdfpy_interface.CDFidp_value(*args)
CDFidp_value = _cdfpy_interface.CDFidp_value

def PyCDFcreate(*args):
  return _cdfpy_interface.PyCDFcreate(*args)
PyCDFcreate = _cdfpy_interface.PyCDFcreate

def int_array(*args):
  return _cdfpy_interface.int_array(*args)
int_array = _cdfpy_interface.int_array

def PyCDFopen(*args):
  return _cdfpy_interface.PyCDFopen(*args)
PyCDFopen = _cdfpy_interface.PyCDFopen

def PyCDFcloseCDF(*args):
  return _cdfpy_interface.PyCDFcloseCDF(*args)
PyCDFcloseCDF = _cdfpy_interface.PyCDFcloseCDF

def PyCDFinquire(*args):
  return _cdfpy_interface.PyCDFinquire(*args)
PyCDFinquire = _cdfpy_interface.PyCDFinquire

def PyCDFinquireCDF(*args):
  return _cdfpy_interface.PyCDFinquireCDF(*args)
PyCDFinquireCDF = _cdfpy_interface.PyCDFinquireCDF

def PyCDFgetAttrName(*args):
  return _cdfpy_interface.PyCDFgetAttrName(*args)
PyCDFgetAttrName = _cdfpy_interface.PyCDFgetAttrName

def PyCDFinquireAttr(*args):
  return _cdfpy_interface.PyCDFinquireAttr(*args)
PyCDFinquireAttr = _cdfpy_interface.PyCDFinquireAttr

def PyCDFinquirezVar(*args):
  return _cdfpy_interface.PyCDFinquirezVar(*args)
PyCDFinquirezVar = _cdfpy_interface.PyCDFinquirezVar

def PyCDFinquirerVar(*args):
  return _cdfpy_interface.PyCDFinquirerVar(*args)
PyCDFinquirerVar = _cdfpy_interface.PyCDFinquirerVar

def PyCDFinquireAttrgEntry(*args):
  return _cdfpy_interface.PyCDFinquireAttrgEntry(*args)
PyCDFinquireAttrgEntry = _cdfpy_interface.PyCDFinquireAttrgEntry

def PyCDFgetAttrgEntry(*args):
  return _cdfpy_interface.PyCDFgetAttrgEntry(*args)
PyCDFgetAttrgEntry = _cdfpy_interface.PyCDFgetAttrgEntry

def PyCDFcreateAttr(*args):
  return _cdfpy_interface.PyCDFcreateAttr(*args)
PyCDFcreateAttr = _cdfpy_interface.PyCDFcreateAttr

def PyCDFinquireAttrzEntry(*args):
  return _cdfpy_interface.PyCDFinquireAttrzEntry(*args)
PyCDFinquireAttrzEntry = _cdfpy_interface.PyCDFinquireAttrzEntry

def PyCDFgetAttrzEntryDataType(*args):
  return _cdfpy_interface.PyCDFgetAttrzEntryDataType(*args)
PyCDFgetAttrzEntryDataType = _cdfpy_interface.PyCDFgetAttrzEntryDataType

def PyCDFgetAttrzEntryNumElements(*args):
  return _cdfpy_interface.PyCDFgetAttrzEntryNumElements(*args)
PyCDFgetAttrzEntryNumElements = _cdfpy_interface.PyCDFgetAttrzEntryNumElements

def PyCDFgetAttrzEntry(*args):
  return _cdfpy_interface.PyCDFgetAttrzEntry(*args)
PyCDFgetAttrzEntry = _cdfpy_interface.PyCDFgetAttrzEntry

def PyCDFgetAttrNum(*args):
  return _cdfpy_interface.PyCDFgetAttrNum(*args)
PyCDFgetAttrNum = _cdfpy_interface.PyCDFgetAttrNum

def PyCDFgetzVarAllocRecords(*args):
  return _cdfpy_interface.PyCDFgetzVarAllocRecords(*args)
PyCDFgetzVarAllocRecords = _cdfpy_interface.PyCDFgetzVarAllocRecords

def PyCDFgetzVarRecordData(*args):
  return _cdfpy_interface.PyCDFgetzVarRecordData(*args)
PyCDFgetzVarRecordData = _cdfpy_interface.PyCDFgetzVarRecordData

def PyCDFhyperGetzVarData(*args):
  return _cdfpy_interface.PyCDFhyperGetzVarData(*args)
PyCDFhyperGetzVarData = _cdfpy_interface.PyCDFhyperGetzVarData

def PyCDFgetCompression(*args):
  return _cdfpy_interface.PyCDFgetCompression(*args)
PyCDFgetCompression = _cdfpy_interface.PyCDFgetCompression


