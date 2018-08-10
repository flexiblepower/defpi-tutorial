# service/model/InflexibleControllerEfi20/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b550fb16b19cc058aca9062a23ea1ae456ced48d
# Generated 2018-08-10 09:05:39.930062 by PyXB version 1.2.6 using Python 3.6.6.final.0
# Namespace http://www.flexiblepower.org/efi-2

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8d6f1928-9c7c-11e8-8822-0242ac110003')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.flexiblepower.org/efi-2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.flexiblepower.org/efi-2}InstructionStatus
class InstructionStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstructionStatus')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 87, 1)
    _Documentation = None
InstructionStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InstructionStatus, enum_prefix=None)
InstructionStatus.ACCEPTED = InstructionStatus._CF_enumeration.addEnumeration(unicode_value='ACCEPTED', tag='ACCEPTED')
InstructionStatus.STARTED = InstructionStatus._CF_enumeration.addEnumeration(unicode_value='STARTED', tag='STARTED')
InstructionStatus.SUCCEEDED = InstructionStatus._CF_enumeration.addEnumeration(unicode_value='SUCCEEDED', tag='SUCCEEDED')
InstructionStatus.REJECTED = InstructionStatus._CF_enumeration.addEnumeration(unicode_value='REJECTED', tag='REJECTED')
InstructionStatus.ABORTED = InstructionStatus._CF_enumeration.addEnumeration(unicode_value='ABORTED', tag='ABORTED')
InstructionStatus._InitializeFacetMap(InstructionStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InstructionStatus', InstructionStatus)
_module_typeBindings.InstructionStatus = InstructionStatus

# Atomic simple type: {http://www.flexiblepower.org/efi-2}CommodityEnum
class CommodityEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommodityEnum')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 114, 1)
    _Documentation = None
CommodityEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CommodityEnum, enum_prefix=None)
CommodityEnum.ELECTRICITY = CommodityEnum._CF_enumeration.addEnumeration(unicode_value='ELECTRICITY', tag='ELECTRICITY')
CommodityEnum.GAS = CommodityEnum._CF_enumeration.addEnumeration(unicode_value='GAS', tag='GAS')
CommodityEnum.HEAT = CommodityEnum._CF_enumeration.addEnumeration(unicode_value='HEAT', tag='HEAT')
CommodityEnum._InitializeFacetMap(CommodityEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CommodityEnum', CommodityEnum)
_module_typeBindings.CommodityEnum = CommodityEnum

# Atomic simple type: {http://www.flexiblepower.org/efi-2}CurtailmentQuantity
class CurtailmentQuantity (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurtailmentQuantity')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 121, 1)
    _Documentation = None
CurtailmentQuantity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurtailmentQuantity, enum_prefix=None)
CurtailmentQuantity.ELECTRICITY_POWER = CurtailmentQuantity._CF_enumeration.addEnumeration(unicode_value='ELECTRICITY.POWER', tag='ELECTRICITY_POWER')
CurtailmentQuantity.GAS_FLOWRATE = CurtailmentQuantity._CF_enumeration.addEnumeration(unicode_value='GAS.FLOWRATE', tag='GAS_FLOWRATE')
CurtailmentQuantity.HEAT_TEMPERATURE = CurtailmentQuantity._CF_enumeration.addEnumeration(unicode_value='HEAT.TEMPERATURE', tag='HEAT_TEMPERATURE')
CurtailmentQuantity.HEAT_FLOWRATE = CurtailmentQuantity._CF_enumeration.addEnumeration(unicode_value='HEAT.FLOWRATE', tag='HEAT_FLOWRATE')
CurtailmentQuantity.HEAT_THERMALPOWER = CurtailmentQuantity._CF_enumeration.addEnumeration(unicode_value='HEAT.THERMALPOWER', tag='HEAT_THERMALPOWER')
CurtailmentQuantity._InitializeFacetMap(CurtailmentQuantity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CurtailmentQuantity', CurtailmentQuantity)
_module_typeBindings.CurtailmentQuantity = CurtailmentQuantity

# Atomic simple type: {http://www.flexiblepower.org/efi-2}CurrencyType
class CurrencyType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 469, 1)
    _Documentation = None
CurrencyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurrencyType, enum_prefix=None)
CurrencyType.AED = CurrencyType._CF_enumeration.addEnumeration(unicode_value='AED', tag='AED')
CurrencyType.ANG = CurrencyType._CF_enumeration.addEnumeration(unicode_value='ANG', tag='ANG')
CurrencyType.AUD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='AUD', tag='AUD')
CurrencyType.CHE = CurrencyType._CF_enumeration.addEnumeration(unicode_value='CHE', tag='CHE')
CurrencyType.CHF = CurrencyType._CF_enumeration.addEnumeration(unicode_value='CHF', tag='CHF')
CurrencyType.CHW = CurrencyType._CF_enumeration.addEnumeration(unicode_value='CHW', tag='CHW')
CurrencyType.EUR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
CurrencyType.GBP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
CurrencyType.LBP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='LBP', tag='LBP')
CurrencyType.LKR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='LKR', tag='LKR')
CurrencyType.LRD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='LRD', tag='LRD')
CurrencyType.LSL = CurrencyType._CF_enumeration.addEnumeration(unicode_value='LSL', tag='LSL')
CurrencyType.LYD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='LYD', tag='LYD')
CurrencyType.MAD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MAD', tag='MAD')
CurrencyType.MDL = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MDL', tag='MDL')
CurrencyType.MGA = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MGA', tag='MGA')
CurrencyType.MKD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MKD', tag='MKD')
CurrencyType.MMK = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MMK', tag='MMK')
CurrencyType.MNT = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MNT', tag='MNT')
CurrencyType.MOP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MOP', tag='MOP')
CurrencyType.MRO = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MRO', tag='MRO')
CurrencyType.MUR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MUR', tag='MUR')
CurrencyType.MVR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MVR', tag='MVR')
CurrencyType.MWK = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MWK', tag='MWK')
CurrencyType.MXN = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MXN', tag='MXN')
CurrencyType.MXV = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MXV', tag='MXV')
CurrencyType.MYR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MYR', tag='MYR')
CurrencyType.MZN = CurrencyType._CF_enumeration.addEnumeration(unicode_value='MZN', tag='MZN')
CurrencyType.NAD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='NAD', tag='NAD')
CurrencyType.NGN = CurrencyType._CF_enumeration.addEnumeration(unicode_value='NGN', tag='NGN')
CurrencyType.NIO = CurrencyType._CF_enumeration.addEnumeration(unicode_value='NIO', tag='NIO')
CurrencyType.NOK = CurrencyType._CF_enumeration.addEnumeration(unicode_value='NOK', tag='NOK')
CurrencyType.NPR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='NPR', tag='NPR')
CurrencyType.NZD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='NZD', tag='NZD')
CurrencyType.OMR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='OMR', tag='OMR')
CurrencyType.PAB = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PAB', tag='PAB')
CurrencyType.PEN = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PEN', tag='PEN')
CurrencyType.PGK = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PGK', tag='PGK')
CurrencyType.PHP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PHP', tag='PHP')
CurrencyType.PKR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PKR', tag='PKR')
CurrencyType.PLN = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PLN', tag='PLN')
CurrencyType.PYG = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PYG', tag='PYG')
CurrencyType.QAR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='QAR', tag='QAR')
CurrencyType.RON = CurrencyType._CF_enumeration.addEnumeration(unicode_value='RON', tag='RON')
CurrencyType.RSD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='RSD', tag='RSD')
CurrencyType.RUB = CurrencyType._CF_enumeration.addEnumeration(unicode_value='RUB', tag='RUB')
CurrencyType.RWF = CurrencyType._CF_enumeration.addEnumeration(unicode_value='RWF', tag='RWF')
CurrencyType.SAR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SAR', tag='SAR')
CurrencyType.SBD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SBD', tag='SBD')
CurrencyType.SCR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SCR', tag='SCR')
CurrencyType.SDG = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SDG', tag='SDG')
CurrencyType.SEK = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
CurrencyType.SGD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SGD', tag='SGD')
CurrencyType.SHP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SHP', tag='SHP')
CurrencyType.SLL = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SLL', tag='SLL')
CurrencyType.SOS = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SOS', tag='SOS')
CurrencyType.SRD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SRD', tag='SRD')
CurrencyType.SSP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SSP', tag='SSP')
CurrencyType.STD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='STD', tag='STD')
CurrencyType.SYP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SYP', tag='SYP')
CurrencyType.SZL = CurrencyType._CF_enumeration.addEnumeration(unicode_value='SZL', tag='SZL')
CurrencyType.THB = CurrencyType._CF_enumeration.addEnumeration(unicode_value='THB', tag='THB')
CurrencyType.TJS = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TJS', tag='TJS')
CurrencyType.TMT = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TMT', tag='TMT')
CurrencyType.TND = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TND', tag='TND')
CurrencyType.TOP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TOP', tag='TOP')
CurrencyType.TRY = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TRY', tag='TRY')
CurrencyType.TTD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TTD', tag='TTD')
CurrencyType.TWD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TWD', tag='TWD')
CurrencyType.TZS = CurrencyType._CF_enumeration.addEnumeration(unicode_value='TZS', tag='TZS')
CurrencyType.UAH = CurrencyType._CF_enumeration.addEnumeration(unicode_value='UAH', tag='UAH')
CurrencyType.UGX = CurrencyType._CF_enumeration.addEnumeration(unicode_value='UGX', tag='UGX')
CurrencyType.USD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='USD', tag='USD')
CurrencyType.USN = CurrencyType._CF_enumeration.addEnumeration(unicode_value='USN', tag='USN')
CurrencyType.UYI = CurrencyType._CF_enumeration.addEnumeration(unicode_value='UYI', tag='UYI')
CurrencyType.UYU = CurrencyType._CF_enumeration.addEnumeration(unicode_value='UYU', tag='UYU')
CurrencyType.UZS = CurrencyType._CF_enumeration.addEnumeration(unicode_value='UZS', tag='UZS')
CurrencyType.VEF = CurrencyType._CF_enumeration.addEnumeration(unicode_value='VEF', tag='VEF')
CurrencyType.VND = CurrencyType._CF_enumeration.addEnumeration(unicode_value='VND', tag='VND')
CurrencyType.VUV = CurrencyType._CF_enumeration.addEnumeration(unicode_value='VUV', tag='VUV')
CurrencyType.WST = CurrencyType._CF_enumeration.addEnumeration(unicode_value='WST', tag='WST')
CurrencyType.XAG = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XAG', tag='XAG')
CurrencyType.XAU = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XAU', tag='XAU')
CurrencyType.XBA = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XBA', tag='XBA')
CurrencyType.XBB = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XBB', tag='XBB')
CurrencyType.XBC = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XBC', tag='XBC')
CurrencyType.XBD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XBD', tag='XBD')
CurrencyType.XCD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XCD', tag='XCD')
CurrencyType.XOF = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XOF', tag='XOF')
CurrencyType.XPD = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XPD', tag='XPD')
CurrencyType.XPF = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XPF', tag='XPF')
CurrencyType.XPT = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XPT', tag='XPT')
CurrencyType.XSU = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XSU', tag='XSU')
CurrencyType.XTS = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XTS', tag='XTS')
CurrencyType.XUA = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XUA', tag='XUA')
CurrencyType.XXX = CurrencyType._CF_enumeration.addEnumeration(unicode_value='XXX', tag='XXX')
CurrencyType.YER = CurrencyType._CF_enumeration.addEnumeration(unicode_value='YER', tag='YER')
CurrencyType.ZAR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='ZAR', tag='ZAR')
CurrencyType.ZMW = CurrencyType._CF_enumeration.addEnumeration(unicode_value='ZMW', tag='ZMW')
CurrencyType.ZWL = CurrencyType._CF_enumeration.addEnumeration(unicode_value='ZWL', tag='ZWL')
CurrencyType._InitializeFacetMap(CurrencyType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CurrencyType', CurrencyType)
_module_typeBindings.CurrencyType = CurrencyType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 712, 4)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.double(0.0))
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.double(1.0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive,
   STD_ANON._CF_maxInclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 786, 4)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.double(0.0))
STD_ANON_._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.double(1.0))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive,
   STD_ANON_._CF_maxInclusive)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 903, 7)
    _Documentation = None
STD_ANON_2._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_2, value=pyxb.binding.datatypes.double(0.0))
STD_ANON_2._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_2, value=pyxb.binding.datatypes.double(1.0))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minInclusive,
   STD_ANON_2._CF_maxInclusive)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 925, 7)
    _Documentation = None
STD_ANON_3._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_3, value=pyxb.binding.datatypes.double(0.0))
STD_ANON_3._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_3, value=pyxb.binding.datatypes.double(1.0))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_minInclusive,
   STD_ANON_3._CF_maxInclusive)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: {http://www.flexiblepower.org/efi-2}DeviceClass
class DeviceClass (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeviceClass')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 938, 1)
    _Documentation = None
DeviceClass._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeviceClass, enum_prefix=None)
DeviceClass.Refrigerator = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Refrigerator', tag='Refrigerator')
DeviceClass.Freezer = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Freezer', tag='Freezer')
DeviceClass.Water_Cooler = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Water Cooler', tag='Water_Cooler')
DeviceClass.Water_Heater = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Water Heater', tag='Water_Heater')
DeviceClass.Washing_Machine = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Washing Machine', tag='Washing_Machine')
DeviceClass.Clothes_Dryer = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Clothes Dryer', tag='Clothes_Dryer')
DeviceClass.Combo_Washer_Dryer = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Combo Washer Dryer', tag='Combo_Washer_Dryer')
DeviceClass.Drying_Cabinet = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Drying Cabinet', tag='Drying_Cabinet')
DeviceClass.Dishwasher = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Dishwasher', tag='Dishwasher')
DeviceClass.Heatpump = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Heatpump', tag='Heatpump')
DeviceClass.Micro_CHP = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Micro-CHP', tag='Micro_CHP')
DeviceClass.Stationary_Battery = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Stationary Battery', tag='Stationary_Battery')
DeviceClass.Electrical_Vehicle = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Electrical Vehicle', tag='Electrical_Vehicle')
DeviceClass.PV_Panel = DeviceClass._CF_enumeration.addEnumeration(unicode_value='PV Panel', tag='PV_Panel')
DeviceClass.Windmill = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Windmill', tag='Windmill')
DeviceClass.Solar_Collector = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Solar Collector', tag='Solar_Collector')
DeviceClass.Air_Conditioner = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Air Conditioner', tag='Air_Conditioner')
DeviceClass.Ventilation = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Ventilation', tag='Ventilation')
DeviceClass.Air_Quality_Appliance = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Air Quality Appliance', tag='Air_Quality_Appliance')
DeviceClass.Gas_Geater = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Gas Geater', tag='Gas_Geater')
DeviceClass.Floor_Heating = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Floor Heating', tag='Floor_Heating')
DeviceClass.Generator = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Generator', tag='Generator')
DeviceClass.Miscellaneous = DeviceClass._CF_enumeration.addEnumeration(unicode_value='Miscellaneous', tag='Miscellaneous')
DeviceClass._InitializeFacetMap(DeviceClass._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeviceClass', DeviceClass)
_module_typeBindings.DeviceClass = DeviceClass

# Atomic simple type: {http://www.flexiblepower.org/efi-2}Identifier
class Identifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 965, 1)
    _Documentation = None
Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
Identifier._CF_pattern.addPattern(pattern='[a-zA-Z0-9\\-_:]{2,64}')
Identifier._InitializeFacetMap(Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Identifier', Identifier)
_module_typeBindings.Identifier = Identifier

# Complex type {http://www.flexiblepower.org/efi-2}EfiMessage with content type ELEMENT_ONLY
class EfiMessage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}EfiMessage with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EfiMessage')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 22, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'header'), 'header', '__httpwww_flexiblepower_orgefi_2_EfiMessage_httpwww_flexiblepower_orgefi_2header', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3), )

    
    header = property(__header.value, __header.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}efiVersion uses Python identifier efiVersion
    __efiVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'efiVersion'), 'efiVersion', '__httpwww_flexiblepower_orgefi_2_EfiMessage_httpwww_flexiblepower_orgefi_2efiVersion', pyxb.binding.datatypes.string, fixed=True, unicode_default='2.0', required=True)
    __efiVersion._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 33, 2)
    __efiVersion._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 33, 2)
    
    efiVersion = property(__efiVersion.value, __efiVersion.set, None, None)

    _ElementMap.update({
        __header.name() : __header
    })
    _AttributeMap.update({
        __efiVersion.name() : __efiVersion
    })
_module_typeBindings.EfiMessage = EfiMessage
Namespace.addCategoryObject('typeBinding', 'EfiMessage', EfiMessage)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 25, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}efiResourceId uses Python identifier efiResourceId
    __efiResourceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'efiResourceId'), 'efiResourceId', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_httpwww_flexiblepower_orgefi_2efiResourceId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 27, 6), )

    
    efiResourceId = property(__efiResourceId.value, __efiResourceId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_httpwww_flexiblepower_orgefi_2timestamp', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 28, 6), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    _ElementMap.update({
        __efiResourceId.name() : __efiResourceId,
        __timestamp.name() : __timestamp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.flexiblepower.org/efi-2}DeviceDescription with content type ELEMENT_ONLY
class DeviceDescription (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}DeviceDescription with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeviceDescription')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}deviceClass uses Python identifier deviceClass
    __deviceClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deviceClass'), 'deviceClass', '__httpwww_flexiblepower_orgefi_2_DeviceDescription_httpwww_flexiblepower_orgefi_2deviceClass', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 37, 3), )

    
    deviceClass = property(__deviceClass.value, __deviceClass.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}serialNumber uses Python identifier serialNumber
    __serialNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serialNumber'), 'serialNumber', '__httpwww_flexiblepower_orgefi_2_DeviceDescription_httpwww_flexiblepower_orgefi_2serialNumber', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 38, 3), )

    
    serialNumber = property(__serialNumber.value, __serialNumber.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__httpwww_flexiblepower_orgefi_2_DeviceDescription_httpwww_flexiblepower_orgefi_2label', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 39, 3), )

    
    label = property(__label.value, __label.set, None, None)

    _ElementMap.update({
        __deviceClass.name() : __deviceClass,
        __serialNumber.name() : __serialNumber,
        __label.name() : __label
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DeviceDescription = DeviceDescription
Namespace.addCategoryObject('typeBinding', 'DeviceDescription', DeviceDescription)


# Complex type {http://www.flexiblepower.org/efi-2}ProbabilityAttributes with content type EMPTY
class ProbabilityAttributes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ProbabilityAttributes with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProbabilityAttributes')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 130, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}the68PPRLower uses Python identifier the68PPRLower
    __the68PPRLower = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'the68PPRLower'), 'the68PPRLower', '__httpwww_flexiblepower_orgefi_2_ProbabilityAttributes_httpwww_flexiblepower_orgefi_2the68PPRLower', pyxb.binding.datatypes.double, required=True)
    __the68PPRLower._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 131, 2)
    __the68PPRLower._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 131, 2)
    
    the68PPRLower = property(__the68PPRLower.value, __the68PPRLower.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}the95PPRLower uses Python identifier the95PPRLower
    __the95PPRLower = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'the95PPRLower'), 'the95PPRLower', '__httpwww_flexiblepower_orgefi_2_ProbabilityAttributes_httpwww_flexiblepower_orgefi_2the95PPRLower', pyxb.binding.datatypes.double, required=True)
    __the95PPRLower._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 132, 2)
    __the95PPRLower._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 132, 2)
    
    the95PPRLower = property(__the95PPRLower.value, __the95PPRLower.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}expected uses Python identifier expected
    __expected = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'expected'), 'expected', '__httpwww_flexiblepower_orgefi_2_ProbabilityAttributes_httpwww_flexiblepower_orgefi_2expected', pyxb.binding.datatypes.double, required=True)
    __expected._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 133, 2)
    __expected._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 133, 2)
    
    expected = property(__expected.value, __expected.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}the95PPRUpper uses Python identifier the95PPRUpper
    __the95PPRUpper = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'the95PPRUpper'), 'the95PPRUpper', '__httpwww_flexiblepower_orgefi_2_ProbabilityAttributes_httpwww_flexiblepower_orgefi_2the95PPRUpper', pyxb.binding.datatypes.double, required=True)
    __the95PPRUpper._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 134, 2)
    __the95PPRUpper._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 134, 2)
    
    the95PPRUpper = property(__the95PPRUpper.value, __the95PPRUpper.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}the68PPRUpper uses Python identifier the68PPRUpper
    __the68PPRUpper = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'the68PPRUpper'), 'the68PPRUpper', '__httpwww_flexiblepower_orgefi_2_ProbabilityAttributes_httpwww_flexiblepower_orgefi_2the68PPRUpper', pyxb.binding.datatypes.double, required=True)
    __the68PPRUpper._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 135, 2)
    __the68PPRUpper._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 135, 2)
    
    the68PPRUpper = property(__the68PPRUpper.value, __the68PPRUpper.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __the68PPRLower.name() : __the68PPRLower,
        __the95PPRLower.name() : __the95PPRLower,
        __expected.name() : __expected,
        __the95PPRUpper.name() : __the95PPRUpper,
        __the68PPRUpper.name() : __the68PPRUpper
    })
