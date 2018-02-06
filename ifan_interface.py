
from pymodbus.client.sync import ModbusTcpClient

#Typical Modbus IP stuff; later configure from app
KstrFanIP='192.168.2.16'
KintFanPort=502
KmbUnitID=1

#register holds site name on define PCB (w/ Macro)
KpcbSiteIDReg=6125#16658
KpcbRunReg=5122
KpcbDirReg=5121
KpcbSpdReg=5120


def get_site_id():
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.read_holding_registers(KpcbSiteIDReg,1,unit=KmbUnitID)
    client.close()
    return(result.registers[0])


def set_start_stop(start1):
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.write_register(KpcbRunReg, start1, unit=KmbUnitID)
    print("Set start:\n")
    print(result)
    return(0)


def set_direction(clock1):
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.write_register(KpcbDirReg, clock1, unit=KmbUnitID)
    print('Set Dir:\n')
    print(result)
    return(0)

def set_speed(to):
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.write_register(KpcbSpdReg, to, unit=KmbUnitID)
    print('Set Speed:\n')
    print(result)
    return(0)


