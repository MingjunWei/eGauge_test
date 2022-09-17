# !!! DO NOT EDIT !!!  Generated by gen-phys-units.
#
#   Released under MIT license.
#   See file LICENSE for details.
#
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-locals

from enum import Enum

from .physical_units import AlternateUnit, PhysicalUnits, \
    PhysicalUnitConversion, PrimaryUnit

class UnitSystem(Enum):
    METRIC = 0
    IMPERIAL = 1

METRIC = 0	# for backwards compatibility (use UnitSystem instead)
IMPERIAL = 1	# for backwards compatibility (use UnitSystem instead)

class RegisterType(Enum):
    POWER = "P"
    APPARENT_POWER = "S"
    VOLTAGE = "V"
    CURRENT = "I"
    FREQ = "F"
    THD = "THD"
    TEMP = "T"
    FLOW = "Q"
    SPEED = "v"
    NUMBER = "#"
    RESISTANCE = "R"
    IRRADIANCE = "Ee"
    REACTIVE_POWER = "PQ"
    MONEY = "$"
    ANGLE = "a"
    HUMIDITY = "h"
    FLOWVOL = "Qv"
    PRESSURE = "Pa"
    CHARGE = "Qe"
    VOLTAGE_MEAN = "Vdc"
    CURRENT_MEAN = "Idc"
    MASS = "m"
    FIXED3 = "#3"
    AIR_QUALITY = "aq"
    PERCENTAGE = "%"
    PPM = "ppm"
    DISCRETE = "d"
    TEMP_DIFF = "dT"