_module_typeBindings.ProbabilityAttributes = ProbabilityAttributes
Namespace.addCategoryObject('typeBinding', 'ProbabilityAttributes', ProbabilityAttributes)


# Complex type {http://www.flexiblepower.org/efi-2}StorageUsageProfile with content type ELEMENT_ONLY
class StorageUsageProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageUsageProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageUsageProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 144, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'element'), 'element', '__httpwww_flexiblepower_orgefi_2_StorageUsageProfile_httpwww_flexiblepower_orgefi_2element', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 146, 3), )

    
    element = property(__element.value, __element.set, None, None)

    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StorageUsageProfile = StorageUsageProfile
Namespace.addCategoryObject('typeBinding', 'StorageUsageProfile', StorageUsageProfile)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 147, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_CTD_ANON__httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 148, 5)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 148, 5)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}usageRate uses Python identifier usageRate
    __usageRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'usageRate'), 'usageRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON__httpwww_flexiblepower_orgefi_2usageRate', pyxb.binding.datatypes.double, required=True)
    __usageRate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 149, 5)
    __usageRate._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 149, 5)
    
    usageRate = property(__usageRate.value, __usageRate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration,
        __usageRate.name() : __usageRate
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.flexiblepower.org/efi-2}StorageUsageProbabilityProfile with content type ELEMENT_ONLY
class StorageUsageProbabilityProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageUsageProbabilityProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageUsageProbabilityProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 154, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}usageRateElement uses Python identifier usageRateElement
    __usageRateElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usageRateElement'), 'usageRateElement', '__httpwww_flexiblepower_orgefi_2_StorageUsageProbabilityProfile_httpwww_flexiblepower_orgefi_2usageRateElement', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 156, 3), )

    
    usageRateElement = property(__usageRateElement.value, __usageRateElement.set, None, None)

    _ElementMap.update({
        __usageRateElement.name() : __usageRateElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StorageUsageProbabilityProfile = StorageUsageProbabilityProfile
Namespace.addCategoryObject('typeBinding', 'StorageUsageProbabilityProfile', StorageUsageProbabilityProfile)


# Complex type {http://www.flexiblepower.org/efi-2}ElectricityProfile with content type ELEMENT_ONLY
class ElectricityProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ElectricityProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElectricityProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 159, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'element'), 'element', '__httpwww_flexiblepower_orgefi_2_ElectricityProfile_httpwww_flexiblepower_orgefi_2element', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 161, 3), )

    
    element = property(__element.value, __element.set, None, None)

    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ElectricityProfile = ElectricityProfile
Namespace.addCategoryObject('typeBinding', 'ElectricityProfile', ElectricityProfile)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 162, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_2_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 163, 5)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 163, 5)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}power uses Python identifier power
    __power = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'power'), 'power', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_2_httpwww_flexiblepower_orgefi_2power', pyxb.binding.datatypes.double, required=True)
    __power._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 164, 5)
    __power._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 164, 5)
    
    power = property(__power.value, __power.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration,
        __power.name() : __power
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.flexiblepower.org/efi-2}ElectricityProbabilityProfile with content type ELEMENT_ONLY
class ElectricityProbabilityProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ElectricityProbabilityProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElectricityProbabilityProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 169, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}powerElement uses Python identifier powerElement
    __powerElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'powerElement'), 'powerElement', '__httpwww_flexiblepower_orgefi_2_ElectricityProbabilityProfile_httpwww_flexiblepower_orgefi_2powerElement', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 171, 3), )

    
    powerElement = property(__powerElement.value, __powerElement.set, None, None)

    _ElementMap.update({
        __powerElement.name() : __powerElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ElectricityProbabilityProfile = ElectricityProbabilityProfile
Namespace.addCategoryObject('typeBinding', 'ElectricityProbabilityProfile', ElectricityProbabilityProfile)


# Complex type {http://www.flexiblepower.org/efi-2}GasProfile with content type ELEMENT_ONLY
class GasProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}GasProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GasProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 174, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'element'), 'element', '__httpwww_flexiblepower_orgefi_2_GasProfile_httpwww_flexiblepower_orgefi_2element', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 176, 3), )

    
    element = property(__element.value, __element.set, None, None)

    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GasProfile = GasProfile
Namespace.addCategoryObject('typeBinding', 'GasProfile', GasProfile)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 177, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_3_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 178, 5)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 178, 5)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}flowRate uses Python identifier flowRate
    __flowRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'flowRate'), 'flowRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_3_httpwww_flexiblepower_orgefi_2flowRate', pyxb.binding.datatypes.double, required=True)
    __flowRate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 179, 5)
    __flowRate._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 179, 5)
    
    flowRate = property(__flowRate.value, __flowRate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration,
        __flowRate.name() : __flowRate
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://www.flexiblepower.org/efi-2}GasProbabilityProfile with content type ELEMENT_ONLY
class GasProbabilityProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}GasProbabilityProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GasProbabilityProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 184, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}flowRateElement uses Python identifier flowRateElement
    __flowRateElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flowRateElement'), 'flowRateElement', '__httpwww_flexiblepower_orgefi_2_GasProbabilityProfile_httpwww_flexiblepower_orgefi_2flowRateElement', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 186, 3), )

    
    flowRateElement = property(__flowRateElement.value, __flowRateElement.set, None, None)

    _ElementMap.update({
        __flowRateElement.name() : __flowRateElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GasProbabilityProfile = GasProbabilityProfile
Namespace.addCategoryObject('typeBinding', 'GasProbabilityProfile', GasProbabilityProfile)


# Complex type {http://www.flexiblepower.org/efi-2}HeatProfile with content type ELEMENT_ONLY
class HeatProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}HeatProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HeatProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 189, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'element'), 'element', '__httpwww_flexiblepower_orgefi_2_HeatProfile_httpwww_flexiblepower_orgefi_2element', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 191, 3), )

    
    element = property(__element.value, __element.set, None, None)

    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HeatProfile = HeatProfile
Namespace.addCategoryObject('typeBinding', 'HeatProfile', HeatProfile)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 192, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_4_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 193, 5)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 193, 5)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'temperature'), 'temperature', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_4_httpwww_flexiblepower_orgefi_2temperature', pyxb.binding.datatypes.double)
    __temperature._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 194, 5)
    __temperature._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 194, 5)
    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}flowRate uses Python identifier flowRate
    __flowRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'flowRate'), 'flowRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_4_httpwww_flexiblepower_orgefi_2flowRate', pyxb.binding.datatypes.double)
    __flowRate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 195, 5)
    __flowRate._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 195, 5)
    
    flowRate = property(__flowRate.value, __flowRate.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}thermalPower uses Python identifier thermalPower
    __thermalPower = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'thermalPower'), 'thermalPower', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_4_httpwww_flexiblepower_orgefi_2thermalPower', pyxb.binding.datatypes.double)
    __thermalPower._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 196, 5)
    __thermalPower._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 196, 5)
    
    thermalPower = property(__thermalPower.value, __thermalPower.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration,
        __temperature.name() : __temperature,
        __flowRate.name() : __flowRate,
        __thermalPower.name() : __thermalPower
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.flexiblepower.org/efi-2}HeatProbabilityProfile with content type ELEMENT_ONLY
class HeatProbabilityProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}HeatProbabilityProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HeatProbabilityProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 201, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'element'), 'element', '__httpwww_flexiblepower_orgefi_2_HeatProbabilityProfile_httpwww_flexiblepower_orgefi_2element', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 203, 3), )

    
    element = property(__element.value, __element.set, None, None)

    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HeatProbabilityProfile = HeatProbabilityProfile
Namespace.addCategoryObject('typeBinding', 'HeatProbabilityProfile', HeatProbabilityProfile)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 204, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'temperature'), 'temperature', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_5_httpwww_flexiblepower_orgefi_2temperature', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 206, 6), )

    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}flowRate uses Python identifier flowRate
    __flowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flowRate'), 'flowRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_5_httpwww_flexiblepower_orgefi_2flowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 207, 6), )

    
    flowRate = property(__flowRate.value, __flowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}thermalPower uses Python identifier thermalPower
    __thermalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'thermalPower'), 'thermalPower', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_5_httpwww_flexiblepower_orgefi_2thermalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 208, 6), )

    
    thermalPower = property(__thermalPower.value, __thermalPower.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_5_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 210, 5)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 210, 5)
    
    duration = property(__duration.value, __duration.set, None, None)

    _ElementMap.update({
        __temperature.name() : __temperature,
        __flowRate.name() : __flowRate,
        __thermalPower.name() : __thermalPower
    })
    _AttributeMap.update({
        __duration.name() : __duration
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type {http://www.flexiblepower.org/efi-2}SupportedCommodities with content type ELEMENT_ONLY
class SupportedCommodities (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}SupportedCommodities with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedCommodities')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 226, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}commodityType uses Python identifier commodityType
    __commodityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'commodityType'), 'commodityType', '__httpwww_flexiblepower_orgefi_2_SupportedCommodities_httpwww_flexiblepower_orgefi_2commodityType', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 228, 3), )

    
    commodityType = property(__commodityType.value, __commodityType.set, None, None)

    _ElementMap.update({
        __commodityType.name() : __commodityType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SupportedCommodities = SupportedCommodities
Namespace.addCategoryObject('typeBinding', 'SupportedCommodities', SupportedCommodities)


# Complex type {http://www.flexiblepower.org/efi-2}CurtailmentOptions with content type ELEMENT_ONLY
class CurtailmentOptions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}CurtailmentOptions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurtailmentOptions')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 231, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}curtailmentOption uses Python identifier curtailmentOption
    __curtailmentOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'curtailmentOption'), 'curtailmentOption', '__httpwww_flexiblepower_orgefi_2_CurtailmentOptions_httpwww_flexiblepower_orgefi_2curtailmentOption', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 233, 3), )

    
    curtailmentOption = property(__curtailmentOption.value, __curtailmentOption.set, None, None)

    _ElementMap.update({
        __curtailmentOption.name() : __curtailmentOption
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CurtailmentOptions = CurtailmentOptions
Namespace.addCategoryObject('typeBinding', 'CurtailmentOptions', CurtailmentOptions)


# Complex type {http://www.flexiblepower.org/efi-2}CurtailmentRange with content type EMPTY
class CurtailmentRange (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}CurtailmentRange with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurtailmentRange')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 243, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}lowerBound uses Python identifier lowerBound
    __lowerBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lowerBound'), 'lowerBound', '__httpwww_flexiblepower_orgefi_2_CurtailmentRange_httpwww_flexiblepower_orgefi_2lowerBound', pyxb.binding.datatypes.double, required=True)
    __lowerBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 244, 2)
    __lowerBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 244, 2)
    
    lowerBound = property(__lowerBound.value, __lowerBound.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}upperBound uses Python identifier upperBound
    __upperBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'upperBound'), 'upperBound', '__httpwww_flexiblepower_orgefi_2_CurtailmentRange_httpwww_flexiblepower_orgefi_2upperBound', pyxb.binding.datatypes.double, required=True)
    __upperBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 245, 2)
    __upperBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 245, 2)
    
    upperBound = property(__upperBound.value, __upperBound.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lowerBound.name() : __lowerBound,
        __upperBound.name() : __upperBound
    })
_module_typeBindings.CurtailmentRange = CurtailmentRange
Namespace.addCategoryObject('typeBinding', 'CurtailmentRange', CurtailmentRange)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 259, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}power uses Python identifier power
    __power = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'power'), 'power', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_6_httpwww_flexiblepower_orgefi_2power', pyxb.binding.datatypes.double, required=True)
    __power._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 260, 8)
    __power._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 260, 8)
    
    power = property(__power.value, __power.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __power.name() : __power
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 264, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}flowRate uses Python identifier flowRate
    __flowRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'flowRate'), 'flowRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_7_httpwww_flexiblepower_orgefi_2flowRate', pyxb.binding.datatypes.double, required=True)
    __flowRate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 265, 8)
    __flowRate._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 265, 8)
    
    flowRate = property(__flowRate.value, __flowRate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __flowRate.name() : __flowRate
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 269, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'temperature'), 'temperature', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_8_httpwww_flexiblepower_orgefi_2temperature', pyxb.binding.datatypes.double)
    __temperature._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 270, 8)
    __temperature._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 270, 8)
    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}flowRate uses Python identifier flowRate
    __flowRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'flowRate'), 'flowRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_8_httpwww_flexiblepower_orgefi_2flowRate', pyxb.binding.datatypes.double)
    __flowRate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 271, 8)
    __flowRate._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 271, 8)
    
    flowRate = property(__flowRate.value, __flowRate.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}thermalPower uses Python identifier thermalPower
    __thermalPower = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'thermalPower'), 'thermalPower', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_8_httpwww_flexiblepower_orgefi_2thermalPower', pyxb.binding.datatypes.double)
    __thermalPower._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 272, 8)
    __thermalPower._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 272, 8)
    
    thermalPower = property(__thermalPower.value, __thermalPower.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __temperature.name() : __temperature,
        __flowRate.name() : __flowRate,
        __thermalPower.name() : __thermalPower
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type {http://www.flexiblepower.org/efi-2}ProfileContainer with content type ELEMENT_ONLY
class ProfileContainer (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ProfileContainer with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProfileContainer')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 291, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}electricityProfile uses Python identifier electricityProfile
    __electricityProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electricityProfile'), 'electricityProfile', '__httpwww_flexiblepower_orgefi_2_ProfileContainer_httpwww_flexiblepower_orgefi_2electricityProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 294, 4), )

    
    electricityProfile = property(__electricityProfile.value, __electricityProfile.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}electricityProbabilityProfile uses Python identifier electricityProbabilityProfile
    __electricityProbabilityProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electricityProbabilityProfile'), 'electricityProbabilityProfile', '__httpwww_flexiblepower_orgefi_2_ProfileContainer_httpwww_flexiblepower_orgefi_2electricityProbabilityProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 295, 4), )

    
    electricityProbabilityProfile = property(__electricityProbabilityProfile.value, __electricityProbabilityProfile.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}gasProfile uses Python identifier gasProfile
    __gasProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gasProfile'), 'gasProfile', '__httpwww_flexiblepower_orgefi_2_ProfileContainer_httpwww_flexiblepower_orgefi_2gasProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 298, 4), )

    
    gasProfile = property(__gasProfile.value, __gasProfile.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}gasProbabilityProfile uses Python identifier gasProbabilityProfile
    __gasProbabilityProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gasProbabilityProfile'), 'gasProbabilityProfile', '__httpwww_flexiblepower_orgefi_2_ProfileContainer_httpwww_flexiblepower_orgefi_2gasProbabilityProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 299, 4), )

    
    gasProbabilityProfile = property(__gasProbabilityProfile.value, __gasProbabilityProfile.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatProfile uses Python identifier heatProfile
    __heatProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatProfile'), 'heatProfile', '__httpwww_flexiblepower_orgefi_2_ProfileContainer_httpwww_flexiblepower_orgefi_2heatProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 302, 4), )

    
    heatProfile = property(__heatProfile.value, __heatProfile.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatProbabilityProfile uses Python identifier heatProbabilityProfile
    __heatProbabilityProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatProbabilityProfile'), 'heatProbabilityProfile', '__httpwww_flexiblepower_orgefi_2_ProfileContainer_httpwww_flexiblepower_orgefi_2heatProbabilityProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 303, 4), )

    
    heatProbabilityProfile = property(__heatProbabilityProfile.value, __heatProbabilityProfile.set, None, None)

    _ElementMap.update({
        __electricityProfile.name() : __electricityProfile,
        __electricityProbabilityProfile.name() : __electricityProbabilityProfile,
        __gasProfile.name() : __gasProfile,
        __gasProbabilityProfile.name() : __gasProbabilityProfile,
        __heatProfile.name() : __heatProfile,
        __heatProbabilityProfile.name() : __heatProbabilityProfile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProfileContainer = ProfileContainer
Namespace.addCategoryObject('typeBinding', 'ProfileContainer', ProfileContainer)


# Complex type {http://www.flexiblepower.org/efi-2}CurtailmentProfileElement with content type EMPTY
class CurtailmentProfileElement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}CurtailmentProfileElement with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurtailmentProfileElement')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 336, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_CurtailmentProfileElement_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 337, 2)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 337, 2)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_flexiblepower_orgefi_2_CurtailmentProfileElement_httpwww_flexiblepower_orgefi_2value', pyxb.binding.datatypes.double, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 338, 2)
    __value._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 338, 2)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration,
        __value.name() : __value
    })
_module_typeBindings.CurtailmentProfileElement = CurtailmentProfileElement
Namespace.addCategoryObject('typeBinding', 'CurtailmentProfileElement', CurtailmentProfileElement)


