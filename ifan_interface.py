
from pymodbus.client.sync import ModbusTcpClient

#Typical Modbus IP stuff; later configure from app
KstrFanIP='192.168.2.16'
KintFanPort=502
KmbUnitID=1

#register holds site name on define PCB (w/ Macro)
import rg


def get_site_id():
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.read_holding_registers(rg.KpcbSiteIDReg,1,unit=KmbUnitID)
    client.close()
    return(result.registers[0])


def set_start_stop(start1):
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.write_register(rg.KpcbRunReg, start1, unit=KmbUnitID)
    print("Set start:\n")
    print(result)
    return(0)


def set_direction(clock1):
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.write_register(rg.KpcbDirReg, clock1, unit=KmbUnitID)
    print('Set Dir:\n')
    print(result)
    return(0)


def set_speed(to):
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.write_register(rg.KpcbSpdReg, to, unit=KmbUnitID)
    print('Set Speed:\n')
    print(result)
    return(0)


def inc_dec_speed(up1):
    client = ModbusTcpClient(KstrFanIP, KintFanPort)
    result = client.read_holding_registers(rg.KpcbSpdReg, 1, unit=KmbUnitID)
    print(result)
    if result.function_code < 0x80:
        current_speed = result.registers[0]

        if up1 == 1:
            current_speed += 1
        else:
            current_speed -= 1
            
        if current_speed > 10:
            current_speed = 10
        elif current_speed < 1:
            current_speed = 1

        result = client.write_register(rg.KpcbSpdReg, current_speed, unit=KmbUnitID)
        print('up dn speed: \n')
        print(result)
        return(0)
    else:
        return(1)


def get_status():

    return(1)



    
        
