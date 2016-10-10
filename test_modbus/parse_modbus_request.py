import struct
from actionTable import ledDic
from actionTable import eyeemotionDict
from actionTable import actionDict
from actionTable import actioncatgoryDict
from actionTable import SlaveIdDict
from actionTable import FunCodeDict
from actionTable import RegisterBlockDict
from actionTable import StateBlockDict


def parse_modbus_request(requestpdu):
    modbus_request = requestpdu[1]
    (slaveid, funcode) = struct.unpack('>BB', modbus_request[0:2])  # 拆包结果是个tuple
    (regaddress, ) = struct.unpack('>H', modbus_request[2:4])  # 拆包结果是个tuple
    (blockaddress, ) = struct.unpack('>B', modbus_request[2:3])  # 拆包结果是个tuple
    # print(modbus_request)
    # print(hex(regaddress))
    print("发给", SlaveIdDict[slaveid], FunCodeDict[funcode], RegisterBlockDict[blockaddress], "起始地址:", hex(regaddress), "起始位置:", StateBlockDict[regaddress], end="")

    if funcode == 0x03:
        (quantity, ) = struct.unpack('>H', modbus_request[4:6])
        print("长度:", quantity)
    elif funcode == 0x06:
        (dataa, ) = struct.unpack('>H', modbus_request[4:6])
        print("数据:", hex(dataa))
    elif funcode == 0x10:
        (quantity,) = struct.unpack('>H', modbus_request[4:6])
        (bytenum, ) = struct.unpack('>B', modbus_request[6:7])

        # 从modbus_tk的原文件获取的方法
        data = []
        count = 0
        for i in range(quantity):
            count += 1
            fmt = "H"
            data.append(struct.unpack(">" + fmt, modbus_request[7 + 2 * i:9 + 2 * i])[0])
        print("长度:", quantity, "bytes:", bytenum, ' ', end="")  # end=""表示不换行
        print("数据:", " ".join(hex(i) for i in data))
        if StateBlockDict[regaddress] == 'LED控制字':
            parse_led(data)
        elif StateBlockDict[regaddress] == '表情控制字':
            parse_emotion(data)
        elif StateBlockDict[regaddress] == '并发动作控制字':
            parse_action(data)


def parse_led(data):

    # 控制字
    # b15 1覆盖方式执行/0队列缓存执行
    # b14 1停止全部效果/0增加执行效果
    # b13：0，保留
    if (data[0]&0x8000) >> 15 == 1:
        print("覆盖方式执行", ' ', end="")
    elif (data[0]&0x8000) >> 15 == 0:
        print("队列缓存执行", ' ', end="")

    if (data[0]&0x4000) >> 14 == 1:
        print("停止全部效果", ' ', end="")
    elif (data[0]&0x4000) >> 14 == 0:
        print("增加执行效果", ' ', end="")

    # 效果编号
    # ledDic,记录了对应编号
    print("LED效果:", ledDic[data[1]], ' ', end="")
    # 参数1
    # 亮度0-100%
    print("亮度:", data[2])
    # 参数2
    # 一些效果有
    # 参数3
    # 个别效果有


def parse_emotion(data):

    # 控制字
    # b15 1覆盖方式执行/0队列缓存执行
    # b14 1停止全部效果/0增加执行效果
    # b13：0，保留
    if (data[0]&0x8000) >> 15 == 1:
        print("覆盖方式执行", ' ', end="")
    elif (data[0]&0x8000) >> 15 == 0:
        print("队列缓存执行", ' ', end="")

    if (data[0]&0x4000) >> 14 == 1:
        print("停止全部效果", ' ', end="")
    elif (data[0]&0x4000) >> 14 == 0:
        print("增加执行效果", ' ', end="")

    # 效果编号
    # ledDic,记录了对应编号
    print("表情效果:", eyeemotionDict[data[1]], ' ', end="")
    # 参数1
    # 亮度0-100%
    print("次数:", data[2])
    # 参数2
    # 一些效果有
    # 参数3
    # 个别效果有


def parse_action(data):

    # 控制字
    # b15 1覆盖方式执行/0队列缓存执行
    # b14 1停止全部效果/0增加执行效果
    # b13：0，保留
    if (data[0] & 0x8000) >> 15 == 1:
        print("覆盖方式执行", ' ', end="")
    elif (data[0] & 0x8000) >> 15 == 0:
        print("队列缓存执行", ' ', end="")

    if (data[0] & 0x4000) >> 14 == 1:
        print("停止全部效果", ' ', end="")
    elif (data[0] & 0x4000) >> 14 == 0:
        print("增加执行效果", ' ', end="")

    # A动作编号
    # actionDict,记录了对应编号
    print("A动作编号:", actionDict[data[1]], ' ', end="")
    # A动作参数
    print("类型:", actioncatgoryDict[(data[2] & 0x7000) >> 12], ' ', end="")
    print("参数:", (data[2] & 0x0FFF), ' ', end="")

    # B动作编号
    print("B动作编号:", actionDict[data[3]], ' ', end="")
    # B动作参数
    print("类型:", actioncatgoryDict[(data[4] & 0x7000) >> 12], ' ', end="")
    print("参数:", (data[4] & 0x0FFF), ' ', end="")

    # C动作编号
    print("C动作编号:", actionDict[data[5]], ' ', end="")
    # C动作参数
    print("类型:", actioncatgoryDict[(data[6] & 0x7000) >> 12], ' ', end="")
    print("参数:", (data[6] & 0x0FFF))