# Complex type {http://www.flexiblepower.org/efi-2}SequentialProfile with content type ELEMENT_ONLY
class SequentialProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}SequentialProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequentialProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 351, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}maxIntervalBefore uses Python identifier maxIntervalBefore
    __maxIntervalBefore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxIntervalBefore'), 'maxIntervalBefore', '__httpwww_flexiblepower_orgefi_2_SequentialProfile_httpwww_flexiblepower_orgefi_2maxIntervalBefore', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 353, 3), )

    
    maxIntervalBefore = property(__maxIntervalBefore.value, __maxIntervalBefore.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}sequentialProfileAlternatives uses Python identifier sequentialProfileAlternatives
    __sequentialProfileAlternatives = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileAlternatives'), 'sequentialProfileAlternatives', '__httpwww_flexiblepower_orgefi_2_SequentialProfile_httpwww_flexiblepower_orgefi_2sequentialProfileAlternatives', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 354, 3), )

    
    sequentialProfileAlternatives = property(__sequentialProfileAlternatives.value, __sequentialProfileAlternatives.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}sequenceNr uses Python identifier sequenceNr
    __sequenceNr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'sequenceNr'), 'sequenceNr', '__httpwww_flexiblepower_orgefi_2_SequentialProfile_httpwww_flexiblepower_orgefi_2sequenceNr', pyxb.binding.datatypes.int, required=True)
    __sequenceNr._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 356, 2)
    __sequenceNr._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 356, 2)
    
    sequenceNr = property(__sequenceNr.value, __sequenceNr.set, None, None)

    _ElementMap.update({
        __maxIntervalBefore.name() : __maxIntervalBefore,
        __sequentialProfileAlternatives.name() : __sequentialProfileAlternatives
    })
    _AttributeMap.update({
        __sequenceNr.name() : __sequenceNr
    })
_module_typeBindings.SequentialProfile = SequentialProfile
Namespace.addCategoryObject('typeBinding', 'SequentialProfile', SequentialProfile)


# Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileAlternatives with content type ELEMENT_ONLY
class SequentialProfileAlternatives (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileAlternatives with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequentialProfileAlternatives')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 365, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}sequentialProfileAlternative uses Python identifier sequentialProfileAlternative
    __sequentialProfileAlternative = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileAlternative'), 'sequentialProfileAlternative', '__httpwww_flexiblepower_orgefi_2_SequentialProfileAlternatives_httpwww_flexiblepower_orgefi_2sequentialProfileAlternative', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 367, 3), )

    
    sequentialProfileAlternative = property(__sequentialProfileAlternative.value, __sequentialProfileAlternative.set, None, None)

    _ElementMap.update({
        __sequentialProfileAlternative.name() : __sequentialProfileAlternative
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SequentialProfileAlternatives = SequentialProfileAlternatives
Namespace.addCategoryObject('typeBinding', 'SequentialProfileAlternatives', SequentialProfileAlternatives)


# Complex type {http://www.flexiblepower.org/efi-2}SequentialProfiles with content type ELEMENT_ONLY
class SequentialProfiles (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}SequentialProfiles with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequentialProfiles')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 370, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}sequentialProfile uses Python identifier sequentialProfile
    __sequentialProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfile'), 'sequentialProfile', '__httpwww_flexiblepower_orgefi_2_SequentialProfiles_httpwww_flexiblepower_orgefi_2sequentialProfile', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 372, 3), )

    
    sequentialProfile = property(__sequentialProfile.value, __sequentialProfile.set, None, None)

    _ElementMap.update({
        __sequentialProfile.name() : __sequentialProfile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SequentialProfiles = SequentialProfiles
Namespace.addCategoryObject('typeBinding', 'SequentialProfiles', SequentialProfiles)


# Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileInstruction with content type ELEMENT_ONLY
class SequentialProfileInstruction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileInstruction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequentialProfileInstruction')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 387, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}sequenceNr uses Python identifier sequenceNr
    __sequenceNr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequenceNr'), 'sequenceNr', '__httpwww_flexiblepower_orgefi_2_SequentialProfileInstruction_httpwww_flexiblepower_orgefi_2sequenceNr', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 389, 3), )

    
    sequenceNr = property(__sequenceNr.value, __sequenceNr.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}alternativeNr uses Python identifier alternativeNr
    __alternativeNr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alternativeNr'), 'alternativeNr', '__httpwww_flexiblepower_orgefi_2_SequentialProfileInstruction_httpwww_flexiblepower_orgefi_2alternativeNr', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 390, 3), )

    
    alternativeNr = property(__alternativeNr.value, __alternativeNr.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startTime'), 'startTime', '__httpwww_flexiblepower_orgefi_2_SequentialProfileInstruction_httpwww_flexiblepower_orgefi_2startTime', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 391, 3), )

    
    startTime = property(__startTime.value, __startTime.set, None, None)

    _ElementMap.update({
        __sequenceNr.name() : __sequenceNr,
        __alternativeNr.name() : __alternativeNr,
        __startTime.name() : __startTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SequentialProfileInstruction = SequentialProfileInstruction
Namespace.addCategoryObject('typeBinding', 'SequentialProfileInstruction', SequentialProfileInstruction)


# Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileInstructions with content type ELEMENT_ONLY
class SequentialProfileInstructions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileInstructions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequentialProfileInstructions')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 394, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}sequentialProfileInstruction uses Python identifier sequentialProfileInstruction
    __sequentialProfileInstruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileInstruction'), 'sequentialProfileInstruction', '__httpwww_flexiblepower_orgefi_2_SequentialProfileInstructions_httpwww_flexiblepower_orgefi_2sequentialProfileInstruction', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 396, 3), )

    
    sequentialProfileInstruction = property(__sequentialProfileInstruction.value, __sequentialProfileInstruction.set, None, None)

    _ElementMap.update({
        __sequentialProfileInstruction.name() : __sequentialProfileInstruction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SequentialProfileInstructions = SequentialProfileInstructions
Namespace.addCategoryObject('typeBinding', 'SequentialProfileInstructions', SequentialProfileInstructions)


# Complex type {http://www.flexiblepower.org/efi-2}Actuator with content type ELEMENT_ONLY
class Actuator (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}Actuator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Actuator')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 423, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}supportedCommodity uses Python identifier supportedCommodity
    __supportedCommodity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodity'), 'supportedCommodity', '__httpwww_flexiblepower_orgefi_2_Actuator_httpwww_flexiblepower_orgefi_2supportedCommodity', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 425, 3), )

    
    supportedCommodity = property(__supportedCommodity.value, __supportedCommodity.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpwww_flexiblepower_orgefi_2_Actuator_httpwww_flexiblepower_orgefi_2id', pyxb.binding.datatypes.int, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 427, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 427, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__httpwww_flexiblepower_orgefi_2_Actuator_httpwww_flexiblepower_orgefi_2label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 428, 2)
    __label._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 428, 2)
    
    label = property(__label.value, __label.set, None, None)

    _ElementMap.update({
        __supportedCommodity.name() : __supportedCommodity
    })
    _AttributeMap.update({
        __id.name() : __id,
        __label.name() : __label
    })
_module_typeBindings.Actuator = Actuator
Namespace.addCategoryObject('typeBinding', 'Actuator', Actuator)


# Complex type {http://www.flexiblepower.org/efi-2}Actuators with content type ELEMENT_ONLY
class Actuators (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}Actuators with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Actuators')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 430, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}actuator uses Python identifier actuator
    __actuator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuator'), 'actuator', '__httpwww_flexiblepower_orgefi_2_Actuators_httpwww_flexiblepower_orgefi_2actuator', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 432, 3), )

    
    actuator = property(__actuator.value, __actuator.set, None, None)

    _ElementMap.update({
        __actuator.name() : __actuator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Actuators = Actuators
Namespace.addCategoryObject('typeBinding', 'Actuators', Actuators)


# Complex type {http://www.flexiblepower.org/efi-2}Timer with content type EMPTY
class Timer (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}Timer with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Timer')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 435, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpwww_flexiblepower_orgefi_2_Timer_httpwww_flexiblepower_orgefi_2id', pyxb.binding.datatypes.int, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 436, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 436, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__httpwww_flexiblepower_orgefi_2_Timer_httpwww_flexiblepower_orgefi_2label', pyxb.binding.datatypes.string, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 437, 2)
    __label._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 437, 2)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_Timer_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 438, 2)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 438, 2)
    
    duration = property(__duration.value, __duration.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __label.name() : __label,
        __duration.name() : __duration
    })
_module_typeBindings.Timer = Timer
Namespace.addCategoryObject('typeBinding', 'Timer', Timer)


# Complex type {http://www.flexiblepower.org/efi-2}Timers with content type ELEMENT_ONLY
class Timers (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}Timers with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Timers')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 440, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}timer uses Python identifier timer
    __timer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timer'), 'timer', '__httpwww_flexiblepower_orgefi_2_Timers_httpwww_flexiblepower_orgefi_2timer', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 442, 3), )

    
    timer = property(__timer.value, __timer.set, None, None)

    _ElementMap.update({
        __timer.name() : __timer
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Timers = Timers
Namespace.addCategoryObject('typeBinding', 'Timers', Timers)


# Complex type {http://www.flexiblepower.org/efi-2}Transitions with content type ELEMENT_ONLY
class Transitions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}Transitions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Transitions')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 445, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}transition uses Python identifier transition
    __transition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transition'), 'transition', '__httpwww_flexiblepower_orgefi_2_Transitions_httpwww_flexiblepower_orgefi_2transition', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 447, 3), )

    
    transition = property(__transition.value, __transition.set, None, None)

    _ElementMap.update({
        __transition.name() : __transition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Transitions = Transitions
Namespace.addCategoryObject('typeBinding', 'Transitions', Transitions)


# Complex type {http://www.flexiblepower.org/efi-2}TimerReferences with content type ELEMENT_ONLY
class TimerReferences (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}TimerReferences with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimerReferences')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 450, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}timerReference uses Python identifier timerReference
    __timerReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timerReference'), 'timerReference', '__httpwww_flexiblepower_orgefi_2_TimerReferences_httpwww_flexiblepower_orgefi_2timerReference', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 452, 3), )

    
    timerReference = property(__timerReference.value, __timerReference.set, None, None)

    _ElementMap.update({
        __timerReference.name() : __timerReference
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimerReferences = TimerReferences
Namespace.addCategoryObject('typeBinding', 'TimerReferences', TimerReferences)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 453, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}timerId uses Python identifier timerId
    __timerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'timerId'), 'timerId', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_9_httpwww_flexiblepower_orgefi_2timerId', pyxb.binding.datatypes.int, required=True)
    __timerId._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 454, 5)
    __timerId._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 454, 5)
    
    timerId = property(__timerId.value, __timerId.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __timerId.name() : __timerId
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {http://www.flexiblepower.org/efi-2}Transition with content type ELEMENT_ONLY
class Transition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}Transition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Transition')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 459, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}startTimers uses Python identifier startTimers
    __startTimers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startTimers'), 'startTimers', '__httpwww_flexiblepower_orgefi_2_Transition_httpwww_flexiblepower_orgefi_2startTimers', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 461, 3), )

    
    startTimers = property(__startTimers.value, __startTimers.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}blockingTimers uses Python identifier blockingTimers
    __blockingTimers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockingTimers'), 'blockingTimers', '__httpwww_flexiblepower_orgefi_2_Transition_httpwww_flexiblepower_orgefi_2blockingTimers', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 462, 3), )

    
    blockingTimers = property(__blockingTimers.value, __blockingTimers.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}fromRunningModeId uses Python identifier fromRunningModeId
    __fromRunningModeId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'fromRunningModeId'), 'fromRunningModeId', '__httpwww_flexiblepower_orgefi_2_Transition_httpwww_flexiblepower_orgefi_2fromRunningModeId', pyxb.binding.datatypes.int, required=True)
    __fromRunningModeId._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 464, 2)
    __fromRunningModeId._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 464, 2)
    
    fromRunningModeId = property(__fromRunningModeId.value, __fromRunningModeId.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}toRunningModeId uses Python identifier toRunningModeId
    __toRunningModeId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'toRunningModeId'), 'toRunningModeId', '__httpwww_flexiblepower_orgefi_2_Transition_httpwww_flexiblepower_orgefi_2toRunningModeId', pyxb.binding.datatypes.int, required=True)
    __toRunningModeId._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 465, 2)
    __toRunningModeId._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 465, 2)
    
    toRunningModeId = property(__toRunningModeId.value, __toRunningModeId.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}transitionCost uses Python identifier transitionCost
    __transitionCost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'transitionCost'), 'transitionCost', '__httpwww_flexiblepower_orgefi_2_Transition_httpwww_flexiblepower_orgefi_2transitionCost', pyxb.binding.datatypes.double)
    __transitionCost._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 466, 2)
    __transitionCost._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 466, 2)
    
    transitionCost = property(__transitionCost.value, __transitionCost.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}transitionDuration uses Python identifier transitionDuration
    __transitionDuration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'transitionDuration'), 'transitionDuration', '__httpwww_flexiblepower_orgefi_2_Transition_httpwww_flexiblepower_orgefi_2transitionDuration', pyxb.binding.datatypes.duration)
    __transitionDuration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 467, 2)
    __transitionDuration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 467, 2)
    
    transitionDuration = property(__transitionDuration.value, __transitionDuration.set, None, None)

    _ElementMap.update({
        __startTimers.name() : __startTimers,
        __blockingTimers.name() : __blockingTimers
    })
    _AttributeMap.update({
        __fromRunningModeId.name() : __fromRunningModeId,
        __toRunningModeId.name() : __toRunningModeId,
        __transitionCost.name() : __transitionCost,
        __transitionDuration.name() : __transitionDuration
    })
_module_typeBindings.Transition = Transition
Namespace.addCategoryObject('typeBinding', 'Transition', Transition)


# Complex type {http://www.flexiblepower.org/efi-2}RunningMode with content type EMPTY
class RunningMode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}RunningMode with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunningMode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 573, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpwww_flexiblepower_orgefi_2_RunningMode_httpwww_flexiblepower_orgefi_2id', pyxb.binding.datatypes.int, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 574, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 574, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__httpwww_flexiblepower_orgefi_2_RunningMode_httpwww_flexiblepower_orgefi_2label', pyxb.binding.datatypes.string, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 575, 2)
    __label._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 575, 2)
    
    label = property(__label.value, __label.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __label.name() : __label
    })
_module_typeBindings.RunningMode = RunningMode
Namespace.addCategoryObject('typeBinding', 'RunningMode', RunningMode)


# Complex type {http://www.flexiblepower.org/efi-2}StorageRunningModeElement with content type EMPTY
class StorageRunningModeElement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageRunningModeElement with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageRunningModeElement')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 577, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}fillLevelLowerBound uses Python identifier fillLevelLowerBound
    __fillLevelLowerBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'fillLevelLowerBound'), 'fillLevelLowerBound', '__httpwww_flexiblepower_orgefi_2_StorageRunningModeElement_httpwww_flexiblepower_orgefi_2fillLevelLowerBound', pyxb.binding.datatypes.double, required=True)
    __fillLevelLowerBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 578, 2)
    __fillLevelLowerBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 578, 2)
    
    fillLevelLowerBound = property(__fillLevelLowerBound.value, __fillLevelLowerBound.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}fillLevelUpperBound uses Python identifier fillLevelUpperBound
    __fillLevelUpperBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'fillLevelUpperBound'), 'fillLevelUpperBound', '__httpwww_flexiblepower_orgefi_2_StorageRunningModeElement_httpwww_flexiblepower_orgefi_2fillLevelUpperBound', pyxb.binding.datatypes.double, required=True)
    __fillLevelUpperBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 579, 2)
    __fillLevelUpperBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 579, 2)
    
    fillLevelUpperBound = property(__fillLevelUpperBound.value, __fillLevelUpperBound.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fillLevelLowerBound.name() : __fillLevelLowerBound,
        __fillLevelUpperBound.name() : __fillLevelUpperBound
    })
_module_typeBindings.StorageRunningModeElement = StorageRunningModeElement
Namespace.addCategoryObject('typeBinding', 'StorageRunningModeElement', StorageRunningModeElement)


# Complex type {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData with content type ELEMENT_ONLY
class StorageContinuousRunningModeData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageContinuousRunningModeData')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 606, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}fillingRate uses Python identifier fillingRate
    __fillingRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fillingRate'), 'fillingRate', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningModeData_httpwww_flexiblepower_orgefi_2fillingRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 608, 3), )

    
    fillingRate = property(__fillingRate.value, __fillingRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}runningCost uses Python identifier runningCost
    __runningCost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), 'runningCost', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningModeData_httpwww_flexiblepower_orgefi_2runningCost', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3), )

    
    runningCost = property(__runningCost.value, __runningCost.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}electricalPower uses Python identifier electricalPower
    __electricalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), 'electricalPower', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningModeData_httpwww_flexiblepower_orgefi_2electricalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3), )

    
    electricalPower = property(__electricalPower.value, __electricalPower.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}gasFlowRate uses Python identifier gasFlowRate
    __gasFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), 'gasFlowRate', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningModeData_httpwww_flexiblepower_orgefi_2gasFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3), )

    
    gasFlowRate = property(__gasFlowRate.value, __gasFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatTemperature uses Python identifier heatTemperature
    __heatTemperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), 'heatTemperature', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningModeData_httpwww_flexiblepower_orgefi_2heatTemperature', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3), )

    
    heatTemperature = property(__heatTemperature.value, __heatTemperature.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatFlowRate uses Python identifier heatFlowRate
    __heatFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), 'heatFlowRate', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningModeData_httpwww_flexiblepower_orgefi_2heatFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3), )

    
    heatFlowRate = property(__heatFlowRate.value, __heatFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatThermalPower uses Python identifier heatThermalPower
    __heatThermalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), 'heatThermalPower', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningModeData_httpwww_flexiblepower_orgefi_2heatThermalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3), )

    
    heatThermalPower = property(__heatThermalPower.value, __heatThermalPower.set, None, None)

    _ElementMap.update({
        __fillingRate.name() : __fillingRate,
        __runningCost.name() : __runningCost,
        __electricalPower.name() : __electricalPower,
        __gasFlowRate.name() : __gasFlowRate,
        __heatTemperature.name() : __heatTemperature,
        __heatFlowRate.name() : __heatFlowRate,
        __heatThermalPower.name() : __heatThermalPower
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StorageContinuousRunningModeData = StorageContinuousRunningModeData
Namespace.addCategoryObject('typeBinding', 'StorageContinuousRunningModeData', StorageContinuousRunningModeData)


# Complex type {http://www.flexiblepower.org/efi-2}StorageRunningModes with content type ELEMENT_ONLY
class StorageRunningModes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageRunningModes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageRunningModes')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 649, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}discreteRunningMode uses Python identifier discreteRunningMode
    __discreteRunningMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningMode'), 'discreteRunningMode', '__httpwww_flexiblepower_orgefi_2_StorageRunningModes_httpwww_flexiblepower_orgefi_2discreteRunningMode', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 652, 4), )

    
    discreteRunningMode = property(__discreteRunningMode.value, __discreteRunningMode.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}continuousRunningMode uses Python identifier continuousRunningMode
    __continuousRunningMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningMode'), 'continuousRunningMode', '__httpwww_flexiblepower_orgefi_2_StorageRunningModes_httpwww_flexiblepower_orgefi_2continuousRunningMode', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 653, 4), )

    
    continuousRunningMode = property(__continuousRunningMode.value, __continuousRunningMode.set, None, None)

    _ElementMap.update({
        __discreteRunningMode.name() : __discreteRunningMode,
        __continuousRunningMode.name() : __continuousRunningMode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StorageRunningModes = StorageRunningModes
Namespace.addCategoryObject('typeBinding', 'StorageRunningModes', StorageRunningModes)


# Complex type {http://www.flexiblepower.org/efi-2}ActuatorBehaviour with content type ELEMENT_ONLY
class ActuatorBehaviour (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ActuatorBehaviour with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActuatorBehaviour')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 657, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}runningModes uses Python identifier runningModes
    __runningModes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModes'), 'runningModes', '__httpwww_flexiblepower_orgefi_2_ActuatorBehaviour_httpwww_flexiblepower_orgefi_2runningModes', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 659, 3), )

    
    runningModes = property(__runningModes.value, __runningModes.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}timers uses Python identifier timers
    __timers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timers'), 'timers', '__httpwww_flexiblepower_orgefi_2_ActuatorBehaviour_httpwww_flexiblepower_orgefi_2timers', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 660, 3), )

    
    timers = property(__timers.value, __timers.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}transitions uses Python identifier transitions
    __transitions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transitions'), 'transitions', '__httpwww_flexiblepower_orgefi_2_ActuatorBehaviour_httpwww_flexiblepower_orgefi_2transitions', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 661, 3), )

    
    transitions = property(__transitions.value, __transitions.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}actuatorId uses Python identifier actuatorId
    __actuatorId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'actuatorId'), 'actuatorId', '__httpwww_flexiblepower_orgefi_2_ActuatorBehaviour_httpwww_flexiblepower_orgefi_2actuatorId', pyxb.binding.datatypes.int, required=True)
    __actuatorId._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 663, 2)
    __actuatorId._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 663, 2)
    
    actuatorId = property(__actuatorId.value, __actuatorId.set, None, None)

    _ElementMap.update({
        __runningModes.name() : __runningModes,
        __timers.name() : __timers,
        __transitions.name() : __transitions
    })
    _AttributeMap.update({
        __actuatorId.name() : __actuatorId
    })
_module_typeBindings.ActuatorBehaviour = ActuatorBehaviour
Namespace.addCategoryObject('typeBinding', 'ActuatorBehaviour', ActuatorBehaviour)


# Complex type {http://www.flexiblepower.org/efi-2}LeakageElement with content type EMPTY
class LeakageElement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}LeakageElement with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LeakageElement')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 665, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}fillLevelLowerBound uses Python identifier fillLevelLowerBound
    __fillLevelLowerBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'fillLevelLowerBound'), 'fillLevelLowerBound', '__httpwww_flexiblepower_orgefi_2_LeakageElement_httpwww_flexiblepower_orgefi_2fillLevelLowerBound', pyxb.binding.datatypes.double, required=True)
    __fillLevelLowerBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 666, 2)
    __fillLevelLowerBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 666, 2)
    
    fillLevelLowerBound = property(__fillLevelLowerBound.value, __fillLevelLowerBound.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}fillLevelUpperBound uses Python identifier fillLevelUpperBound
    __fillLevelUpperBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'fillLevelUpperBound'), 'fillLevelUpperBound', '__httpwww_flexiblepower_orgefi_2_LeakageElement_httpwww_flexiblepower_orgefi_2fillLevelUpperBound', pyxb.binding.datatypes.double, required=True)
    __fillLevelUpperBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 667, 2)
    __fillLevelUpperBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 667, 2)
    
    fillLevelUpperBound = property(__fillLevelUpperBound.value, __fillLevelUpperBound.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}leakageRate uses Python identifier leakageRate
    __leakageRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'leakageRate'), 'leakageRate', '__httpwww_flexiblepower_orgefi_2_LeakageElement_httpwww_flexiblepower_orgefi_2leakageRate', pyxb.binding.datatypes.double, required=True)
    __leakageRate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 668, 2)
    __leakageRate._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 668, 2)
    
    leakageRate = property(__leakageRate.value, __leakageRate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fillLevelLowerBound.name() : __fillLevelLowerBound,
        __fillLevelUpperBound.name() : __fillLevelUpperBound,
        __leakageRate.name() : __leakageRate
    })