def _create_units():
    pus = PhysicalUnits()

    p0 = PrimaryUnit("W", "Power")
    pus.add(p0)
    pus.add_scaled(p0, "yW", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p0, "zW", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p0, "aW", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p0, "fW", 999999999999999.88, "femto")
    pus.add_scaled(p0, "pW", 1000000000000, "pico")
    pus.add_scaled(p0, "nW", 999999999.99999988, "nano")
    pus.add_scaled(p0, "μW", 1000000, "micro")
    pus.add_scaled(p0, "mW", 1000, "milli")
    pus.add_scaled(p0, "kW", 0.001, "kilo")
    pus.add_scaled(p0, "MW", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p0, "GW", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p0, "TW", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p0, "PW", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p0, "EW", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p0, "ZW", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p0, "YW", 1.0000000000000001e-24, "yotta")

    p1 = PrimaryUnit("VA", "Apparent Power")
    pus.add(p1)
    pus.add_scaled(p1, "yVA", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p1, "zVA", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p1, "aVA", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p1, "fVA", 999999999999999.88, "femto")
    pus.add_scaled(p1, "pVA", 1000000000000, "pico")
    pus.add_scaled(p1, "nVA", 999999999.99999988, "nano")
    pus.add_scaled(p1, "μVA", 1000000, "micro")
    pus.add_scaled(p1, "mVA", 1000, "milli")
    pus.add_scaled(p1, "kVA", 0.001, "kilo")
    pus.add_scaled(p1, "MVA", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p1, "GVA", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p1, "TVA", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p1, "PVA", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p1, "EVA", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p1, "ZVA", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p1, "YVA", 1.0000000000000001e-24, "yotta")

    p2 = PrimaryUnit("V", "Voltage")
    pus.add(p2)
    pus.add_scaled(p2, "yV", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p2, "zV", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p2, "aV", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p2, "fV", 999999999999999.88, "femto")
    pus.add_scaled(p2, "pV", 1000000000000, "pico")
    pus.add_scaled(p2, "nV", 999999999.99999988, "nano")
    pus.add_scaled(p2, "μV", 1000000, "micro")
    pus.add_scaled(p2, "mV", 1000, "milli")
    pus.add_scaled(p2, "kV", 0.001, "kilo")
    pus.add_scaled(p2, "MV", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p2, "GV", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p2, "TV", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p2, "PV", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p2, "EV", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p2, "ZV", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p2, "YV", 1.0000000000000001e-24, "yotta")

    p3 = PrimaryUnit("A", "Current")
    pus.add(p3)
    pus.add_scaled(p3, "yA", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p3, "zA", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p3, "aA", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p3, "fA", 999999999999999.88, "femto")
    pus.add_scaled(p3, "pA", 1000000000000, "pico")
    pus.add_scaled(p3, "nA", 999999999.99999988, "nano")
    pus.add_scaled(p3, "μA", 1000000, "micro")
    pus.add_scaled(p3, "mA", 1000, "milli")
    pus.add_scaled(p3, "kA", 0.001, "kilo")
    pus.add_scaled(p3, "MA", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p3, "GA", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p3, "TA", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p3, "PA", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p3, "EA", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p3, "ZA", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p3, "YA", 1.0000000000000001e-24, "yotta")

    p4 = PrimaryUnit("Hz", "Frequency")
    pus.add(p4)
    pus.add_scaled(p4, "yHz", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p4, "zHz", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p4, "aHz", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p4, "fHz", 999999999999999.88, "femto")
    pus.add_scaled(p4, "pHz", 1000000000000, "pico")
    pus.add_scaled(p4, "nHz", 999999999.99999988, "nano")
    pus.add_scaled(p4, "μHz", 1000000, "micro")
    pus.add_scaled(p4, "mHz", 1000, "milli")
    pus.add_scaled(p4, "kHz", 0.001, "kilo")
    pus.add_scaled(p4, "MHz", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p4, "GHz", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p4, "THz", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p4, "PHz", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p4, "EHz", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p4, "ZHz", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p4, "YHz", 1.0000000000000001e-24, "yotta")

    p5 = PrimaryUnit("Hz·s")
    pus.add(p5)

    p6 = PrimaryUnit("%", "THD")
    pus.add(p6)

    p7 = PrimaryUnit("%·s")
    pus.add(p7)

    p8 = PrimaryUnit("°C", "Temperature")
    pus.add(p8)

    p9 = PrimaryUnit("°C·s")
    pus.add(p9)
    pus.add_scaled(p9, "°C·h", 0.00027777777777777778, "Celsius degree hours")
    pus.add_scaled(p9, "°C·d", 1.1574074074074073e-05, "Celsius degree days")

    p10 = PrimaryUnit("g/s", "Mass flow")
    pus.add(p10)
    pus.add_scaled(p10, "μg/s", 1000000)
    pus.add_scaled(p10, "mg/s", 1000)
    pus.add_scaled(p10, "kg/s", 0.001)
    pus.add_scaled(p10, "T/s", 9.9999999999999995e-07)
    pus.add_scaled(p10, "kT/s", 1.0000000000000001e-09)
    pus.add_scaled(p10, "MT/s", 9.9999999999999998e-13)
    pus.add_scaled(p10, "GT/s", 1.0000000000000001e-15)
    pus.add_scaled(p10, "TT/s", 1.0000000000000001e-18)
    pus.add_scaled(p10, "PT/s", 9.9999999999999991e-22)

    p11 = PrimaryUnit("m/s", "Speed")
    pus.add(p11)
    pus.add_scaled(p11, "ym/s", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p11, "zm/s", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p11, "am/s", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p11, "fm/s", 999999999999999.88, "femto")
    pus.add_scaled(p11, "pm/s", 1000000000000, "pico")
    pus.add_scaled(p11, "nm/s", 999999999.99999988, "nano")
    pus.add_scaled(p11, "μm/s", 1000000, "micro")
    pus.add_scaled(p11, "mm/s", 1000, "milli")
    pus.add_scaled(p11, "km/s", 0.001, "kilo")
    pus.add_scaled(p11, "Mm/s", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p11, "Gm/s", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p11, "Tm/s", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p11, "Pm/s", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p11, "Em/s", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p11, "Zm/s", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p11, "Ym/s", 1.0000000000000001e-24, "yotta")

    p12 = PrimaryUnit("m")
    pus.add(p12)
    pus.add_scaled(p12, "ym", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p12, "zm", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p12, "am", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p12, "fm", 999999999999999.88, "femto")
    pus.add_scaled(p12, "pm", 1000000000000, "pico")
    pus.add_scaled(p12, "nm", 999999999.99999988, "nano")
    pus.add_scaled(p12, "μm", 1000000, "micro")
    pus.add_scaled(p12, "mm", 1000, "milli")
    pus.add_scaled(p12, "km", 0.001, "kilo")
    pus.add_scaled(p12, "Mm", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p12, "Gm", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p12, "Tm", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p12, "Pm", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p12, "Em", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p12, "Zm", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p12, "Ym", 1.0000000000000001e-24, "yotta")

    p13 = PrimaryUnit("", "Whole number")
    pus.add(p13)

    p14 = PrimaryUnit("s")
    pus.add(p14)

    p15 = PrimaryUnit("Ω", "Resistance")
    pus.add(p15)
    pus.add_scaled(p15, "yΩ", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p15, "zΩ", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p15, "aΩ", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p15, "fΩ", 999999999999999.88, "femto")
    pus.add_scaled(p15, "pΩ", 1000000000000, "pico")
    pus.add_scaled(p15, "nΩ", 999999999.99999988, "nano")
    pus.add_scaled(p15, "μΩ", 1000000, "micro")
    pus.add_scaled(p15, "mΩ", 1000, "milli")
    pus.add_scaled(p15, "kΩ", 0.001, "kilo")
    pus.add_scaled(p15, "MΩ", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p15, "GΩ", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p15, "TΩ", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p15, "PΩ", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p15, "EΩ", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p15, "ZΩ", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p15, "YΩ", 1.0000000000000001e-24, "yotta")

    p16 = PrimaryUnit("Ω·s")
    pus.add(p16)

    p17 = PrimaryUnit("W/m^2", "Irradiance")
    pus.add(p17)
    pus.add_scaled(p17, "yW/m^2", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p17, "zW/m^2", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p17, "aW/m^2", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p17, "fW/m^2", 999999999999999.88, "femto")
    pus.add_scaled(p17, "pW/m^2", 1000000000000, "pico")
    pus.add_scaled(p17, "nW/m^2", 999999999.99999988, "nano")
    pus.add_scaled(p17, "μW/m^2", 1000000, "micro")
    pus.add_scaled(p17, "mW/m^2", 1000, "milli")
    pus.add_scaled(p17, "kW/m^2", 0.001, "kilo")
    pus.add_scaled(p17, "MW/m^2", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p17, "GW/m^2", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p17, "TW/m^2", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p17, "PW/m^2", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p17, "EW/m^2", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p17, "ZW/m^2", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p17, "YW/m^2", 1.0000000000000001e-24, "yotta")

    p18 = PrimaryUnit("var", "Reactive Power")
    pus.add(p18)
    pus.add_scaled(p18, "yvar", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(p18, "zvar", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(p18, "avar", 9.9999999999999987e+17, "atto")
    pus.add_scaled(p18, "fvar", 999999999999999.88, "femto")
    pus.add_scaled(p18, "pvar", 1000000000000, "pico")
    pus.add_scaled(p18, "nvar", 999999999.99999988, "nano")
    pus.add_scaled(p18, "μvar", 1000000, "micro")
    pus.add_scaled(p18, "mvar", 1000, "milli")
    pus.add_scaled(p18, "kvar", 0.001, "kilo")
    pus.add_scaled(p18, "Mvar", 9.9999999999999995e-07, "mega")
    pus.add_scaled(p18, "Gvar", 1.0000000000000001e-09, "giga")
    pus.add_scaled(p18, "Tvar", 9.9999999999999998e-13, "tera")
    pus.add_scaled(p18, "Pvar", 1.0000000000000001e-15, "peta")
    pus.add_scaled(p18, "Evar", 1.0000000000000001e-18, "exa")
    pus.add_scaled(p18, "Zvar", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(p18, "Yvar", 1.0000000000000001e-24, "yotta")

    p19 = PrimaryUnit("${currency}/s", "Monetary")
    pus.add(p19)

    p20 = PrimaryUnit("${currency}")
    pus.add(p20)

    p21 = PrimaryUnit("°", "Angle")
    pus.add(p21)

    p22 = PrimaryUnit("°·s")
    pus.add(p22)

    p23 = PrimaryUnit("m^3/s", "Volumetric flow")
    pus.add(p23)

    p24 = PrimaryUnit("Pa", "Pressure")
    pus.add(p24)

    p25 = PrimaryUnit("Pa·s")
    pus.add(p25)

    p26 = PrimaryUnit("Ah·s")
    pus.add(p26)

    p27 = PrimaryUnit("g", "Mass")
    pus.add(p27)
    pus.add_scaled(p27, "μg", 1000000, "microgram")
    pus.add_scaled(p27, "mg", 1000, "milligram")
    pus.add_scaled(p27, "kg", 0.001, "kilogram")

    p28 = PrimaryUnit("g·s")
    pus.add(p28)
    pus.add_scaled(p28, "μg·s", 1000000)
    pus.add_scaled(p28, "mg·s", 1000)
    pus.add_scaled(p28, "kg·s", 0.001)
    pus.add_scaled(p28, "T·s", 9.9999999999999995e-07)
    pus.add_scaled(p28, "kT·s", 1.0000000000000001e-09)
    pus.add_scaled(p28, "MT·s", 9.9999999999999998e-13)
    pus.add_scaled(p28, "GT·s", 1.0000000000000001e-15)
    pus.add_scaled(p28, "TT·s", 1.0000000000000001e-18)
    pus.add_scaled(p28, "PT·s", 9.9999999999999991e-22)

    p29 = PrimaryUnit("ppm", "Parts per million")
    pus.add(p29)

    p30 = PrimaryUnit("ppm·s")
    pus.add(p30)

    p31 = PrimaryUnit("A·s")
    pus.add(p31)

    c2 = PhysicalUnitConversion(False,
        lambda x, t=None: (1/3600)*x,
        lambda x, t=None: 3600*x
    )
    au = AlternateUnit("Ah", p31, c2)
    pus.add(au)
    pus.add_scaled(au, "yAh", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(au, "zAh", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(au, "aAh", 9.9999999999999987e+17, "atto")
    pus.add_scaled(au, "fAh", 999999999999999.88, "femto")
    pus.add_scaled(au, "pAh", 1000000000000, "pico")
    pus.add_scaled(au, "nAh", 999999999.99999988, "nano")
    pus.add_scaled(au, "μAh", 1000000, "micro")
    pus.add_scaled(au, "mAh", 1000, "milli")
    pus.add_scaled(au, "kAh", 0.001, "kilo")
    pus.add_scaled(au, "MAh", 9.9999999999999995e-07, "mega")
    pus.add_scaled(au, "GAh", 1.0000000000000001e-09, "giga")
    pus.add_scaled(au, "TAh", 9.9999999999999998e-13, "tera")
    pus.add_scaled(au, "PAh", 1.0000000000000001e-15, "peta")
    pus.add_scaled(au, "EAh", 1.0000000000000001e-18, "exa")
    pus.add_scaled(au, "ZAh", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(au, "YAh", 1.0000000000000001e-24, "yotta")

    c9 = PhysicalUnitConversion(False,
        lambda x, t=None: (1/100)*x,
        lambda x, t=None: 100*x
    )
    au = AlternateUnit("hPa", p24, c9)
    pus.add(au)

    c10 = PhysicalUnitConversion(False,
        lambda x, t=None: 1.0e-5*x,
        lambda x, t=None: 100000.0*x
    )
    au = AlternateUnit("bar", p24, c10)
    pus.add(au)

    c11 = PhysicalUnitConversion(False,
        lambda x, t=None: 0.00014503773773*x,
        lambda x, t=None: 6894.7572931783*x
    )
    au = AlternateUnit("psi", p24, c11)
    pus.add(au)

    c12 = PhysicalUnitConversion(False,
        lambda x, t=None: 0.000295300999981497*x,
        lambda x, t=None: 3386.375258*x
    )
    au = AlternateUnit("inHg", p24, c12)
    pus.add(au)
    au = AlternateUnit("psi·s", p25, c11)
    pus.add(au)
    au = AlternateUnit("inHg·s", p25, c12)
    pus.add(au)

    p32 = PrimaryUnit("VA·s")
    pus.add(p32)
    au = AlternateUnit("VAh", p32, c2)
    pus.add(au)
    pus.add_scaled(au, "yVAh", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(au, "zVAh", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(au, "aVAh", 9.9999999999999987e+17, "atto")
    pus.add_scaled(au, "fVAh", 999999999999999.88, "femto")
    pus.add_scaled(au, "pVAh", 1000000000000, "pico")
    pus.add_scaled(au, "nVAh", 999999999.99999988, "nano")
    pus.add_scaled(au, "μVAh", 1000000, "micro")
    pus.add_scaled(au, "mVAh", 1000, "milli")
    pus.add_scaled(au, "kVAh", 0.001, "kilo")
    pus.add_scaled(au, "MVAh", 9.9999999999999995e-07, "mega")
    pus.add_scaled(au, "GVAh", 1.0000000000000001e-09, "giga")
    pus.add_scaled(au, "TVAh", 9.9999999999999998e-13, "tera")
    pus.add_scaled(au, "PVAh", 1.0000000000000001e-15, "peta")
    pus.add_scaled(au, "EVAh", 1.0000000000000001e-18, "exa")
    pus.add_scaled(au, "ZVAh", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(au, "YVAh", 1.0000000000000001e-24, "yotta")

    p33 = PrimaryUnit("V·s")
    pus.add(p33)
    au = AlternateUnit("Vh", p33, c2)
    pus.add(au)
    pus.add_scaled(au, "yVh", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(au, "zVh", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(au, "aVh", 9.9999999999999987e+17, "atto")
    pus.add_scaled(au, "fVh", 999999999999999.88, "femto")
    pus.add_scaled(au, "pVh", 1000000000000, "pico")
    pus.add_scaled(au, "nVh", 999999999.99999988, "nano")
    pus.add_scaled(au, "μVh", 1000000, "micro")
    pus.add_scaled(au, "mVh", 1000, "milli")
    pus.add_scaled(au, "kVh", 0.001, "kilo")
    pus.add_scaled(au, "MVh", 9.9999999999999995e-07, "mega")
    pus.add_scaled(au, "GVh", 1.0000000000000001e-09, "giga")
    pus.add_scaled(au, "TVh", 9.9999999999999998e-13, "tera")
    pus.add_scaled(au, "PVh", 1.0000000000000001e-15, "peta")
    pus.add_scaled(au, "EVh", 1.0000000000000001e-18, "exa")
    pus.add_scaled(au, "ZVh", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(au, "YVh", 1.0000000000000001e-24, "yotta")

    c0 = PhysicalUnitConversion(False,
        lambda x, t=None: 0.00135962115516133*x,
        lambda x, t=None: 735.499*x
    )
    au = AlternateUnit("hp", p0, c0)
    pus.add(au)

    c1 = PhysicalUnitConversion(False,
        lambda x, t=None: 3.412141633*x,
        lambda x, t=None: 0.293071070183211*x
    )
    au = AlternateUnit("Btu/h", p0, c1)
    pus.add(au)
    pus.add_scaled(au, "MBH", 0.001)

    p34 = PrimaryUnit("W·s")
    pus.add(p34)
    au = AlternateUnit("Wh", p34, c2)
    pus.add(au)
    pus.add_scaled(au, "yWh", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(au, "zWh", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(au, "aWh", 9.9999999999999987e+17, "atto")
    pus.add_scaled(au, "fWh", 999999999999999.88, "femto")
    pus.add_scaled(au, "pWh", 1000000000000, "pico")
    pus.add_scaled(au, "nWh", 999999999.99999988, "nano")
    pus.add_scaled(au, "μWh", 1000000, "micro")
    pus.add_scaled(au, "mWh", 1000, "milli")
    pus.add_scaled(au, "kWh", 0.001, "kilo")
    pus.add_scaled(au, "MWh", 9.9999999999999995e-07, "mega")
    pus.add_scaled(au, "GWh", 1.0000000000000001e-09, "giga")
    pus.add_scaled(au, "TWh", 9.9999999999999998e-13, "tera")
    pus.add_scaled(au, "PWh", 1.0000000000000001e-15, "peta")
    pus.add_scaled(au, "EWh", 1.0000000000000001e-18, "exa")
    pus.add_scaled(au, "ZWh", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(au, "YWh", 1.0000000000000001e-24, "yotta")

    c3 = PhysicalUnitConversion(False,
        lambda x, t=None: x,
        lambda x, t=None: x
    )
    au = AlternateUnit("J", p34, c3)
    pus.add(au)

    c4 = PhysicalUnitConversion(False,
        lambda x, t=None: 0.000947817077749151*x,
        lambda x, t=None: 1055.0559*x
    )
    au = AlternateUnit("Btu", p34, c4)
    pus.add(au)

    p35 = PrimaryUnit("W·s/m^2")
    pus.add(p35)
    au = AlternateUnit("Wh/m^2", p35, c2)
    pus.add(au)
    pus.add_scaled(au, "yWh/m^2", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(au, "zWh/m^2", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(au, "aWh/m^2", 9.9999999999999987e+17, "atto")
    pus.add_scaled(au, "fWh/m^2", 999999999999999.88, "femto")
    pus.add_scaled(au, "pWh/m^2", 1000000000000, "pico")
    pus.add_scaled(au, "nWh/m^2", 999999999.99999988, "nano")
    pus.add_scaled(au, "μWh/m^2", 1000000, "micro")
    pus.add_scaled(au, "mWh/m^2", 1000, "milli")
    pus.add_scaled(au, "kWh/m^2", 0.001, "kilo")
    pus.add_scaled(au, "MWh/m^2", 9.9999999999999995e-07, "mega")
    pus.add_scaled(au, "GWh/m^2", 1.0000000000000001e-09, "giga")
    pus.add_scaled(au, "TWh/m^2", 9.9999999999999998e-13, "tera")
    pus.add_scaled(au, "PWh/m^2", 1.0000000000000001e-15, "peta")
    pus.add_scaled(au, "EWh/m^2", 1.0000000000000001e-18, "exa")
    pus.add_scaled(au, "ZWh/m^2", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(au, "YWh/m^2", 1.0000000000000001e-24, "yotta")

    c18 = PhysicalUnitConversion(False,
        lambda x, t=None: 0.00220462*x,
        lambda x, t=None: 453.59290943564*x
    )
    au = AlternateUnit("lbs", p27, c18)
    pus.add(au)

    c19 = PhysicalUnitConversion(False,
        lambda x, t=None: 1.0e-6*x,
        lambda x, t=None: 1000000.0*x
    )
    au = AlternateUnit("T", p27, c19)
    pus.add(au)
    pus.add_scaled(au, "kT", 0.001, "kiloton")
    pus.add_scaled(au, "MT", 9.9999999999999995e-07, "megaton")
    pus.add_scaled(au, "GT", 1.0000000000000001e-09, "gigaton")
    pus.add_scaled(au, "TT", 9.9999999999999998e-13, "teraton")
    pus.add_scaled(au, "PT", 1.0000000000000001e-15, "petaton")
    au = AlternateUnit("lbs/s", p10, c18)
    pus.add(au)
    au = AlternateUnit("lbs·s", p28, c18)
    pus.add(au)

    c15 = PhysicalUnitConversion(False,
        lambda x, t=None: 1.09361329833771*x,
        lambda x, t=None: 0.9144*x
    )
    au = AlternateUnit("yd", p12, c15)
    pus.add(au)

    c16 = PhysicalUnitConversion(False,
        lambda x, t=None: 3.28083989501312*x,
        lambda x, t=None: 0.3048*x
    )
    au = AlternateUnit("ft", p12, c16)
    pus.add(au)

    c17 = PhysicalUnitConversion(False,
        lambda x, t=None: 0.000621371192237334*x,
        lambda x, t=None: 1609.344*x
    )
    au = AlternateUnit("mi", p12, c17)
    pus.add(au)

    c13 = PhysicalUnitConversion(False,
        lambda x, t=None: 3600*x,
        lambda x, t=None: (1/3600)*x
    )
    au = AlternateUnit("m/h", p11, c13)
    pus.add(au)
    pus.add_scaled(au, "ym/h", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(au, "zm/h", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(au, "am/h", 9.9999999999999987e+17, "atto")
    pus.add_scaled(au, "fm/h", 999999999999999.88, "femto")
    pus.add_scaled(au, "pm/h", 1000000000000, "pico")
    pus.add_scaled(au, "nm/h", 999999999.99999988, "nano")
    pus.add_scaled(au, "μm/h", 1000000, "micro")
    pus.add_scaled(au, "mm/h", 1000, "milli")
    pus.add_scaled(au, "km/h", 0.001, "kilo")
    pus.add_scaled(au, "Mm/h", 9.9999999999999995e-07, "mega")
    pus.add_scaled(au, "Gm/h", 1.0000000000000001e-09, "giga")
    pus.add_scaled(au, "Tm/h", 9.9999999999999998e-13, "tera")
    pus.add_scaled(au, "Pm/h", 1.0000000000000001e-15, "peta")
    pus.add_scaled(au, "Em/h", 1.0000000000000001e-18, "exa")
    pus.add_scaled(au, "Zm/h", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(au, "Ym/h", 1.0000000000000001e-24, "yotta")

    c14 = PhysicalUnitConversion(False,
        lambda x, t=None: 2.2369362920544*x,
        lambda x, t=None: 0.44704*x
    )
    au = AlternateUnit("mph", p11, c14)
    pus.add(au)

    p36 = PrimaryUnit("m^3")
    pus.add(p36)

    c20 = PhysicalUnitConversion(False,
        lambda x, t=None: 1000.0*x,
        lambda x, t=None: 0.001*x
    )
    au = AlternateUnit("L", p36, c20)
    pus.add(au)

    c23 = PhysicalUnitConversion(False,
        lambda x, t=None: 264.200792602378*x,
        lambda x, t=None: 0.003785*x
    )
    au = AlternateUnit("gal", p36, c23)
    pus.add(au)
    au = AlternateUnit("L/s", p23, c20)
    pus.add(au)

    c21 = PhysicalUnitConversion(False,
        lambda x, t=None: 60000.0*x,
        lambda x, t=None: 1.66666666666667e-5*x
    )
    au = AlternateUnit("L/m", p23, c21)
    pus.add(au)

    c22 = PhysicalUnitConversion(False,
        lambda x, t=None: 3600000.0*x,
        lambda x, t=None: 2.77777777777778e-7*x
    )
    au = AlternateUnit("L/h", p23, c22)
    pus.add(au)
    au = AlternateUnit("gal/s", p23, c23)
    pus.add(au)

    c24 = PhysicalUnitConversion(False,
        lambda x, t=None: 15852.0475561427*x,
        lambda x, t=None: 6.30833333333334e-5*x
    )
    au = AlternateUnit("gpm", p23, c24)
    pus.add(au)

    c25 = PhysicalUnitConversion(False,
        lambda x, t=None: 951122.85336856*x,
        lambda x, t=None: 1.05138888888889e-6*x
    )
    au = AlternateUnit("gph", p23, c25)
    pus.add(au)

    p37 = PrimaryUnit("m·s")
    pus.add(p37)
    au = AlternateUnit("ft·s", p37, c16)
    pus.add(au)

    p38 = PrimaryUnit("var·s")
    pus.add(p38)
    au = AlternateUnit("vahr", p38, c2)
    pus.add(au)
    pus.add_scaled(au, "yvahr", 1.0000000000000001e+24, "yocto")
    pus.add_scaled(au, "zvahr", 1.0000000000000001e+21, "zepto")
    pus.add_scaled(au, "avahr", 9.9999999999999987e+17, "atto")
    pus.add_scaled(au, "fvahr", 999999999999999.88, "femto")
    pus.add_scaled(au, "pvahr", 1000000000000, "pico")
    pus.add_scaled(au, "nvahr", 999999999.99999988, "nano")
    pus.add_scaled(au, "μvahr", 1000000, "micro")
    pus.add_scaled(au, "mvahr", 1000, "milli")
    pus.add_scaled(au, "kvahr", 0.001, "kilo")
    pus.add_scaled(au, "Mvahr", 9.9999999999999995e-07, "mega")
    pus.add_scaled(au, "Gvahr", 1.0000000000000001e-09, "giga")
    pus.add_scaled(au, "Tvahr", 9.9999999999999998e-13, "tera")
    pus.add_scaled(au, "Pvahr", 1.0000000000000001e-15, "peta")
    pus.add_scaled(au, "Evahr", 1.0000000000000001e-18, "exa")
    pus.add_scaled(au, "Zvahr", 9.9999999999999991e-22, "zetta")
    pus.add_scaled(au, "Yvahr", 1.0000000000000001e-24, "yotta")

    c5 = PhysicalUnitConversion(False,
        lambda x, t=None: (9/5)*x + 32,
        lambda x, t=None: (5/9)*x - 160/9,
        lambda x, t=None: (9/5)*x,
        lambda y, t=None: (5/9)*y
    )
    au = AlternateUnit("°F", p8, c5)
    pus.add(au)

    c6 = PhysicalUnitConversion(False,
        lambda x, t=None: x + 273.15,
        lambda x, t=None: x - 273.15,
        lambda x, t=None: x,
        lambda y, t=None: y
    )
    au = AlternateUnit("°K", p8, c6)
    pus.add(au)

    c7 = PhysicalUnitConversion(True,
        lambda x, t=None: 273.15*t + x,
        lambda x, t=None: -273.15*t + x,
        lambda x, t=None: x,
        lambda y, t=None: y
    )
    au = AlternateUnit("°K·s", p9, c7)
    pus.add(au)
    pus.add_scaled(au, "°K·h", 0.00027777777777777778, "Kelvin degree hours")
    pus.add_scaled(au, "°K·d", 1.1574074074074073e-05, "Kelvin degree days")

    c8 = PhysicalUnitConversion(True,
        lambda x, t=None: 32*t + (9/5)*x,
        lambda x, t=None: -160/9*t + (5/9)*x,
        lambda x, t=None: (9/5)*x,
        lambda y, t=None: (5/9)*y
    )
    au = AlternateUnit("°F·s", p9, c8)
    pus.add(au)
    pus.add_scaled(au, "°F·h", 0.00027777777777777778, "Fahrenheight degree hours")
    pus.add_scaled(au, "°F·d", 1.1574074074074073e-05, "Fahrenheit degree days")

    return pus

class UnitTableEntry:
    def __init__(self, fix_scale=None, rate_unit=None,
                 cumul_scale=None, cumul_unit=None,
                 name=None):
        self.fix_scale = fix_scale
        self.rate_unit = rate_unit
        self.cumul_scale = cumul_scale
        self.cumul_unit = cumul_unit
        self.name = name

class ConversionTableEntry:
    def __init__(self, unit=None, time_dependent=False,
                 calc=None, inverse=None):
        self.unit = unit
        self.time_dependent = time_dependent
        self.calc = calc
        self.inverse = inverse

class Units:

    # Preferred units for METRIC and IMPERIAL systems:
    preferred = [
        ['kW', 'kWh', 'kVA', 'kVAh', 'kvar', 'kvahr', 'kg', 'kg/s',
         'kWh/m^2', 'km/h', 'hPa', 'Ah', 'Vh', 'L/m', 'L', '°C',
         '°C·d'],
        ['kW', 'kWh', 'kVA', 'kVAh', 'kvar', 'kvahr', 'lbs', 'lbs/s',
         'kWh/m^2', 'mph', 'inHg', 'Ah', 'Vh', 'ft', '°F', '°F·d',
         'lbs·s', 'inHg·s', 'ft·s', 'gpm', 'gal']
    ]

    table = {
        'P': UnitTableEntry(fix_scale=1, rate_unit='W',
                            cumul_scale=1 / 3600000, cumul_unit='kWh',
                            name='Power'),
        'S': UnitTableEntry(fix_scale=1, rate_unit='VA',
                            cumul_scale=1 / 3600000, cumul_unit='kVAh',
                            name='Apparent Power'),
        'V': UnitTableEntry(fix_scale=1000, rate_unit='V',
                            cumul_scale=1 / 3600000, cumul_unit='Vh',
                            name='Voltage'),
        'I': UnitTableEntry(fix_scale=1000, rate_unit='A',
                            cumul_scale=1 / 3600000, cumul_unit='Ah',
                            name='Current'),
        'F': UnitTableEntry(fix_scale=1000, rate_unit='Hz',
                            cumul_scale=1 / 1000, cumul_unit='Hz·s',
                            name='Frequency'),
        'THD': UnitTableEntry(fix_scale=1000, rate_unit='%',
                              cumul_scale=1 / 1000, cumul_unit='%·s',
                              name='THD'),
        'T': UnitTableEntry(fix_scale=1000, rate_unit='°C',
                            cumul_scale=1 / 1000, cumul_unit='°C·s',
                            name='Temperature'),
        'Q': UnitTableEntry(fix_scale=1, rate_unit='g/s',
                            cumul_scale=1 / 1000, cumul_unit='kg',
                            name='Mass flow'),
        'v': UnitTableEntry(fix_scale=1000, rate_unit='m/s',
                            cumul_scale=1 / 1000, cumul_unit='m',
                            name='Speed'),
        '#': UnitTableEntry(fix_scale=1, rate_unit='',
                            cumul_scale=1, cumul_unit='s',
                            name='Whole number'),
        'R': UnitTableEntry(fix_scale=1, rate_unit='Ω',
                            cumul_scale=1, cumul_unit='Ω·s',
                            name='Resistance'),
        'Ee': UnitTableEntry(fix_scale=1, rate_unit='W/m^2',
                             cumul_scale=1 / 3600000, cumul_unit='kWh/m^2',
                             name='Irradiance'),
        'PQ': UnitTableEntry(fix_scale=1, rate_unit='var',
                             cumul_scale=1 / 3600000, cumul_unit='kvahr',
                             name='Reactive Power'),
        '$': UnitTableEntry(fix_scale=536870912, rate_unit='${currency}/s',
                            cumul_scale=1 / 536870912, cumul_unit='${currency}',
                            name='Monetary'),
        'a': UnitTableEntry(fix_scale=1000, rate_unit='°',
                            cumul_scale=1 / 1000, cumul_unit='°·s',
                            name='Angle'),
        'h': UnitTableEntry(fix_scale=1000, rate_unit='%',
                            cumul_scale=1 / 1000, cumul_unit='%·s',
                            name='Humidity'),
        'Qv': UnitTableEntry(fix_scale=1000000000, rate_unit='m^3/s',
                             cumul_scale=1 / 1000000, cumul_unit='L',
                             name='Volumetric flow'),
        'Pa': UnitTableEntry(fix_scale=1, rate_unit='Pa',
                             cumul_scale=1, cumul_unit='Pa·s',
                             name='Pressure'),
        'Qe': UnitTableEntry(fix_scale=1000, rate_unit='Ah',
                             cumul_scale=1 / 1000, cumul_unit='Ah·s',
                             name='Charge'),
        'Vdc': UnitTableEntry(fix_scale=1000, rate_unit='V',
                              cumul_scale=1 / 3600000, cumul_unit='Vh',
                              name='Voltage (mean)'),
        'Idc': UnitTableEntry(fix_scale=1000, rate_unit='A',
                              cumul_scale=1 / 3600000, cumul_unit='Ah',
                              name='Current (mean)'),
        'm': UnitTableEntry(fix_scale=1000, rate_unit='g',
                            cumul_scale=1 / 1000, cumul_unit='g·s',
                            name='Mass'),
        '#3': UnitTableEntry(fix_scale=1000, rate_unit='',
                             cumul_scale=1 / 1000, cumul_unit='s',
                             name='Number with 3 decimals'),
        'aq': UnitTableEntry(fix_scale=1000, rate_unit='',
                             cumul_scale=1 / 1000, cumul_unit='s',
                             name='Air Quality Index (0=good, 500=bad)'),
        '%': UnitTableEntry(fix_scale=1000, rate_unit='%',
                            cumul_scale=1 / 1000, cumul_unit='%·s',
                            name='Percentage'),
        'ppm': UnitTableEntry(fix_scale=1000, rate_unit='ppm',
                              cumul_scale=1 / 1000, cumul_unit='ppm·s',
                              name='Parts per million'),
        'd': UnitTableEntry(fix_scale=1, rate_unit='',
                            cumul_scale=1, cumul_unit='',
                            name='Discrete number'),
        'dT': UnitTableEntry(fix_scale=1000, rate_unit='°C',
                             cumul_scale=1 / 1000, cumul_unit='°C·s',
                             name='Temperature difference'),
    }

    units = _create_units()