_module_typeBindings.LeakageElement = LeakageElement
Namespace.addCategoryObject('typeBinding', 'LeakageElement', LeakageElement)


# Complex type {http://www.flexiblepower.org/efi-2}LeakageFunction with content type ELEMENT_ONLY
class LeakageFunction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}LeakageFunction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LeakageFunction')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 670, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}leakageElement uses Python identifier leakageElement
    __leakageElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'leakageElement'), 'leakageElement', '__httpwww_flexiblepower_orgefi_2_LeakageFunction_httpwww_flexiblepower_orgefi_2leakageElement', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 672, 3), )

    
    leakageElement = property(__leakageElement.value, __leakageElement.set, None, None)

    _ElementMap.update({
        __leakageElement.name() : __leakageElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LeakageFunction = LeakageFunction
Namespace.addCategoryObject('typeBinding', 'LeakageFunction', LeakageFunction)


# Complex type {http://www.flexiblepower.org/efi-2}ActuatorBehaviours with content type ELEMENT_ONLY
class ActuatorBehaviours (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ActuatorBehaviours with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActuatorBehaviours')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 675, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}actuatorBehaviour uses Python identifier actuatorBehaviour
    __actuatorBehaviour = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuatorBehaviour'), 'actuatorBehaviour', '__httpwww_flexiblepower_orgefi_2_ActuatorBehaviours_httpwww_flexiblepower_orgefi_2actuatorBehaviour', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 677, 3), )

    
    actuatorBehaviour = property(__actuatorBehaviour.value, __actuatorBehaviour.set, None, None)

    _ElementMap.update({
        __actuatorBehaviour.name() : __actuatorBehaviour
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActuatorBehaviours = ActuatorBehaviours
Namespace.addCategoryObject('typeBinding', 'ActuatorBehaviours', ActuatorBehaviours)


# Complex type {http://www.flexiblepower.org/efi-2}TimerUpdate with content type ELEMENT_ONLY
class TimerUpdate (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}TimerUpdate with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimerUpdate')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 697, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}finishedAt uses Python identifier finishedAt
    __finishedAt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'finishedAt'), 'finishedAt', '__httpwww_flexiblepower_orgefi_2_TimerUpdate_httpwww_flexiblepower_orgefi_2finishedAt', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 699, 3), )

    
    finishedAt = property(__finishedAt.value, __finishedAt.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}timerId uses Python identifier timerId
    __timerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'timerId'), 'timerId', '__httpwww_flexiblepower_orgefi_2_TimerUpdate_httpwww_flexiblepower_orgefi_2timerId', pyxb.binding.datatypes.int, required=True)
    __timerId._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 701, 2)
    __timerId._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 701, 2)
    
    timerId = property(__timerId.value, __timerId.set, None, None)

    _ElementMap.update({
        __finishedAt.name() : __finishedAt
    })
    _AttributeMap.update({
        __timerId.name() : __timerId
    })
_module_typeBindings.TimerUpdate = TimerUpdate
Namespace.addCategoryObject('typeBinding', 'TimerUpdate', TimerUpdate)


# Complex type {http://www.flexiblepower.org/efi-2}TimerUpdates with content type ELEMENT_ONLY
class TimerUpdates (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}TimerUpdates with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimerUpdates')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 703, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}timerUpdate uses Python identifier timerUpdate
    __timerUpdate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timerUpdate'), 'timerUpdate', '__httpwww_flexiblepower_orgefi_2_TimerUpdates_httpwww_flexiblepower_orgefi_2timerUpdate', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 705, 3), )

    
    timerUpdate = property(__timerUpdate.value, __timerUpdate.set, None, None)

    _ElementMap.update({
        __timerUpdate.name() : __timerUpdate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimerUpdates = TimerUpdates
Namespace.addCategoryObject('typeBinding', 'TimerUpdates', TimerUpdates)


# Complex type {http://www.flexiblepower.org/efi-2}ActuatorStatus with content type ELEMENT_ONLY
class ActuatorStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ActuatorStatus with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActuatorStatus')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 708, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}currentRunningMode uses Python identifier currentRunningMode
    __currentRunningMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentRunningMode'), 'currentRunningMode', '__httpwww_flexiblepower_orgefi_2_ActuatorStatus_httpwww_flexiblepower_orgefi_2currentRunningMode', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 710, 3), )

    
    currentRunningMode = property(__currentRunningMode.value, __currentRunningMode.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}runningModeFactor uses Python identifier runningModeFactor
    __runningModeFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), 'runningModeFactor', '__httpwww_flexiblepower_orgefi_2_ActuatorStatus_httpwww_flexiblepower_orgefi_2runningModeFactor', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 711, 3), )

    
    runningModeFactor = property(__runningModeFactor.value, __runningModeFactor.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}previousRunningModeId uses Python identifier previousRunningModeId
    __previousRunningModeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'previousRunningModeId'), 'previousRunningModeId', '__httpwww_flexiblepower_orgefi_2_ActuatorStatus_httpwww_flexiblepower_orgefi_2previousRunningModeId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 719, 3), )

    
    previousRunningModeId = property(__previousRunningModeId.value, __previousRunningModeId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}transitionTimestamp uses Python identifier transitionTimestamp
    __transitionTimestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transitionTimestamp'), 'transitionTimestamp', '__httpwww_flexiblepower_orgefi_2_ActuatorStatus_httpwww_flexiblepower_orgefi_2transitionTimestamp', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 720, 3), )

    
    transitionTimestamp = property(__transitionTimestamp.value, __transitionTimestamp.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}timerUpdates uses Python identifier timerUpdates
    __timerUpdates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timerUpdates'), 'timerUpdates', '__httpwww_flexiblepower_orgefi_2_ActuatorStatus_httpwww_flexiblepower_orgefi_2timerUpdates', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 721, 3), )

    
    timerUpdates = property(__timerUpdates.value, __timerUpdates.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}actuatorId uses Python identifier actuatorId
    __actuatorId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'actuatorId'), 'actuatorId', '__httpwww_flexiblepower_orgefi_2_ActuatorStatus_httpwww_flexiblepower_orgefi_2actuatorId', pyxb.binding.datatypes.int, required=True)
    __actuatorId._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 723, 2)
    __actuatorId._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 723, 2)
    
    actuatorId = property(__actuatorId.value, __actuatorId.set, None, None)

    _ElementMap.update({
        __currentRunningMode.name() : __currentRunningMode,
        __runningModeFactor.name() : __runningModeFactor,
        __previousRunningModeId.name() : __previousRunningModeId,
        __transitionTimestamp.name() : __transitionTimestamp,
        __timerUpdates.name() : __timerUpdates
    })
    _AttributeMap.update({
        __actuatorId.name() : __actuatorId
    })
_module_typeBindings.ActuatorStatus = ActuatorStatus
Namespace.addCategoryObject('typeBinding', 'ActuatorStatus', ActuatorStatus)


# Complex type {http://www.flexiblepower.org/efi-2}ActuatorStatuses with content type ELEMENT_ONLY
class ActuatorStatuses (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ActuatorStatuses with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActuatorStatuses')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 725, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}actuatorStatus uses Python identifier actuatorStatus
    __actuatorStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuatorStatus'), 'actuatorStatus', '__httpwww_flexiblepower_orgefi_2_ActuatorStatuses_httpwww_flexiblepower_orgefi_2actuatorStatus', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 727, 3), )

    
    actuatorStatus = property(__actuatorStatus.value, __actuatorStatus.set, None, None)

    _ElementMap.update({
        __actuatorStatus.name() : __actuatorStatus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActuatorStatuses = ActuatorStatuses
Namespace.addCategoryObject('typeBinding', 'ActuatorStatuses', ActuatorStatuses)


# Complex type {http://www.flexiblepower.org/efi-2}TargetProfile with content type ELEMENT_ONLY
class TargetProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}TargetProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 742, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'element'), 'element', '__httpwww_flexiblepower_orgefi_2_TargetProfile_httpwww_flexiblepower_orgefi_2element', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 744, 3), )

    
    element = property(__element.value, __element.set, None, None)

    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TargetProfile = TargetProfile
Namespace.addCategoryObject('typeBinding', 'TargetProfile', TargetProfile)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 745, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_10_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 746, 5)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 746, 5)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}fillLevelLowerBound uses Python identifier fillLevelLowerBound
    __fillLevelLowerBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'fillLevelLowerBound'), 'fillLevelLowerBound', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_10_httpwww_flexiblepower_orgefi_2fillLevelLowerBound', pyxb.binding.datatypes.double, required=True)
    __fillLevelLowerBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 747, 5)
    __fillLevelLowerBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 747, 5)
    
    fillLevelLowerBound = property(__fillLevelLowerBound.value, __fillLevelLowerBound.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}fillLevelUpperBound uses Python identifier fillLevelUpperBound
    __fillLevelUpperBound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'fillLevelUpperBound'), 'fillLevelUpperBound', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_10_httpwww_flexiblepower_orgefi_2fillLevelUpperBound', pyxb.binding.datatypes.double, required=True)
    __fillLevelUpperBound._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 748, 5)
    __fillLevelUpperBound._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 748, 5)
    
    fillLevelUpperBound = property(__fillLevelUpperBound.value, __fillLevelUpperBound.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration,
        __fillLevelLowerBound.name() : __fillLevelLowerBound,
        __fillLevelUpperBound.name() : __fillLevelUpperBound
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 770, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}usageProfile uses Python identifier usageProfile
    __usageProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usageProfile'), 'usageProfile', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_11_httpwww_flexiblepower_orgefi_2usageProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 772, 9), )

    
    usageProfile = property(__usageProfile.value, __usageProfile.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}usageProbabilityProfile uses Python identifier usageProbabilityProfile
    __usageProbabilityProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usageProbabilityProfile'), 'usageProbabilityProfile', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_11_httpwww_flexiblepower_orgefi_2usageProbabilityProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 773, 9), )

    
    usageProbabilityProfile = property(__usageProbabilityProfile.value, __usageProbabilityProfile.set, None, None)

    _ElementMap.update({
        __usageProfile.name() : __usageProfile,
        __usageProbabilityProfile.name() : __usageProbabilityProfile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type {http://www.flexiblepower.org/efi-2}ActuatorInstruction with content type ELEMENT_ONLY
class ActuatorInstruction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ActuatorInstruction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActuatorInstruction')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 782, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}runningModeId uses Python identifier runningModeId
    __runningModeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModeId'), 'runningModeId', '__httpwww_flexiblepower_orgefi_2_ActuatorInstruction_httpwww_flexiblepower_orgefi_2runningModeId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 784, 3), )

    
    runningModeId = property(__runningModeId.value, __runningModeId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}runningModeFactor uses Python identifier runningModeFactor
    __runningModeFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), 'runningModeFactor', '__httpwww_flexiblepower_orgefi_2_ActuatorInstruction_httpwww_flexiblepower_orgefi_2runningModeFactor', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 785, 3), )

    
    runningModeFactor = property(__runningModeFactor.value, __runningModeFactor.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startTime'), 'startTime', '__httpwww_flexiblepower_orgefi_2_ActuatorInstruction_httpwww_flexiblepower_orgefi_2startTime', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 793, 3), )

    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}actuatorId uses Python identifier actuatorId
    __actuatorId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'actuatorId'), 'actuatorId', '__httpwww_flexiblepower_orgefi_2_ActuatorInstruction_httpwww_flexiblepower_orgefi_2actuatorId', pyxb.binding.datatypes.int, required=True)
    __actuatorId._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 795, 2)
    __actuatorId._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 795, 2)
    
    actuatorId = property(__actuatorId.value, __actuatorId.set, None, None)

    _ElementMap.update({
        __runningModeId.name() : __runningModeId,
        __runningModeFactor.name() : __runningModeFactor,
        __startTime.name() : __startTime
    })
    _AttributeMap.update({
        __actuatorId.name() : __actuatorId
    })
_module_typeBindings.ActuatorInstruction = ActuatorInstruction
Namespace.addCategoryObject('typeBinding', 'ActuatorInstruction', ActuatorInstruction)


# Complex type {http://www.flexiblepower.org/efi-2}ActuatorInstructions with content type ELEMENT_ONLY
class ActuatorInstructions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}ActuatorInstructions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActuatorInstructions')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 797, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}actuatorInstruction uses Python identifier actuatorInstruction
    __actuatorInstruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuatorInstruction'), 'actuatorInstruction', '__httpwww_flexiblepower_orgefi_2_ActuatorInstructions_httpwww_flexiblepower_orgefi_2actuatorInstruction', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 799, 3), )

    
    actuatorInstruction = property(__actuatorInstruction.value, __actuatorInstruction.set, None, None)

    _ElementMap.update({
        __actuatorInstruction.name() : __actuatorInstruction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActuatorInstructions = ActuatorInstructions
Namespace.addCategoryObject('typeBinding', 'ActuatorInstructions', ActuatorInstructions)


# Complex type {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData with content type ELEMENT_ONLY
class AdjustableContinuousRunningModeData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdjustableContinuousRunningModeData')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 838, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}runningCost uses Python identifier runningCost
    __runningCost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), 'runningCost', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningModeData_httpwww_flexiblepower_orgefi_2runningCost', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3), )

    
    runningCost = property(__runningCost.value, __runningCost.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}electricalPower uses Python identifier electricalPower
    __electricalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), 'electricalPower', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningModeData_httpwww_flexiblepower_orgefi_2electricalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3), )

    
    electricalPower = property(__electricalPower.value, __electricalPower.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}gasFlowRate uses Python identifier gasFlowRate
    __gasFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), 'gasFlowRate', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningModeData_httpwww_flexiblepower_orgefi_2gasFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3), )

    
    gasFlowRate = property(__gasFlowRate.value, __gasFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatTemperature uses Python identifier heatTemperature
    __heatTemperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), 'heatTemperature', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningModeData_httpwww_flexiblepower_orgefi_2heatTemperature', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3), )

    
    heatTemperature = property(__heatTemperature.value, __heatTemperature.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatFlowRate uses Python identifier heatFlowRate
    __heatFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), 'heatFlowRate', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningModeData_httpwww_flexiblepower_orgefi_2heatFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3), )

    
    heatFlowRate = property(__heatFlowRate.value, __heatFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatThermalPower uses Python identifier heatThermalPower
    __heatThermalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), 'heatThermalPower', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningModeData_httpwww_flexiblepower_orgefi_2heatThermalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3), )

    
    heatThermalPower = property(__heatThermalPower.value, __heatThermalPower.set, None, None)

    _ElementMap.update({
        __runningCost.name() : __runningCost,
        __electricalPower.name() : __electricalPower,
        __gasFlowRate.name() : __gasFlowRate,
        __heatTemperature.name() : __heatTemperature,
        __heatFlowRate.name() : __heatFlowRate,
        __heatThermalPower.name() : __heatThermalPower
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdjustableContinuousRunningModeData = AdjustableContinuousRunningModeData
Namespace.addCategoryObject('typeBinding', 'AdjustableContinuousRunningModeData', AdjustableContinuousRunningModeData)


# Complex type {http://www.flexiblepower.org/efi-2}AdjustableRunningModes with content type ELEMENT_ONLY
class AdjustableRunningModes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}AdjustableRunningModes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdjustableRunningModes')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 870, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}discreteRunningMode uses Python identifier discreteRunningMode
    __discreteRunningMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningMode'), 'discreteRunningMode', '__httpwww_flexiblepower_orgefi_2_AdjustableRunningModes_httpwww_flexiblepower_orgefi_2discreteRunningMode', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 873, 4), )

    
    discreteRunningMode = property(__discreteRunningMode.value, __discreteRunningMode.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}continuousRunningMode uses Python identifier continuousRunningMode
    __continuousRunningMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningMode'), 'continuousRunningMode', '__httpwww_flexiblepower_orgefi_2_AdjustableRunningModes_httpwww_flexiblepower_orgefi_2continuousRunningMode', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 874, 4), )

    
    continuousRunningMode = property(__continuousRunningMode.value, __continuousRunningMode.set, None, None)

    _ElementMap.update({
        __discreteRunningMode.name() : __discreteRunningMode,
        __continuousRunningMode.name() : __continuousRunningMode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdjustableRunningModes = AdjustableRunningModes
Namespace.addCategoryObject('typeBinding', 'AdjustableRunningModes', AdjustableRunningModes)


# Complex type {http://www.flexiblepower.org/efi-2}FlexibilityRegistration with content type ELEMENT_ONLY
class FlexibilityRegistration (EfiMessage):
    """Complex type {http://www.flexiblepower.org/efi-2}FlexibilityRegistration with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlexibilityRegistration')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 42, 1)
    _ElementMap = EfiMessage._ElementMap.copy()
    _AttributeMap = EfiMessage._AttributeMap.copy()
    # Base type is EfiMessage
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element {http://www.flexiblepower.org/efi-2}instructionProcessingDelay uses Python identifier instructionProcessingDelay
    __instructionProcessingDelay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instructionProcessingDelay'), 'instructionProcessingDelay', '__httpwww_flexiblepower_orgefi_2_FlexibilityRegistration_httpwww_flexiblepower_orgefi_2instructionProcessingDelay', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 46, 5), )

    
    instructionProcessingDelay = property(__instructionProcessingDelay.value, __instructionProcessingDelay.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}deviceDescription uses Python identifier deviceDescription
    __deviceDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deviceDescription'), 'deviceDescription', '__httpwww_flexiblepower_orgefi_2_FlexibilityRegistration_httpwww_flexiblepower_orgefi_2deviceDescription', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 47, 5), )

    
    deviceDescription = property(__deviceDescription.value, __deviceDescription.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__httpwww_flexiblepower_orgefi_2_FlexibilityRegistration_httpwww_flexiblepower_orgefi_2currency', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5), )

    
    currency = property(__currency.value, __currency.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __instructionProcessingDelay.name() : __instructionProcessingDelay,
        __deviceDescription.name() : __deviceDescription,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FlexibilityRegistration = FlexibilityRegistration
Namespace.addCategoryObject('typeBinding', 'FlexibilityRegistration', FlexibilityRegistration)


# Complex type {http://www.flexiblepower.org/efi-2}FlexibilityUpdate with content type ELEMENT_ONLY
class FlexibilityUpdate (EfiMessage):
    """Complex type {http://www.flexiblepower.org/efi-2}FlexibilityUpdate with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlexibilityUpdate')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 53, 1)
    _ElementMap = EfiMessage._ElementMap.copy()
    _AttributeMap = EfiMessage._AttributeMap.copy()
    # Base type is EfiMessage
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element {http://www.flexiblepower.org/efi-2}flexibilityUpdateId uses Python identifier flexibilityUpdateId
    __flexibilityUpdateId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId'), 'flexibilityUpdateId', '__httpwww_flexiblepower_orgefi_2_FlexibilityUpdate_httpwww_flexiblepower_orgefi_2flexibilityUpdateId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5), )

    
    flexibilityUpdateId = property(__flexibilityUpdateId.value, __flexibilityUpdateId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}validFrom uses Python identifier validFrom
    __validFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validFrom'), 'validFrom', '__httpwww_flexiblepower_orgefi_2_FlexibilityUpdate_httpwww_flexiblepower_orgefi_2validFrom', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5), )

    
    validFrom = property(__validFrom.value, __validFrom.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __flexibilityUpdateId.name() : __flexibilityUpdateId,
        __validFrom.name() : __validFrom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FlexibilityUpdate = FlexibilityUpdate
Namespace.addCategoryObject('typeBinding', 'FlexibilityUpdate', FlexibilityUpdate)


# Complex type {http://www.flexiblepower.org/efi-2}Instruction with content type ELEMENT_ONLY
class Instruction (EfiMessage):
    """Complex type {http://www.flexiblepower.org/efi-2}Instruction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Instruction')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 63, 1)
    _ElementMap = EfiMessage._ElementMap.copy()
    _AttributeMap = EfiMessage._AttributeMap.copy()
    # Base type is EfiMessage
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element {http://www.flexiblepower.org/efi-2}instructionId uses Python identifier instructionId
    __instructionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instructionId'), 'instructionId', '__httpwww_flexiblepower_orgefi_2_Instruction_httpwww_flexiblepower_orgefi_2instructionId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 67, 5), )

    
    instructionId = property(__instructionId.value, __instructionId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}flexibilityUpdateId uses Python identifier flexibilityUpdateId
    __flexibilityUpdateId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId'), 'flexibilityUpdateId', '__httpwww_flexiblepower_orgefi_2_Instruction_httpwww_flexiblepower_orgefi_2flexibilityUpdateId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 68, 5), )

    
    flexibilityUpdateId = property(__flexibilityUpdateId.value, __flexibilityUpdateId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}isEmergencyInstruction uses Python identifier isEmergencyInstruction
    __isEmergencyInstruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isEmergencyInstruction'), 'isEmergencyInstruction', '__httpwww_flexiblepower_orgefi_2_Instruction_httpwww_flexiblepower_orgefi_2isEmergencyInstruction', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 69, 5), )

    
    isEmergencyInstruction = property(__isEmergencyInstruction.value, __isEmergencyInstruction.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __instructionId.name() : __instructionId,
        __flexibilityUpdateId.name() : __flexibilityUpdateId,
        __isEmergencyInstruction.name() : __isEmergencyInstruction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Instruction = Instruction
Namespace.addCategoryObject('typeBinding', 'Instruction', Instruction)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (EfiMessage):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 75, 2)
    _ElementMap = EfiMessage._ElementMap.copy()
    _AttributeMap = EfiMessage._AttributeMap.copy()
    # Base type is EfiMessage
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element {http://www.flexiblepower.org/efi-2}instructionId uses Python identifier instructionId
    __instructionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instructionId'), 'instructionId', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_12_httpwww_flexiblepower_orgefi_2instructionId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 79, 6), )

    
    instructionId = property(__instructionId.value, __instructionId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_12_httpwww_flexiblepower_orgefi_2status', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 80, 6), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}debugInformation uses Python identifier debugInformation
    __debugInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'debugInformation'), 'debugInformation', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_12_httpwww_flexiblepower_orgefi_2debugInformation', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 81, 6), )

    
    debugInformation = property(__debugInformation.value, __debugInformation.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __instructionId.name() : __instructionId,
        __status.name() : __status,
        __debugInformation.name() : __debugInformation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (EfiMessage):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 97, 2)
    _ElementMap = EfiMessage._ElementMap.copy()
    _AttributeMap = EfiMessage._AttributeMap.copy()
    # Base type is EfiMessage
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (EfiMessage):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 104, 2)
    _ElementMap = EfiMessage._ElementMap.copy()
    _AttributeMap = EfiMessage._AttributeMap.copy()
    # Base type is EfiMessage
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element {http://www.flexiblepower.org/efi-2}instructionId uses Python identifier instructionId
    __instructionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instructionId'), 'instructionId', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_14_httpwww_flexiblepower_orgefi_2instructionId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 108, 6), )

    
    instructionId = property(__instructionId.value, __instructionId.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __instructionId.name() : __instructionId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type {http://www.flexiblepower.org/efi-2}ProbabilityAttributesWithDuration with content type EMPTY
class ProbabilityAttributesWithDuration (ProbabilityAttributes):
    """Complex type {http://www.flexiblepower.org/efi-2}ProbabilityAttributesWithDuration with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProbabilityAttributesWithDuration')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 137, 1)
    _ElementMap = ProbabilityAttributes._ElementMap.copy()
    _AttributeMap = ProbabilityAttributes._AttributeMap.copy()
    # Base type is ProbabilityAttributes
    
    # Attribute the68PPRLower inherited from {http://www.flexiblepower.org/efi-2}ProbabilityAttributes
    
    # Attribute the95PPRLower inherited from {http://www.flexiblepower.org/efi-2}ProbabilityAttributes
    
    # Attribute expected inherited from {http://www.flexiblepower.org/efi-2}ProbabilityAttributes
    
    # Attribute the95PPRUpper inherited from {http://www.flexiblepower.org/efi-2}ProbabilityAttributes
    
    # Attribute the68PPRUpper inherited from {http://www.flexiblepower.org/efi-2}ProbabilityAttributes
    
    # Attribute {http://www.flexiblepower.org/efi-2}duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__httpwww_flexiblepower_orgefi_2_ProbabilityAttributesWithDuration_httpwww_flexiblepower_orgefi_2duration', pyxb.binding.datatypes.duration, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 140, 4)
    __duration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 140, 4)
    
    duration = property(__duration.value, __duration.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration
    })
_module_typeBindings.ProbabilityAttributesWithDuration = ProbabilityAttributesWithDuration
Namespace.addCategoryObject('typeBinding', 'ProbabilityAttributesWithDuration', ProbabilityAttributesWithDuration)


# Complex type {http://www.flexiblepower.org/efi-2}CurtailmentOption with content type ELEMENT_ONLY
class CurtailmentOption (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}CurtailmentOption with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurtailmentOption')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 236, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}curtailmentRange uses Python identifier curtailmentRange
    __curtailmentRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'curtailmentRange'), 'curtailmentRange', '__httpwww_flexiblepower_orgefi_2_CurtailmentOption_httpwww_flexiblepower_orgefi_2curtailmentRange', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 238, 3), )

    
    curtailmentRange = property(__curtailmentRange.value, __curtailmentRange.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}curtailmentQuantity uses Python identifier curtailmentQuantity
    __curtailmentQuantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'curtailmentQuantity'), 'curtailmentQuantity', '__httpwww_flexiblepower_orgefi_2_CurtailmentOption_httpwww_flexiblepower_orgefi_2curtailmentQuantity', _module_typeBindings.CurtailmentQuantity, required=True)
    __curtailmentQuantity._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 240, 2)
    __curtailmentQuantity._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 240, 2)
    
    curtailmentQuantity = property(__curtailmentQuantity.value, __curtailmentQuantity.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}minimalCurtailmentDuration uses Python identifier minimalCurtailmentDuration
    __minimalCurtailmentDuration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'minimalCurtailmentDuration'), 'minimalCurtailmentDuration', '__httpwww_flexiblepower_orgefi_2_CurtailmentOption_httpwww_flexiblepower_orgefi_2minimalCurtailmentDuration', pyxb.binding.datatypes.duration, unicode_default='PT0S')
    __minimalCurtailmentDuration._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 241, 2)
    __minimalCurtailmentDuration._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 241, 2)
    
    minimalCurtailmentDuration = property(__minimalCurtailmentDuration.value, __minimalCurtailmentDuration.set, None, None)

    _ElementMap.update({
        __curtailmentRange.name() : __curtailmentRange
    })
    _AttributeMap.update({
        __curtailmentQuantity.name() : __curtailmentQuantity,
        __minimalCurtailmentDuration.name() : __minimalCurtailmentDuration
    })
_module_typeBindings.CurtailmentOption = CurtailmentOption
Namespace.addCategoryObject('typeBinding', 'CurtailmentOption', CurtailmentOption)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (EfiMessage):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 253, 2)
    _ElementMap = EfiMessage._ElementMap.copy()
    _AttributeMap = EfiMessage._AttributeMap.copy()
    # Base type is EfiMessage
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element {http://www.flexiblepower.org/efi-2}measurementTimestamp uses Python identifier measurementTimestamp
    __measurementTimestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measurementTimestamp'), 'measurementTimestamp', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_15_httpwww_flexiblepower_orgefi_2measurementTimestamp', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 257, 6), )

    
    measurementTimestamp = property(__measurementTimestamp.value, __measurementTimestamp.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}electricityMeasurement uses Python identifier electricityMeasurement
    __electricityMeasurement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electricityMeasurement'), 'electricityMeasurement', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_15_httpwww_flexiblepower_orgefi_2electricityMeasurement', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 258, 6), )

    
    electricityMeasurement = property(__electricityMeasurement.value, __electricityMeasurement.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}gasMeasurement uses Python identifier gasMeasurement
    __gasMeasurement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gasMeasurement'), 'gasMeasurement', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_15_httpwww_flexiblepower_orgefi_2gasMeasurement', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 263, 6), )

    
    gasMeasurement = property(__gasMeasurement.value, __gasMeasurement.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatMeasurement uses Python identifier heatMeasurement
    __heatMeasurement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatMeasurement'), 'heatMeasurement', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_15_httpwww_flexiblepower_orgefi_2heatMeasurement', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 268, 6), )

    
    heatMeasurement = property(__heatMeasurement.value, __heatMeasurement.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __measurementTimestamp.name() : __measurementTimestamp,
        __electricityMeasurement.name() : __electricityMeasurement,
        __gasMeasurement.name() : __gasMeasurement,
        __heatMeasurement.name() : __heatMeasurement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type {http://www.flexiblepower.org/efi-2}CurtailmentProfile with content type ELEMENT_ONLY
class CurtailmentProfile (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.flexiblepower.org/efi-2}CurtailmentProfile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurtailmentProfile')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 329, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.flexiblepower.org/efi-2}curtailmentProfileElement uses Python identifier curtailmentProfileElement
    __curtailmentProfileElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'curtailmentProfileElement'), 'curtailmentProfileElement', '__httpwww_flexiblepower_orgefi_2_CurtailmentProfile_httpwww_flexiblepower_orgefi_2curtailmentProfileElement', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 331, 3), )

    
    curtailmentProfileElement = property(__curtailmentProfileElement.value, __curtailmentProfileElement.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}curtailmentQuantity uses Python identifier curtailmentQuantity
    __curtailmentQuantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'curtailmentQuantity'), 'curtailmentQuantity', '__httpwww_flexiblepower_orgefi_2_CurtailmentProfile_httpwww_flexiblepower_orgefi_2curtailmentQuantity', _module_typeBindings.CurtailmentQuantity, required=True)
    __curtailmentQuantity._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 333, 2)
    __curtailmentQuantity._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 333, 2)
    
    curtailmentQuantity = property(__curtailmentQuantity.value, __curtailmentQuantity.set, None, None)

    
    # Attribute {http://www.flexiblepower.org/efi-2}startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'startTime'), 'startTime', '__httpwww_flexiblepower_orgefi_2_CurtailmentProfile_httpwww_flexiblepower_orgefi_2startTime', pyxb.binding.datatypes.dateTime, required=True)
    __startTime._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 334, 2)
    __startTime._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 334, 2)
    
    startTime = property(__startTime.value, __startTime.set, None, None)

    _ElementMap.update({
        __curtailmentProfileElement.name() : __curtailmentProfileElement
    })
    _AttributeMap.update({
        __curtailmentQuantity.name() : __curtailmentQuantity,
        __startTime.name() : __startTime
    })
_module_typeBindings.CurtailmentProfile = CurtailmentProfile
Namespace.addCategoryObject('typeBinding', 'CurtailmentProfile', CurtailmentProfile)


# Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileAlternative with content type ELEMENT_ONLY
class SequentialProfileAlternative (ProfileContainer):
    """Complex type {http://www.flexiblepower.org/efi-2}SequentialProfileAlternative with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequentialProfileAlternative')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 358, 1)
    _ElementMap = ProfileContainer._ElementMap.copy()
    _AttributeMap = ProfileContainer._AttributeMap.copy()
    # Base type is ProfileContainer
    
    # Element electricityProfile ({http://www.flexiblepower.org/efi-2}electricityProfile) inherited from {http://www.flexiblepower.org/efi-2}ProfileContainer
    
    # Element electricityProbabilityProfile ({http://www.flexiblepower.org/efi-2}electricityProbabilityProfile) inherited from {http://www.flexiblepower.org/efi-2}ProfileContainer
    
    # Element gasProfile ({http://www.flexiblepower.org/efi-2}gasProfile) inherited from {http://www.flexiblepower.org/efi-2}ProfileContainer
    
    # Element gasProbabilityProfile ({http://www.flexiblepower.org/efi-2}gasProbabilityProfile) inherited from {http://www.flexiblepower.org/efi-2}ProfileContainer
    
    # Element heatProfile ({http://www.flexiblepower.org/efi-2}heatProfile) inherited from {http://www.flexiblepower.org/efi-2}ProfileContainer
    
    # Element heatProbabilityProfile ({http://www.flexiblepower.org/efi-2}heatProbabilityProfile) inherited from {http://www.flexiblepower.org/efi-2}ProfileContainer
    
    # Attribute {http://www.flexiblepower.org/efi-2}alternativeNr uses Python identifier alternativeNr
    __alternativeNr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'alternativeNr'), 'alternativeNr', '__httpwww_flexiblepower_orgefi_2_SequentialProfileAlternative_httpwww_flexiblepower_orgefi_2alternativeNr', pyxb.binding.datatypes.int, required=True)
    __alternativeNr._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 361, 4)
    __alternativeNr._UseLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 361, 4)
    
    alternativeNr = property(__alternativeNr.value, __alternativeNr.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __alternativeNr.name() : __alternativeNr
    })
_module_typeBindings.SequentialProfileAlternative = SequentialProfileAlternative
Namespace.addCategoryObject('typeBinding', 'SequentialProfileAlternative', SequentialProfileAlternative)


# Complex type {http://www.flexiblepower.org/efi-2}StorageDiscreteRunningMode with content type ELEMENT_ONLY
class StorageDiscreteRunningMode (RunningMode):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageDiscreteRunningMode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageDiscreteRunningMode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 581, 1)
    _ElementMap = RunningMode._ElementMap.copy()
    _AttributeMap = RunningMode._AttributeMap.copy()
    # Base type is RunningMode
    
    # Element {http://www.flexiblepower.org/efi-2}discreteRunningModeElement uses Python identifier discreteRunningModeElement
    __discreteRunningModeElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningModeElement'), 'discreteRunningModeElement', '__httpwww_flexiblepower_orgefi_2_StorageDiscreteRunningMode_httpwww_flexiblepower_orgefi_2discreteRunningModeElement', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 585, 5), )

    
    discreteRunningModeElement = property(__discreteRunningModeElement.value, __discreteRunningModeElement.set, None, None)

    
    # Attribute id inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    
    # Attribute label inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    _ElementMap.update({
        __discreteRunningModeElement.name() : __discreteRunningModeElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StorageDiscreteRunningMode = StorageDiscreteRunningMode
Namespace.addCategoryObject('typeBinding', 'StorageDiscreteRunningMode', StorageDiscreteRunningMode)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (StorageRunningModeElement):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 586, 6)
    _ElementMap = StorageRunningModeElement._ElementMap.copy()
    _AttributeMap = StorageRunningModeElement._AttributeMap.copy()
    # Base type is StorageRunningModeElement
    
    # Element {http://www.flexiblepower.org/efi-2}fillingRate uses Python identifier fillingRate
    __fillingRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fillingRate'), 'fillingRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_16_httpwww_flexiblepower_orgefi_2fillingRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 590, 10), )

    
    fillingRate = property(__fillingRate.value, __fillingRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}runningCost uses Python identifier runningCost
    __runningCost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), 'runningCost', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_16_httpwww_flexiblepower_orgefi_2runningCost', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 591, 10), )

    
    runningCost = property(__runningCost.value, __runningCost.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}electricalPower uses Python identifier electricalPower
    __electricalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), 'electricalPower', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_16_httpwww_flexiblepower_orgefi_2electricalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 592, 10), )

    
    electricalPower = property(__electricalPower.value, __electricalPower.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}gasFlowRate uses Python identifier gasFlowRate
    __gasFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), 'gasFlowRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_16_httpwww_flexiblepower_orgefi_2gasFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 593, 10), )

    
    gasFlowRate = property(__gasFlowRate.value, __gasFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatTemperature uses Python identifier heatTemperature
    __heatTemperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), 'heatTemperature', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_16_httpwww_flexiblepower_orgefi_2heatTemperature', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 594, 10), )

    
    heatTemperature = property(__heatTemperature.value, __heatTemperature.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatFlowRate uses Python identifier heatFlowRate
    __heatFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), 'heatFlowRate', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_16_httpwww_flexiblepower_orgefi_2heatFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 595, 10), )

    
    heatFlowRate = property(__heatFlowRate.value, __heatFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatThermalPower uses Python identifier heatThermalPower
    __heatThermalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), 'heatThermalPower', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_16_httpwww_flexiblepower_orgefi_2heatThermalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 596, 10), )

    
    heatThermalPower = property(__heatThermalPower.value, __heatThermalPower.set, None, None)

    
    # Attribute fillLevelLowerBound inherited from {http://www.flexiblepower.org/efi-2}StorageRunningModeElement
    
    # Attribute fillLevelUpperBound inherited from {http://www.flexiblepower.org/efi-2}StorageRunningModeElement
    _ElementMap.update({
        __fillingRate.name() : __fillingRate,
        __runningCost.name() : __runningCost,
        __electricalPower.name() : __electricalPower,
        __gasFlowRate.name() : __gasFlowRate,
        __heatTemperature.name() : __heatTemperature,
        __heatFlowRate.name() : __heatFlowRate,
        __heatThermalPower.name() : __heatThermalPower
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type {http://www.flexiblepower.org/efi-2}StorageContinuousRunningMode with content type ELEMENT_ONLY
class StorageContinuousRunningMode (RunningMode):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageContinuousRunningMode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageContinuousRunningMode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 617, 1)
    _ElementMap = RunningMode._ElementMap.copy()
    _AttributeMap = RunningMode._AttributeMap.copy()
    # Base type is RunningMode
    
    # Element {http://www.flexiblepower.org/efi-2}continuousRunningModeElement uses Python identifier continuousRunningModeElement
    __continuousRunningModeElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningModeElement'), 'continuousRunningModeElement', '__httpwww_flexiblepower_orgefi_2_StorageContinuousRunningMode_httpwww_flexiblepower_orgefi_2continuousRunningModeElement', True, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 621, 5), )

    
    continuousRunningModeElement = property(__continuousRunningModeElement.value, __continuousRunningModeElement.set, None, None)

    
    # Attribute id inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    
    # Attribute label inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    _ElementMap.update({
        __continuousRunningModeElement.name() : __continuousRunningModeElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StorageContinuousRunningMode = StorageContinuousRunningMode
Namespace.addCategoryObject('typeBinding', 'StorageContinuousRunningMode', StorageContinuousRunningMode)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (StorageRunningModeElement):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 622, 6)
    _ElementMap = StorageRunningModeElement._ElementMap.copy()
    _AttributeMap = StorageRunningModeElement._AttributeMap.copy()
    # Base type is StorageRunningModeElement
    
    # Element {http://www.flexiblepower.org/efi-2}lowerBound uses Python identifier lowerBound
    __lowerBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lowerBound'), 'lowerBound', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_17_httpwww_flexiblepower_orgefi_2lowerBound', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 626, 10), )

    
    lowerBound = property(__lowerBound.value, __lowerBound.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}upperBound uses Python identifier upperBound
    __upperBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'upperBound'), 'upperBound', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_17_httpwww_flexiblepower_orgefi_2upperBound', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 633, 10), )

    
    upperBound = property(__upperBound.value, __upperBound.set, None, None)

    
    # Attribute fillLevelLowerBound inherited from {http://www.flexiblepower.org/efi-2}StorageRunningModeElement
    
    # Attribute fillLevelUpperBound inherited from {http://www.flexiblepower.org/efi-2}StorageRunningModeElement
    _ElementMap.update({
        __lowerBound.name() : __lowerBound,
        __upperBound.name() : __upperBound
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (StorageContinuousRunningModeData):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 627, 11)
    _ElementMap = StorageContinuousRunningModeData._ElementMap.copy()
    _AttributeMap = StorageContinuousRunningModeData._AttributeMap.copy()
    # Base type is StorageContinuousRunningModeData
    
    # Element fillingRate ({http://www.flexiblepower.org/efi-2}fillingRate) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element runningCost ({http://www.flexiblepower.org/efi-2}runningCost) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element electricalPower ({http://www.flexiblepower.org/efi-2}electricalPower) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element gasFlowRate ({http://www.flexiblepower.org/efi-2}gasFlowRate) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element heatTemperature ({http://www.flexiblepower.org/efi-2}heatTemperature) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element heatFlowRate ({http://www.flexiblepower.org/efi-2}heatFlowRate) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element heatThermalPower ({http://www.flexiblepower.org/efi-2}heatThermalPower) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (StorageContinuousRunningModeData):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 634, 11)
    _ElementMap = StorageContinuousRunningModeData._ElementMap.copy()
    _AttributeMap = StorageContinuousRunningModeData._AttributeMap.copy()
    # Base type is StorageContinuousRunningModeData
    
    # Element fillingRate ({http://www.flexiblepower.org/efi-2}fillingRate) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element runningCost ({http://www.flexiblepower.org/efi-2}runningCost) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element electricalPower ({http://www.flexiblepower.org/efi-2}electricalPower) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element gasFlowRate ({http://www.flexiblepower.org/efi-2}gasFlowRate) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element heatTemperature ({http://www.flexiblepower.org/efi-2}heatTemperature) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element heatFlowRate ({http://www.flexiblepower.org/efi-2}heatFlowRate) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    
    # Element heatThermalPower ({http://www.flexiblepower.org/efi-2}heatThermalPower) inherited from {http://www.flexiblepower.org/efi-2}StorageContinuousRunningModeData
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type {http://www.flexiblepower.org/efi-2}AdjustableDiscreteRunningMode with content type ELEMENT_ONLY
class AdjustableDiscreteRunningMode (RunningMode):
    """Complex type {http://www.flexiblepower.org/efi-2}AdjustableDiscreteRunningMode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdjustableDiscreteRunningMode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 824, 1)
    _ElementMap = RunningMode._ElementMap.copy()
    _AttributeMap = RunningMode._AttributeMap.copy()
    # Base type is RunningMode
    
    # Element {http://www.flexiblepower.org/efi-2}runningCost uses Python identifier runningCost
    __runningCost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), 'runningCost', '__httpwww_flexiblepower_orgefi_2_AdjustableDiscreteRunningMode_httpwww_flexiblepower_orgefi_2runningCost', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 828, 5), )

    
    runningCost = property(__runningCost.value, __runningCost.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}electricalPower uses Python identifier electricalPower
    __electricalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), 'electricalPower', '__httpwww_flexiblepower_orgefi_2_AdjustableDiscreteRunningMode_httpwww_flexiblepower_orgefi_2electricalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 829, 5), )

    
    electricalPower = property(__electricalPower.value, __electricalPower.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}gasFlowRate uses Python identifier gasFlowRate
    __gasFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), 'gasFlowRate', '__httpwww_flexiblepower_orgefi_2_AdjustableDiscreteRunningMode_httpwww_flexiblepower_orgefi_2gasFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 830, 5), )

    
    gasFlowRate = property(__gasFlowRate.value, __gasFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatTemperature uses Python identifier heatTemperature
    __heatTemperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), 'heatTemperature', '__httpwww_flexiblepower_orgefi_2_AdjustableDiscreteRunningMode_httpwww_flexiblepower_orgefi_2heatTemperature', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 831, 5), )

    
    heatTemperature = property(__heatTemperature.value, __heatTemperature.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatFlowRate uses Python identifier heatFlowRate
    __heatFlowRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), 'heatFlowRate', '__httpwww_flexiblepower_orgefi_2_AdjustableDiscreteRunningMode_httpwww_flexiblepower_orgefi_2heatFlowRate', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 832, 5), )

    
    heatFlowRate = property(__heatFlowRate.value, __heatFlowRate.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}heatThermalPower uses Python identifier heatThermalPower
    __heatThermalPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), 'heatThermalPower', '__httpwww_flexiblepower_orgefi_2_AdjustableDiscreteRunningMode_httpwww_flexiblepower_orgefi_2heatThermalPower', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 833, 5), )

    
    heatThermalPower = property(__heatThermalPower.value, __heatThermalPower.set, None, None)

    
    # Attribute id inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    
    # Attribute label inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    _ElementMap.update({
        __runningCost.name() : __runningCost,
        __electricalPower.name() : __electricalPower,
        __gasFlowRate.name() : __gasFlowRate,
        __heatTemperature.name() : __heatTemperature,
        __heatFlowRate.name() : __heatFlowRate,
        __heatThermalPower.name() : __heatThermalPower
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdjustableDiscreteRunningMode = AdjustableDiscreteRunningMode
Namespace.addCategoryObject('typeBinding', 'AdjustableDiscreteRunningMode', AdjustableDiscreteRunningMode)


# Complex type {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningMode with content type ELEMENT_ONLY
class AdjustableContinuousRunningMode (RunningMode):
    """Complex type {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningMode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdjustableContinuousRunningMode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 848, 1)
    _ElementMap = RunningMode._ElementMap.copy()
    _AttributeMap = RunningMode._AttributeMap.copy()
    # Base type is RunningMode
    
    # Element {http://www.flexiblepower.org/efi-2}lowerBound uses Python identifier lowerBound
    __lowerBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lowerBound'), 'lowerBound', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningMode_httpwww_flexiblepower_orgefi_2lowerBound', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 852, 5), )

    
    lowerBound = property(__lowerBound.value, __lowerBound.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}upperBound uses Python identifier upperBound
    __upperBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'upperBound'), 'upperBound', '__httpwww_flexiblepower_orgefi_2_AdjustableContinuousRunningMode_httpwww_flexiblepower_orgefi_2upperBound', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 859, 5), )

    
    upperBound = property(__upperBound.value, __upperBound.set, None, None)

    
    # Attribute id inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    
    # Attribute label inherited from {http://www.flexiblepower.org/efi-2}RunningMode
    _ElementMap.update({
        __lowerBound.name() : __lowerBound,
        __upperBound.name() : __upperBound
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdjustableContinuousRunningMode = AdjustableContinuousRunningMode
Namespace.addCategoryObject('typeBinding', 'AdjustableContinuousRunningMode', AdjustableContinuousRunningMode)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (AdjustableContinuousRunningModeData):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 853, 6)
    _ElementMap = AdjustableContinuousRunningModeData._ElementMap.copy()
    _AttributeMap = AdjustableContinuousRunningModeData._AttributeMap.copy()
    # Base type is AdjustableContinuousRunningModeData
    
    # Element runningCost ({http://www.flexiblepower.org/efi-2}runningCost) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element electricalPower ({http://www.flexiblepower.org/efi-2}electricalPower) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element gasFlowRate ({http://www.flexiblepower.org/efi-2}gasFlowRate) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element heatTemperature ({http://www.flexiblepower.org/efi-2}heatTemperature) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element heatFlowRate ({http://www.flexiblepower.org/efi-2}heatFlowRate) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element heatThermalPower ({http://www.flexiblepower.org/efi-2}heatThermalPower) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (AdjustableContinuousRunningModeData):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 860, 6)
    _ElementMap = AdjustableContinuousRunningModeData._ElementMap.copy()
    _AttributeMap = AdjustableContinuousRunningModeData._AttributeMap.copy()
    # Base type is AdjustableContinuousRunningModeData
    
    # Element runningCost ({http://www.flexiblepower.org/efi-2}runningCost) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element electricalPower ({http://www.flexiblepower.org/efi-2}electricalPower) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element gasFlowRate ({http://www.flexiblepower.org/efi-2}gasFlowRate) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element heatTemperature ({http://www.flexiblepower.org/efi-2}heatTemperature) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element heatFlowRate ({http://www.flexiblepower.org/efi-2}heatFlowRate) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    
    # Element heatThermalPower ({http://www.flexiblepower.org/efi-2}heatThermalPower) inherited from {http://www.flexiblepower.org/efi-2}AdjustableContinuousRunningModeData
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (FlexibilityRegistration):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 216, 2)
    _ElementMap = FlexibilityRegistration._ElementMap.copy()
    _AttributeMap = FlexibilityRegistration._AttributeMap.copy()
    # Base type is FlexibilityRegistration
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionProcessingDelay ({http://www.flexiblepower.org/efi-2}instructionProcessingDelay) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element deviceDescription ({http://www.flexiblepower.org/efi-2}deviceDescription) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element currency ({http://www.flexiblepower.org/efi-2}currency) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element {http://www.flexiblepower.org/efi-2}supportedCommodities uses Python identifier supportedCommodities
    __supportedCommodities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities'), 'supportedCommodities', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_22_httpwww_flexiblepower_orgefi_2supportedCommodities', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 220, 6), )

    
    supportedCommodities = property(__supportedCommodities.value, __supportedCommodities.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __supportedCommodities.name() : __supportedCommodities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type {http://www.flexiblepower.org/efi-2}InflexibleUpdate with content type ELEMENT_ONLY
class InflexibleUpdate (FlexibilityUpdate):
    """Complex type {http://www.flexiblepower.org/efi-2}InflexibleUpdate with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InflexibleUpdate')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 247, 1)
    _ElementMap = FlexibilityUpdate._ElementMap.copy()
    _AttributeMap = FlexibilityUpdate._AttributeMap.copy()
    # Base type is FlexibilityUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InflexibleUpdate = InflexibleUpdate
Namespace.addCategoryObject('typeBinding', 'InflexibleUpdate', InflexibleUpdate)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (Instruction):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 319, 2)
    _ElementMap = Instruction._ElementMap.copy()
    _AttributeMap = Instruction._AttributeMap.copy()
    # Base type is Instruction
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionId ({http://www.flexiblepower.org/efi-2}instructionId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element isEmergencyInstruction ({http://www.flexiblepower.org/efi-2}isEmergencyInstruction) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element {http://www.flexiblepower.org/efi-2}curtailmentProfile uses Python identifier curtailmentProfile
    __curtailmentProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'curtailmentProfile'), 'curtailmentProfile', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_23_httpwww_flexiblepower_orgefi_2curtailmentProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 323, 6), )

    
    curtailmentProfile = property(__curtailmentProfile.value, __curtailmentProfile.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __curtailmentProfile.name() : __curtailmentProfile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (FlexibilityRegistration):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 341, 2)
    _ElementMap = FlexibilityRegistration._ElementMap.copy()
    _AttributeMap = FlexibilityRegistration._AttributeMap.copy()
    # Base type is FlexibilityRegistration
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionProcessingDelay ({http://www.flexiblepower.org/efi-2}instructionProcessingDelay) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element deviceDescription ({http://www.flexiblepower.org/efi-2}deviceDescription) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element currency ({http://www.flexiblepower.org/efi-2}currency) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element {http://www.flexiblepower.org/efi-2}supportedCommodities uses Python identifier supportedCommodities
    __supportedCommodities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities'), 'supportedCommodities', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_24_httpwww_flexiblepower_orgefi_2supportedCommodities', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 345, 6), )

    
    supportedCommodities = property(__supportedCommodities.value, __supportedCommodities.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __supportedCommodities.name() : __supportedCommodities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (FlexibilityUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 376, 2)
    _ElementMap = FlexibilityUpdate._ElementMap.copy()
    _AttributeMap = FlexibilityUpdate._AttributeMap.copy()
    # Base type is FlexibilityUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}endBefore uses Python identifier endBefore
    __endBefore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endBefore'), 'endBefore', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_25_httpwww_flexiblepower_orgefi_2endBefore', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 380, 6), )

    
    endBefore = property(__endBefore.value, __endBefore.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}sequentialProfiles uses Python identifier sequentialProfiles
    __sequentialProfiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfiles'), 'sequentialProfiles', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_25_httpwww_flexiblepower_orgefi_2sequentialProfiles', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 381, 6), )

    
    sequentialProfiles = property(__sequentialProfiles.value, __sequentialProfiles.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __endBefore.name() : __endBefore,
        __sequentialProfiles.name() : __sequentialProfiles
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (Instruction):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 400, 2)
    _ElementMap = Instruction._ElementMap.copy()
    _AttributeMap = Instruction._AttributeMap.copy()
    # Base type is Instruction
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionId ({http://www.flexiblepower.org/efi-2}instructionId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element isEmergencyInstruction ({http://www.flexiblepower.org/efi-2}isEmergencyInstruction) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element {http://www.flexiblepower.org/efi-2}sequentialProfileInstructions uses Python identifier sequentialProfileInstructions
    __sequentialProfileInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileInstructions'), 'sequentialProfileInstructions', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_26_httpwww_flexiblepower_orgefi_2sequentialProfileInstructions', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 404, 6), )

    
    sequentialProfileInstructions = property(__sequentialProfileInstructions.value, __sequentialProfileInstructions.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __sequentialProfileInstructions.name() : __sequentialProfileInstructions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (FlexibilityRegistration):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 411, 2)
    _ElementMap = FlexibilityRegistration._ElementMap.copy()
    _AttributeMap = FlexibilityRegistration._AttributeMap.copy()
    # Base type is FlexibilityRegistration
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionProcessingDelay ({http://www.flexiblepower.org/efi-2}instructionProcessingDelay) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element deviceDescription ({http://www.flexiblepower.org/efi-2}deviceDescription) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element currency ({http://www.flexiblepower.org/efi-2}currency) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element {http://www.flexiblepower.org/efi-2}fillLevelLabel uses Python identifier fillLevelLabel
    __fillLevelLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fillLevelLabel'), 'fillLevelLabel', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_27_httpwww_flexiblepower_orgefi_2fillLevelLabel', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 415, 6), )

    
    fillLevelLabel = property(__fillLevelLabel.value, __fillLevelLabel.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}fillLevelUnit uses Python identifier fillLevelUnit
    __fillLevelUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fillLevelUnit'), 'fillLevelUnit', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_27_httpwww_flexiblepower_orgefi_2fillLevelUnit', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 416, 6), )

    
    fillLevelUnit = property(__fillLevelUnit.value, __fillLevelUnit.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}actuators uses Python identifier actuators
    __actuators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuators'), 'actuators', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_27_httpwww_flexiblepower_orgefi_2actuators', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 417, 6), )

    
    actuators = property(__actuators.value, __actuators.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __fillLevelLabel.name() : __fillLevelLabel,
        __fillLevelUnit.name() : __fillLevelUnit,
        __actuators.name() : __actuators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


# Complex type {http://www.flexiblepower.org/efi-2}StorageUpdate with content type ELEMENT_ONLY
class StorageUpdate (FlexibilityUpdate):
    """Complex type {http://www.flexiblepower.org/efi-2}StorageUpdate with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageUpdate')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 692, 1)
    _ElementMap = FlexibilityUpdate._ElementMap.copy()
    _AttributeMap = FlexibilityUpdate._AttributeMap.copy()
    # Base type is FlexibilityUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StorageUpdate = StorageUpdate
Namespace.addCategoryObject('typeBinding', 'StorageUpdate', StorageUpdate)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (Instruction):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 803, 2)
    _ElementMap = Instruction._ElementMap.copy()
    _AttributeMap = Instruction._AttributeMap.copy()
    # Base type is Instruction
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionId ({http://www.flexiblepower.org/efi-2}instructionId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element isEmergencyInstruction ({http://www.flexiblepower.org/efi-2}isEmergencyInstruction) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element {http://www.flexiblepower.org/efi-2}actuatorInstructions uses Python identifier actuatorInstructions
    __actuatorInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuatorInstructions'), 'actuatorInstructions', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_28_httpwww_flexiblepower_orgefi_2actuatorInstructions', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 807, 6), )

    
    actuatorInstructions = property(__actuatorInstructions.value, __actuatorInstructions.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __actuatorInstructions.name() : __actuatorInstructions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_28 = CTD_ANON_28


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (FlexibilityRegistration):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 814, 2)
    _ElementMap = FlexibilityRegistration._ElementMap.copy()
    _AttributeMap = FlexibilityRegistration._AttributeMap.copy()
    # Base type is FlexibilityRegistration
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionProcessingDelay ({http://www.flexiblepower.org/efi-2}instructionProcessingDelay) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element deviceDescription ({http://www.flexiblepower.org/efi-2}deviceDescription) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element currency ({http://www.flexiblepower.org/efi-2}currency) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityRegistration
    
    # Element {http://www.flexiblepower.org/efi-2}supportedCommodities uses Python identifier supportedCommodities
    __supportedCommodities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities'), 'supportedCommodities', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_29_httpwww_flexiblepower_orgefi_2supportedCommodities', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 818, 6), )

    
    supportedCommodities = property(__supportedCommodities.value, __supportedCommodities.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __supportedCommodities.name() : __supportedCommodities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_29 = CTD_ANON_29


# Complex type {http://www.flexiblepower.org/efi-2}AdjustableUpdate with content type ELEMENT_ONLY
class AdjustableUpdate (FlexibilityUpdate):
    """Complex type {http://www.flexiblepower.org/efi-2}AdjustableUpdate with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdjustableUpdate')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 891, 1)
    _ElementMap = FlexibilityUpdate._ElementMap.copy()
    _AttributeMap = FlexibilityUpdate._AttributeMap.copy()
    # Base type is FlexibilityUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdjustableUpdate = AdjustableUpdate
Namespace.addCategoryObject('typeBinding', 'AdjustableUpdate', AdjustableUpdate)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (Instruction):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 919, 2)
    _ElementMap = Instruction._ElementMap.copy()
    _AttributeMap = Instruction._AttributeMap.copy()
    # Base type is Instruction
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element instructionId ({http://www.flexiblepower.org/efi-2}instructionId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element isEmergencyInstruction ({http://www.flexiblepower.org/efi-2}isEmergencyInstruction) inherited from {http://www.flexiblepower.org/efi-2}Instruction
    
    # Element {http://www.flexiblepower.org/efi-2}runningModeId uses Python identifier runningModeId
    __runningModeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModeId'), 'runningModeId', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_30_httpwww_flexiblepower_orgefi_2runningModeId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 923, 6), )

    
    runningModeId = property(__runningModeId.value, __runningModeId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}runningModeFactor uses Python identifier runningModeFactor
    __runningModeFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), 'runningModeFactor', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_30_httpwww_flexiblepower_orgefi_2runningModeFactor', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 924, 6), )

    
    runningModeFactor = property(__runningModeFactor.value, __runningModeFactor.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startTime'), 'startTime', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_30_httpwww_flexiblepower_orgefi_2startTime', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 932, 6), )

    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __runningModeId.name() : __runningModeId,
        __runningModeFactor.name() : __runningModeFactor,
        __startTime.name() : __startTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_30 = CTD_ANON_30


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (InflexibleUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 281, 2)
    _ElementMap = InflexibleUpdate._ElementMap.copy()
    _AttributeMap = InflexibleUpdate._AttributeMap.copy()
    # Base type is InflexibleUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}forecastProfiles uses Python identifier forecastProfiles
    __forecastProfiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'forecastProfiles'), 'forecastProfiles', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_31_httpwww_flexiblepower_orgefi_2forecastProfiles', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 285, 6), )

    
    forecastProfiles = property(__forecastProfiles.value, __forecastProfiles.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __forecastProfiles.name() : __forecastProfiles
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_31 = CTD_ANON_31


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (InflexibleUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 308, 2)
    _ElementMap = InflexibleUpdate._ElementMap.copy()
    _AttributeMap = InflexibleUpdate._AttributeMap.copy()
    # Base type is InflexibleUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}curtailmentOptions uses Python identifier curtailmentOptions
    __curtailmentOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'curtailmentOptions'), 'curtailmentOptions', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_32_httpwww_flexiblepower_orgefi_2curtailmentOptions', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 312, 6), )

    
    curtailmentOptions = property(__curtailmentOptions.value, __curtailmentOptions.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __curtailmentOptions.name() : __curtailmentOptions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_32 = CTD_ANON_32


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (StorageUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 681, 2)
    _ElementMap = StorageUpdate._ElementMap.copy()
    _AttributeMap = StorageUpdate._AttributeMap.copy()
    # Base type is StorageUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}actuatorBehaviours uses Python identifier actuatorBehaviours
    __actuatorBehaviours = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuatorBehaviours'), 'actuatorBehaviours', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_33_httpwww_flexiblepower_orgefi_2actuatorBehaviours', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 685, 6), )

    
    actuatorBehaviours = property(__actuatorBehaviours.value, __actuatorBehaviours.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}leakageBehaviour uses Python identifier leakageBehaviour
    __leakageBehaviour = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'leakageBehaviour'), 'leakageBehaviour', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_33_httpwww_flexiblepower_orgefi_2leakageBehaviour', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 686, 6), )

    
    leakageBehaviour = property(__leakageBehaviour.value, __leakageBehaviour.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __actuatorBehaviours.name() : __actuatorBehaviours,
        __leakageBehaviour.name() : __leakageBehaviour
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_33 = CTD_ANON_33


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (StorageUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 731, 2)
    _ElementMap = StorageUpdate._ElementMap.copy()
    _AttributeMap = StorageUpdate._AttributeMap.copy()
    # Base type is StorageUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}currentFillLevel uses Python identifier currentFillLevel
    __currentFillLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentFillLevel'), 'currentFillLevel', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_34_httpwww_flexiblepower_orgefi_2currentFillLevel', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 735, 6), )

    
    currentFillLevel = property(__currentFillLevel.value, __currentFillLevel.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}actuatorStatuses uses Python identifier actuatorStatuses
    __actuatorStatuses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuatorStatuses'), 'actuatorStatuses', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_34_httpwww_flexiblepower_orgefi_2actuatorStatuses', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 736, 6), )

    
    actuatorStatuses = property(__actuatorStatuses.value, __actuatorStatuses.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __currentFillLevel.name() : __currentFillLevel,
        __actuatorStatuses.name() : __actuatorStatuses
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_34 = CTD_ANON_34


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (StorageUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 754, 2)
    _ElementMap = StorageUpdate._ElementMap.copy()
    _AttributeMap = StorageUpdate._AttributeMap.copy()
    # Base type is StorageUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}targetProfile uses Python identifier targetProfile
    __targetProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'targetProfile'), 'targetProfile', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_35_httpwww_flexiblepower_orgefi_2targetProfile', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 758, 6), )

    
    targetProfile = property(__targetProfile.value, __targetProfile.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __targetProfile.name() : __targetProfile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_35 = CTD_ANON_35


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (StorageUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 765, 2)
    _ElementMap = StorageUpdate._ElementMap.copy()
    _AttributeMap = StorageUpdate._AttributeMap.copy()
    # Base type is StorageUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}usageForecast uses Python identifier usageForecast
    __usageForecast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usageForecast'), 'usageForecast', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_36_httpwww_flexiblepower_orgefi_2usageForecast', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 769, 6), )

    
    usageForecast = property(__usageForecast.value, __usageForecast.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __usageForecast.name() : __usageForecast
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_36 = CTD_ANON_36


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (AdjustableUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 879, 2)
    _ElementMap = AdjustableUpdate._ElementMap.copy()
    _AttributeMap = AdjustableUpdate._AttributeMap.copy()
    # Base type is AdjustableUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}runningModes uses Python identifier runningModes
    __runningModes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModes'), 'runningModes', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_37_httpwww_flexiblepower_orgefi_2runningModes', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 883, 6), )

    
    runningModes = property(__runningModes.value, __runningModes.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}timers uses Python identifier timers
    __timers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timers'), 'timers', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_37_httpwww_flexiblepower_orgefi_2timers', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 884, 6), )

    
    timers = property(__timers.value, __timers.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}transitions uses Python identifier transitions
    __transitions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transitions'), 'transitions', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_37_httpwww_flexiblepower_orgefi_2transitions', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 885, 6), )

    
    transitions = property(__transitions.value, __transitions.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __runningModes.name() : __runningModes,
        __timers.name() : __timers,
        __transitions.name() : __transitions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_37 = CTD_ANON_37


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (AdjustableUpdate):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 897, 2)
    _ElementMap = AdjustableUpdate._ElementMap.copy()
    _AttributeMap = AdjustableUpdate._AttributeMap.copy()
    # Base type is AdjustableUpdate
    
    # Element header ({http://www.flexiblepower.org/efi-2}header) inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    
    # Element flexibilityUpdateId ({http://www.flexiblepower.org/efi-2}flexibilityUpdateId) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element validFrom ({http://www.flexiblepower.org/efi-2}validFrom) inherited from {http://www.flexiblepower.org/efi-2}FlexibilityUpdate
    
    # Element {http://www.flexiblepower.org/efi-2}currentRunningModeId uses Python identifier currentRunningModeId
    __currentRunningModeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentRunningModeId'), 'currentRunningModeId', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_38_httpwww_flexiblepower_orgefi_2currentRunningModeId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 901, 6), )

    
    currentRunningModeId = property(__currentRunningModeId.value, __currentRunningModeId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}runningModeFactor uses Python identifier runningModeFactor
    __runningModeFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), 'runningModeFactor', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_38_httpwww_flexiblepower_orgefi_2runningModeFactor', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 902, 6), )

    
    runningModeFactor = property(__runningModeFactor.value, __runningModeFactor.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}previousRunningModeId uses Python identifier previousRunningModeId
    __previousRunningModeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'previousRunningModeId'), 'previousRunningModeId', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_38_httpwww_flexiblepower_orgefi_2previousRunningModeId', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 910, 6), )

    
    previousRunningModeId = property(__previousRunningModeId.value, __previousRunningModeId.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}transitionTimestamp uses Python identifier transitionTimestamp
    __transitionTimestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transitionTimestamp'), 'transitionTimestamp', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_38_httpwww_flexiblepower_orgefi_2transitionTimestamp', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 911, 6), )

    
    transitionTimestamp = property(__transitionTimestamp.value, __transitionTimestamp.set, None, None)

    
    # Element {http://www.flexiblepower.org/efi-2}timerUpdates uses Python identifier timerUpdates
    __timerUpdates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timerUpdates'), 'timerUpdates', '__httpwww_flexiblepower_orgefi_2_CTD_ANON_38_httpwww_flexiblepower_orgefi_2timerUpdates', False, pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 912, 6), )

    
    timerUpdates = property(__timerUpdates.value, __timerUpdates.set, None, None)

    
    # Attribute efiVersion inherited from {http://www.flexiblepower.org/efi-2}EfiMessage
    _ElementMap.update({
        __currentRunningModeId.name() : __currentRunningModeId,
        __runningModeFactor.name() : __runningModeFactor,
        __previousRunningModeId.name() : __previousRunningModeId,
        __transitionTimestamp.name() : __transitionTimestamp,
        __timerUpdates.name() : __timerUpdates
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_38 = CTD_ANON_38


InstructionStatusUpdate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstructionStatusUpdate'), CTD_ANON_12, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 74, 1))
Namespace.addCategoryObject('elementBinding', InstructionStatusUpdate.name().localName(), InstructionStatusUpdate)

FlexibilityRevoke = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlexibilityRevoke'), CTD_ANON_13, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', FlexibilityRevoke.name().localName(), FlexibilityRevoke)

InstructionRevoke = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstructionRevoke'), CTD_ANON_14, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 103, 1))
Namespace.addCategoryObject('elementBinding', InstructionRevoke.name().localName(), InstructionRevoke)

Measurement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Measurement'), CTD_ANON_15, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 252, 1))
Namespace.addCategoryObject('elementBinding', Measurement.name().localName(), Measurement)

InflexibleRegistration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InflexibleRegistration'), CTD_ANON_22, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 215, 1))
Namespace.addCategoryObject('elementBinding', InflexibleRegistration.name().localName(), InflexibleRegistration)

InflexibleInstruction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InflexibleInstruction'), CTD_ANON_23, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 318, 1))
Namespace.addCategoryObject('elementBinding', InflexibleInstruction.name().localName(), InflexibleInstruction)

ShiftableRegistration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShiftableRegistration'), CTD_ANON_24, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 340, 1))
Namespace.addCategoryObject('elementBinding', ShiftableRegistration.name().localName(), ShiftableRegistration)

ShiftableUpdate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShiftableUpdate'), CTD_ANON_25, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 375, 1))
Namespace.addCategoryObject('elementBinding', ShiftableUpdate.name().localName(), ShiftableUpdate)

ShiftableInstruction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShiftableInstruction'), CTD_ANON_26, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 399, 1))
Namespace.addCategoryObject('elementBinding', ShiftableInstruction.name().localName(), ShiftableInstruction)

StorageRegistration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StorageRegistration'), CTD_ANON_27, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 410, 1))
Namespace.addCategoryObject('elementBinding', StorageRegistration.name().localName(), StorageRegistration)

StorageInstruction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StorageInstruction'), CTD_ANON_28, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 802, 1))
Namespace.addCategoryObject('elementBinding', StorageInstruction.name().localName(), StorageInstruction)

AdjustableRegistration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdjustableRegistration'), CTD_ANON_29, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 813, 1))
Namespace.addCategoryObject('elementBinding', AdjustableRegistration.name().localName(), AdjustableRegistration)

AdjustableInstruction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdjustableInstruction'), CTD_ANON_30, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 918, 1))
Namespace.addCategoryObject('elementBinding', AdjustableInstruction.name().localName(), AdjustableInstruction)

InflexibleForecast = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InflexibleForecast'), CTD_ANON_31, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 280, 1))
Namespace.addCategoryObject('elementBinding', InflexibleForecast.name().localName(), InflexibleForecast)

InflexibleCurtailmentOptions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InflexibleCurtailmentOptions'), CTD_ANON_32, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 307, 1))
Namespace.addCategoryObject('elementBinding', InflexibleCurtailmentOptions.name().localName(), InflexibleCurtailmentOptions)

StorageSystemDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StorageSystemDescription'), CTD_ANON_33, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 680, 1))
Namespace.addCategoryObject('elementBinding', StorageSystemDescription.name().localName(), StorageSystemDescription)

StorageStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StorageStatus'), CTD_ANON_34, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 730, 1))
Namespace.addCategoryObject('elementBinding', StorageStatus.name().localName(), StorageStatus)

StorageFillLevelTargetProfile = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StorageFillLevelTargetProfile'), CTD_ANON_35, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 753, 1))
Namespace.addCategoryObject('elementBinding', StorageFillLevelTargetProfile.name().localName(), StorageFillLevelTargetProfile)

StorageUsageForecast = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StorageUsageForecast'), CTD_ANON_36, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 764, 1))
Namespace.addCategoryObject('elementBinding', StorageUsageForecast.name().localName(), StorageUsageForecast)

AdjustableSystemDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdjustableSystemDescription'), CTD_ANON_37, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 878, 1))
Namespace.addCategoryObject('elementBinding', AdjustableSystemDescription.name().localName(), AdjustableSystemDescription)

AdjustableStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdjustableStatus'), CTD_ANON_38, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 896, 1))
Namespace.addCategoryObject('elementBinding', AdjustableStatus.name().localName(), AdjustableStatus)



EfiMessage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'header'), CTD_ANON, scope=EfiMessage, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EfiMessage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EfiMessage._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'efiResourceId'), Identifier, scope=CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 27, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 28, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'efiResourceId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 27, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 28, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




DeviceDescription._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deviceClass'), DeviceClass, scope=DeviceDescription, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 37, 3)))

DeviceDescription._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serialNumber'), pyxb.binding.datatypes.string, scope=DeviceDescription, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 38, 3)))

DeviceDescription._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), pyxb.binding.datatypes.string, scope=DeviceDescription, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 39, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 38, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 39, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeviceDescription._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deviceClass')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 37, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeviceDescription._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serialNumber')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DeviceDescription._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'label')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 39, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeviceDescription._Automaton = _BuildAutomaton_2()




StorageUsageProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'element'), CTD_ANON_, scope=StorageUsageProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 146, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageUsageProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'element')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 146, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StorageUsageProfile._Automaton = _BuildAutomaton_3()




StorageUsageProbabilityProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usageRateElement'), ProbabilityAttributesWithDuration, scope=StorageUsageProbabilityProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 156, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageUsageProbabilityProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usageRateElement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 156, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StorageUsageProbabilityProfile._Automaton = _BuildAutomaton_4()




ElectricityProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'element'), CTD_ANON_2, scope=ElectricityProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 161, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ElectricityProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'element')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 161, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ElectricityProfile._Automaton = _BuildAutomaton_5()




ElectricityProbabilityProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'powerElement'), ProbabilityAttributesWithDuration, scope=ElectricityProbabilityProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 171, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ElectricityProbabilityProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'powerElement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 171, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ElectricityProbabilityProfile._Automaton = _BuildAutomaton_6()




GasProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'element'), CTD_ANON_3, scope=GasProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 176, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GasProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'element')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 176, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GasProfile._Automaton = _BuildAutomaton_7()




GasProbabilityProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flowRateElement'), ProbabilityAttributesWithDuration, scope=GasProbabilityProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 186, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GasProbabilityProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flowRateElement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 186, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GasProbabilityProfile._Automaton = _BuildAutomaton_8()




HeatProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'element'), CTD_ANON_4, scope=HeatProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 191, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(HeatProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'element')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
HeatProfile._Automaton = _BuildAutomaton_9()




HeatProbabilityProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'element'), CTD_ANON_5, scope=HeatProbabilityProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 203, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(HeatProbabilityProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'element')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 203, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
HeatProbabilityProfile._Automaton = _BuildAutomaton_10()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temperature'), ProbabilityAttributes, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 206, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flowRate'), ProbabilityAttributes, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 207, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thermalPower'), ProbabilityAttributes, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 208, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 206, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 207, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 208, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 206, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 207, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'thermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 208, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_11()




SupportedCommodities._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'commodityType'), CommodityEnum, scope=SupportedCommodities, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 228, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SupportedCommodities._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'commodityType')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 228, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupportedCommodities._Automaton = _BuildAutomaton_12()




CurtailmentOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'curtailmentOption'), CurtailmentOption, scope=CurtailmentOptions, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 233, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 233, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CurtailmentOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'curtailmentOption')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 233, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CurtailmentOptions._Automaton = _BuildAutomaton_13()




ProfileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electricityProfile'), ElectricityProfile, scope=ProfileContainer, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 294, 4)))

ProfileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electricityProbabilityProfile'), ElectricityProbabilityProfile, scope=ProfileContainer, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 295, 4)))

ProfileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gasProfile'), GasProfile, scope=ProfileContainer, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 298, 4)))

ProfileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gasProbabilityProfile'), GasProbabilityProfile, scope=ProfileContainer, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 299, 4)))

ProfileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatProfile'), HeatProfile, scope=ProfileContainer, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 302, 4)))

ProfileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatProbabilityProfile'), HeatProbabilityProfile, scope=ProfileContainer, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 303, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 293, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 297, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 301, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProfileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 294, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProfileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricityProbabilityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 295, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ProfileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 298, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ProfileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasProbabilityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 299, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ProfileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 302, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ProfileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatProbabilityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 303, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProfileContainer._Automaton = _BuildAutomaton_14()




SequentialProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxIntervalBefore'), pyxb.binding.datatypes.duration, scope=SequentialProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 353, 3)))

SequentialProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileAlternatives'), SequentialProfileAlternatives, scope=SequentialProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 354, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequentialProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxIntervalBefore')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 353, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequentialProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileAlternatives')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 354, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequentialProfile._Automaton = _BuildAutomaton_15()




SequentialProfileAlternatives._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileAlternative'), SequentialProfileAlternative, scope=SequentialProfileAlternatives, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 367, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequentialProfileAlternatives._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileAlternative')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 367, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequentialProfileAlternatives._Automaton = _BuildAutomaton_16()




SequentialProfiles._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfile'), SequentialProfile, scope=SequentialProfiles, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 372, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequentialProfiles._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 372, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequentialProfiles._Automaton = _BuildAutomaton_17()




SequentialProfileInstruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequenceNr'), pyxb.binding.datatypes.int, scope=SequentialProfileInstruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 389, 3)))

SequentialProfileInstruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alternativeNr'), pyxb.binding.datatypes.int, scope=SequentialProfileInstruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 390, 3)))

SequentialProfileInstruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startTime'), pyxb.binding.datatypes.dateTime, scope=SequentialProfileInstruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 391, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequentialProfileInstruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequenceNr')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 389, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequentialProfileInstruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alternativeNr')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 390, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequentialProfileInstruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startTime')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 391, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequentialProfileInstruction._Automaton = _BuildAutomaton_18()




SequentialProfileInstructions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileInstruction'), SequentialProfileInstruction, scope=SequentialProfileInstructions, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 396, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequentialProfileInstructions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileInstruction')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 396, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequentialProfileInstructions._Automaton = _BuildAutomaton_19()




Actuator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodity'), CommodityEnum, scope=Actuator, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 425, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Actuator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodity')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 425, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Actuator._Automaton = _BuildAutomaton_20()




Actuators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuator'), Actuator, scope=Actuators, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 432, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Actuators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuator')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 432, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Actuators._Automaton = _BuildAutomaton_21()




Timers._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timer'), Timer, scope=Timers, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 442, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Timers._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timer')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 442, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Timers._Automaton = _BuildAutomaton_22()




Transitions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transition'), Transition, scope=Transitions, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 447, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Transitions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transition')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 447, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Transitions._Automaton = _BuildAutomaton_23()




TimerReferences._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timerReference'), CTD_ANON_9, scope=TimerReferences, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 452, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimerReferences._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timerReference')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 452, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TimerReferences._Automaton = _BuildAutomaton_24()




Transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startTimers'), TimerReferences, scope=Transition, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 461, 3)))

Transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockingTimers'), TimerReferences, scope=Transition, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 462, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 461, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 462, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Transition._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startTimers')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 461, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Transition._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockingTimers')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 462, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Transition._Automaton = _BuildAutomaton_25()




StorageContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fillingRate'), pyxb.binding.datatypes.double, scope=StorageContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 608, 3)))

StorageContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), pyxb.binding.datatypes.decimal, scope=StorageContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3)))

StorageContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), pyxb.binding.datatypes.double, scope=StorageContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3)))

StorageContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), pyxb.binding.datatypes.double, scope=StorageContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3)))

StorageContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), pyxb.binding.datatypes.double, scope=StorageContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3)))

StorageContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), pyxb.binding.datatypes.double, scope=StorageContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3)))

StorageContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), pyxb.binding.datatypes.double, scope=StorageContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fillingRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 608, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StorageContinuousRunningModeData._Automaton = _BuildAutomaton_26()




StorageRunningModes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningMode'), StorageDiscreteRunningMode, scope=StorageRunningModes, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 652, 4)))

StorageRunningModes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningMode'), StorageContinuousRunningMode, scope=StorageRunningModes, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 653, 4)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageRunningModes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningMode')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 652, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageRunningModes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningMode')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 653, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StorageRunningModes._Automaton = _BuildAutomaton_27()




ActuatorBehaviour._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModes'), StorageRunningModes, scope=ActuatorBehaviour, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 659, 3)))

ActuatorBehaviour._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timers'), Timers, scope=ActuatorBehaviour, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 660, 3)))

ActuatorBehaviour._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transitions'), Transitions, scope=ActuatorBehaviour, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 661, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 660, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ActuatorBehaviour._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModes')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 659, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ActuatorBehaviour._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timers')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 660, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActuatorBehaviour._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transitions')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 661, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ActuatorBehaviour._Automaton = _BuildAutomaton_28()




LeakageFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'leakageElement'), LeakageElement, scope=LeakageFunction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 672, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LeakageFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'leakageElement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 672, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LeakageFunction._Automaton = _BuildAutomaton_29()




ActuatorBehaviours._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuatorBehaviour'), ActuatorBehaviour, scope=ActuatorBehaviours, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 677, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActuatorBehaviours._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuatorBehaviour')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 677, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ActuatorBehaviours._Automaton = _BuildAutomaton_30()




TimerUpdate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'finishedAt'), pyxb.binding.datatypes.dateTime, scope=TimerUpdate, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 699, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimerUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'finishedAt')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 699, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TimerUpdate._Automaton = _BuildAutomaton_31()




TimerUpdates._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timerUpdate'), TimerUpdate, scope=TimerUpdates, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 705, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 705, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimerUpdates._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timerUpdate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 705, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimerUpdates._Automaton = _BuildAutomaton_32()




ActuatorStatus._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentRunningMode'), pyxb.binding.datatypes.int, scope=ActuatorStatus, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 710, 3)))

ActuatorStatus._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), STD_ANON, scope=ActuatorStatus, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 711, 3)))

ActuatorStatus._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'previousRunningModeId'), pyxb.binding.datatypes.int, scope=ActuatorStatus, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 719, 3)))

ActuatorStatus._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transitionTimestamp'), pyxb.binding.datatypes.dateTime, scope=ActuatorStatus, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 720, 3)))

ActuatorStatus._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timerUpdates'), TimerUpdates, scope=ActuatorStatus, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 721, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 711, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 719, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 720, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 721, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActuatorStatus._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentRunningMode')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 710, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActuatorStatus._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 711, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ActuatorStatus._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'previousRunningModeId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 719, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ActuatorStatus._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transitionTimestamp')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 720, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ActuatorStatus._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timerUpdates')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 721, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ActuatorStatus._Automaton = _BuildAutomaton_33()




ActuatorStatuses._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuatorStatus'), ActuatorStatus, scope=ActuatorStatuses, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 727, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActuatorStatuses._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuatorStatus')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 727, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ActuatorStatuses._Automaton = _BuildAutomaton_34()




TargetProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'element'), CTD_ANON_10, scope=TargetProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 744, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TargetProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'element')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 744, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TargetProfile._Automaton = _BuildAutomaton_35()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usageProfile'), StorageUsageProfile, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 772, 9)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usageProbabilityProfile'), StorageUsageProbabilityProfile, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 773, 9)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usageProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 772, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usageProbabilityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 773, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_36()




ActuatorInstruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModeId'), pyxb.binding.datatypes.int, scope=ActuatorInstruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 784, 3)))

ActuatorInstruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), STD_ANON_, scope=ActuatorInstruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 785, 3)))

ActuatorInstruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startTime'), pyxb.binding.datatypes.dateTime, scope=ActuatorInstruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 793, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 785, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ActuatorInstruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModeId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 784, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ActuatorInstruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 785, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActuatorInstruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startTime')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 793, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ActuatorInstruction._Automaton = _BuildAutomaton_37()




ActuatorInstructions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuatorInstruction'), ActuatorInstruction, scope=ActuatorInstructions, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 799, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActuatorInstructions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuatorInstruction')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 799, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ActuatorInstructions._Automaton = _BuildAutomaton_38()




AdjustableContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), pyxb.binding.datatypes.decimal, scope=AdjustableContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3)))

AdjustableContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), pyxb.binding.datatypes.double, scope=AdjustableContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3)))

AdjustableContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), pyxb.binding.datatypes.double, scope=AdjustableContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3)))

AdjustableContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), pyxb.binding.datatypes.double, scope=AdjustableContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3)))

AdjustableContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), pyxb.binding.datatypes.double, scope=AdjustableContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3)))

AdjustableContinuousRunningModeData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), pyxb.binding.datatypes.double, scope=AdjustableContinuousRunningModeData, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningModeData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdjustableContinuousRunningModeData._Automaton = _BuildAutomaton_39()




AdjustableRunningModes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningMode'), AdjustableDiscreteRunningMode, scope=AdjustableRunningModes, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 873, 4)))

AdjustableRunningModes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningMode'), AdjustableContinuousRunningMode, scope=AdjustableRunningModes, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 874, 4)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdjustableRunningModes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningMode')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 873, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdjustableRunningModes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningMode')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 874, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AdjustableRunningModes._Automaton = _BuildAutomaton_40()




FlexibilityRegistration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instructionProcessingDelay'), pyxb.binding.datatypes.duration, scope=FlexibilityRegistration, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 46, 5)))

FlexibilityRegistration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deviceDescription'), DeviceDescription, scope=FlexibilityRegistration, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 47, 5)))

FlexibilityRegistration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currency'), CurrencyType, scope=FlexibilityRegistration, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FlexibilityRegistration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FlexibilityRegistration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionProcessingDelay')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 46, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FlexibilityRegistration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deviceDescription')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 47, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FlexibilityRegistration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FlexibilityRegistration._Automaton = _BuildAutomaton_41()




FlexibilityUpdate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId'), Identifier, scope=FlexibilityUpdate, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5)))

FlexibilityUpdate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validFrom'), pyxb.binding.datatypes.dateTime, scope=FlexibilityUpdate, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FlexibilityUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FlexibilityUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FlexibilityUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FlexibilityUpdate._Automaton = _BuildAutomaton_42()




Instruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instructionId'), Identifier, scope=Instruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 67, 5)))

Instruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId'), Identifier, scope=Instruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 68, 5)))

Instruction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isEmergencyInstruction'), pyxb.binding.datatypes.boolean, scope=Instruction, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 69, 5)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Instruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Instruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 67, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Instruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 68, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Instruction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isEmergencyInstruction')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 69, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Instruction._Automaton = _BuildAutomaton_43()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instructionId'), Identifier, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 79, 6)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), InstructionStatus, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 80, 6)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'debugInformation'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 81, 6)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 81, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 79, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 80, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'debugInformation')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 81, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_44()




def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_45()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instructionId'), Identifier, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 108, 6)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_46()




CurtailmentOption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'curtailmentRange'), CurtailmentRange, scope=CurtailmentOption, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 238, 3)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurtailmentOption._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'curtailmentRange')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 238, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CurtailmentOption._Automaton = _BuildAutomaton_47()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measurementTimestamp'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 257, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electricityMeasurement'), CTD_ANON_6, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 258, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gasMeasurement'), CTD_ANON_7, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 263, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatMeasurement'), CTD_ANON_8, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 268, 6)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 258, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 263, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 268, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measurementTimestamp')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 257, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricityMeasurement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 258, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasMeasurement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 263, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatMeasurement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 268, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_48()




CurtailmentProfile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'curtailmentProfileElement'), CurtailmentProfileElement, scope=CurtailmentProfile, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 331, 3)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurtailmentProfile._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'curtailmentProfileElement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 331, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CurtailmentProfile._Automaton = _BuildAutomaton_49()




def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 293, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 297, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 301, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SequentialProfileAlternative._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 294, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SequentialProfileAlternative._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricityProbabilityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 295, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SequentialProfileAlternative._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 298, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SequentialProfileAlternative._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasProbabilityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 299, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SequentialProfileAlternative._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 302, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SequentialProfileAlternative._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatProbabilityProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 303, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SequentialProfileAlternative._Automaton = _BuildAutomaton_50()




StorageDiscreteRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningModeElement'), CTD_ANON_16, scope=StorageDiscreteRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 585, 5)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageDiscreteRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discreteRunningModeElement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 585, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StorageDiscreteRunningMode._Automaton = _BuildAutomaton_51()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fillingRate'), pyxb.binding.datatypes.double, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 590, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 591, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), pyxb.binding.datatypes.double, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 592, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), pyxb.binding.datatypes.double, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 593, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), pyxb.binding.datatypes.double, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 594, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), pyxb.binding.datatypes.double, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 595, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), pyxb.binding.datatypes.double, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 596, 10)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 591, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 592, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 593, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 594, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 595, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 596, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fillingRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 590, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 591, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 592, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 593, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 594, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 595, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 596, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_52()




StorageContinuousRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningModeElement'), CTD_ANON_17, scope=StorageContinuousRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 621, 5)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageContinuousRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'continuousRunningModeElement')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 621, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StorageContinuousRunningMode._Automaton = _BuildAutomaton_53()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lowerBound'), CTD_ANON_18, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 626, 10)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'upperBound'), CTD_ANON_19, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 633, 10)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lowerBound')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 626, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'upperBound')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 633, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_54()




def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fillingRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 608, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_55()




def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fillingRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 608, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 609, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 610, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 611, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 612, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 613, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 614, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_56()




AdjustableDiscreteRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningCost'), pyxb.binding.datatypes.decimal, scope=AdjustableDiscreteRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 828, 5)))

AdjustableDiscreteRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'electricalPower'), pyxb.binding.datatypes.double, scope=AdjustableDiscreteRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 829, 5)))

AdjustableDiscreteRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate'), pyxb.binding.datatypes.double, scope=AdjustableDiscreteRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 830, 5)))

AdjustableDiscreteRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature'), pyxb.binding.datatypes.double, scope=AdjustableDiscreteRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 831, 5)))

AdjustableDiscreteRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate'), pyxb.binding.datatypes.double, scope=AdjustableDiscreteRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 832, 5)))

AdjustableDiscreteRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower'), pyxb.binding.datatypes.double, scope=AdjustableDiscreteRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 833, 5)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 828, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 829, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 830, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 831, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 832, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 833, 5))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableDiscreteRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 828, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableDiscreteRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 829, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableDiscreteRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 830, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableDiscreteRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 831, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableDiscreteRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 832, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AdjustableDiscreteRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 833, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdjustableDiscreteRunningMode._Automaton = _BuildAutomaton_57()




AdjustableContinuousRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lowerBound'), CTD_ANON_20, scope=AdjustableContinuousRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 852, 5)))

AdjustableContinuousRunningMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'upperBound'), CTD_ANON_21, scope=AdjustableContinuousRunningMode, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 859, 5)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lowerBound')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 852, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdjustableContinuousRunningMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'upperBound')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 859, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AdjustableContinuousRunningMode._Automaton = _BuildAutomaton_58()




def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_59()




def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningCost')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 840, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'electricalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 841, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gasFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 842, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatTemperature')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 843, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatFlowRate')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 844, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heatThermalPower')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 845, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_60()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities'), SupportedCommodities, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 220, 6)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionProcessingDelay')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 46, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deviceDescription')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 47, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 220, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_61()




def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InflexibleUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InflexibleUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InflexibleUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InflexibleUpdate._Automaton = _BuildAutomaton_62()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'curtailmentProfile'), CurtailmentProfile, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 323, 6)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 67, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 68, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isEmergencyInstruction')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 69, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'curtailmentProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 323, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_63()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities'), SupportedCommodities, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 345, 6)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionProcessingDelay')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 46, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deviceDescription')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 47, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 345, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_64()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endBefore'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 380, 6)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfiles'), SequentialProfiles, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 381, 6)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endBefore')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 380, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfiles')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 381, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_65()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileInstructions'), SequentialProfileInstructions, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 404, 6)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 67, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 68, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isEmergencyInstruction')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 69, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequentialProfileInstructions')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 404, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_66()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fillLevelLabel'), pyxb.binding.datatypes.string, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 415, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fillLevelUnit'), pyxb.binding.datatypes.string, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 416, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuators'), Actuators, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 417, 6)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionProcessingDelay')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 46, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deviceDescription')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 47, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fillLevelLabel')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 415, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fillLevelUnit')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 416, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuators')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 417, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_67()




def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StorageUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StorageUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StorageUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StorageUpdate._Automaton = _BuildAutomaton_68()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuatorInstructions'), ActuatorInstructions, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 807, 6)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 67, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 68, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isEmergencyInstruction')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 69, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuatorInstructions')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 807, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_69()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities'), SupportedCommodities, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 818, 6)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionProcessingDelay')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 46, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deviceDescription')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 47, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 48, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supportedCommodities')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 818, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_70()




def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AdjustableUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AdjustableUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdjustableUpdate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AdjustableUpdate._Automaton = _BuildAutomaton_71()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModeId'), pyxb.binding.datatypes.int, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 923, 6)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), STD_ANON_3, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 924, 6)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 932, 6)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 924, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instructionId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 67, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 68, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isEmergencyInstruction')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 69, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModeId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 923, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 924, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startTime')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 932, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_72()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forecastProfiles'), ProfileContainer, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 285, 6)))

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'forecastProfiles')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 285, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_73()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'curtailmentOptions'), CurtailmentOptions, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 312, 6)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 312, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'curtailmentOptions')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 312, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_74()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuatorBehaviours'), ActuatorBehaviours, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 685, 6)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'leakageBehaviour'), LeakageFunction, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 686, 6)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 686, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuatorBehaviours')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 685, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'leakageBehaviour')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 686, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_75()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentFillLevel'), pyxb.binding.datatypes.double, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 735, 6)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuatorStatuses'), ActuatorStatuses, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 736, 6)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 736, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentFillLevel')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 735, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuatorStatuses')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 736, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_76()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'targetProfile'), TargetProfile, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 758, 6)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'targetProfile')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 758, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_77()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usageForecast'), CTD_ANON_11, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 769, 6)))

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usageForecast')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 769, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_78()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModes'), AdjustableRunningModes, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 883, 6)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timers'), Timers, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 884, 6)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transitions'), Transitions, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 885, 6)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 884, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModes')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 883, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timers')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 884, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transitions')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 885, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_79()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentRunningModeId'), pyxb.binding.datatypes.int, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 901, 6)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor'), STD_ANON_2, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 902, 6)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'previousRunningModeId'), pyxb.binding.datatypes.int, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 910, 6)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transitionTimestamp'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 911, 6)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timerUpdates'), TimerUpdates, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 912, 6)))

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 902, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 910, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 911, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flexibilityUpdateId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFrom')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentRunningModeId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 901, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runningModeFactor')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 902, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'previousRunningModeId')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 910, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transitionTimestamp')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 911, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timerUpdates')), pyxb.utils.utility.Location('/usr/local/defpi/resources/xsd/InflexibleControllerEfi20.xsd', 912, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_80()

