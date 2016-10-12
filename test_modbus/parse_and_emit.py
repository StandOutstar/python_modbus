import struct
from actionTable import ledDic
from actionTable import eyeemotionDict
from actionTable import actionDict
from actionTable import actioncatgoryDict
from actionTable import SlaveIdDict
from actionTable import FunCodeDict
from actionTable import RegisterBlockDict
from actionTable import StateBlockDict
from PyQt5.QtCore import *


class parse_modbus(QObject):
    # requestpdu = ()
    ledinfosignal = pyqtSignal(str)
    expressioninfosignal = pyqtSignal(str)
    actioninfosignal = pyqtSignal(str)

    # def __init__(self, requestpdu):
    #     self.requestpdu = requestpdu

    def parse_modbus_request(self, requestpdu):
        s_baseinfo = ''

        modbus_request = requestpdu[1]
        (slaveid, funcode) = struct.unpack('>BB', modbus_request[0:2])  # 拆包结果是个tuple
        (regaddress, ) = struct.unpack('>H', modbus_request[2:4])  # 拆包结果是个tuple
        (blockaddress, ) = struct.unpack('>B', modbus_request[2:3])  # 拆包结果是个tuple
        # print(modbus_request)
        # print(hex(regaddress))

        # print("发给", SlaveIdDict[slaveid], FunCodeDict[funcode], RegisterBlockDict[blockaddress], "起始地址:", hex(regaddress), "起始位置:", StateBlockDict[regaddress], end="")
        s_baseinfo += ("发给 "+str(SlaveIdDict[slaveid])+' '+str(FunCodeDict[funcode])+' '+str(RegisterBlockDict[blockaddress])+' '+"起始地址:"+str(hex(regaddress))+' '+"起始位置:"+str(StateBlockDict[regaddress])+' ')

        if funcode == 0x03:  # 读取
            (quantity, ) = struct.unpack('>H', modbus_request[4:6])
            # print("长度:", quantity)
            s_baseinfo += ("长度:"+str(quantity)+' ')
            # print(s_baseinfo)

        elif funcode == 0x06:  # 单个设置
            (dataa, ) = struct.unpack('>H', modbus_request[4:6])
            # print("数据:", hex(dataa))
            s_baseinfo += ("数据:"+str(hex(dataa))+' ')
            # print(s_baseinfo)

        elif funcode == 0x10:  # 连续设置
            (quantity,) = struct.unpack('>H', modbus_request[4:6])
            (bytenum, ) = struct.unpack('>B', modbus_request[6:7])

            # 从modbus_tk的原文件获取的方法
            data = []
            count = 0
            for i in range(quantity):
                count += 1
                fmt = "H"
                data.append(struct.unpack(">" + fmt, modbus_request[7 + 2 * i:9 + 2 * i])[0])
            # print("长度:", quantity, "bytes:", bytenum, ' ', end="")  # end=""表示不换行
            # print("数据:", " ".join(hex(i) for i in data))
            s_baseinfo += ("长度:"+str(quantity)+' '+"bytes:"+str(bytenum)+' '+"数据:"+" ".join(hex(i) for i in data)+' ')
            # print(s_baseinfo, end="")

            if StateBlockDict[regaddress] == 'LED控制字':
                self.parse_led(data, s_baseinfo)
            elif StateBlockDict[regaddress] == '表情控制字':
                self.parse_emotion(data, s_baseinfo)
            elif StateBlockDict[regaddress] == '并发动作控制字':
                self.parse_action(data, s_baseinfo)

    # ledinfosignal = pyqtSignal(str)

    def parse_led(self, data, s_baseinfo):
        s_ledinfo = s_baseinfo
        # ledsig = Sign()

        # 控制字
        # b15 1覆盖方式执行/0队列缓存执行
        # b14 1停止全部效果/0增加执行效果
        # b13：0，保留
        if (data[0]&0x8000) >> 15 == 1:
            # print("覆盖方式执行", ' ', end="")
            s_ledinfo += ("覆盖方式执行"+' ')
        elif (data[0]&0x8000) >> 15 == 0:
            # print("队列缓存执行", ' ', end="")
            s_ledinfo += ("队列缓存执行"+' ')
        if (data[0]&0x4000) >> 14 == 1:
            # print("停止全部效果", ' ', end="")
            s_ledinfo += ("停止全部效果" + ' ')
        elif (data[0]&0x4000) >> 14 == 0:
            # print("增加执行效果", ' ', end="")
            s_ledinfo += ("增加执行效果" + ' ')

        # 效果编号
        # ledDic,记录了对应编号
        # print("LED效果:", ledDic[data[1]], ' ', end="")
        # 参数1
        # 亮度0-100%
        # print("亮度:", data[2])
        # 参数2
        # 一些效果有
        # 参数3
        # 个别效果有
        s_ledinfo += ("LED效果:" + str(ledDic[data[1]]) + ' ' + "亮度:" + str(data[2]))
        # print(s_ledinfo)
        # global ledinfosignal
        # ledinfosignal.emit(s_ledinfo)
        self.ledinfosignal.emit(s_ledinfo)

    # expressioninfosignal = pyqtSignal(str)
    def parse_emotion(self, data, s_baseinfo):
        s_expressioninfo = s_baseinfo


        # 控制字
        # b15 1覆盖方式执行/0队列缓存执行
        # b14 1停止全部效果/0增加执行效果
        # b13：0，保留
        if (data[0]&0x8000) >> 15 == 1:
            # print("覆盖方式执行", ' ', end="")
            s_expressioninfo += ("覆盖方式执行"+' ')
        elif (data[0]&0x8000) >> 15 == 0:
            # print("队列缓存执行", ' ', end="")
            s_expressioninfo += ("队列缓存执行" + ' ')
        if (data[0]&0x4000) >> 14 == 1:
            # print("停止全部效果", ' ', end="")
            s_expressioninfo += ("停止全部效果" + ' ')
        elif (data[0]&0x4000) >> 14 == 0:
            # print("增加执行效果", ' ', end="")
            s_expressioninfo += ("增加执行效果" + ' ')

        # 效果编号
        # ledDic,记录了对应编号
        # print("表情效果:", eyeemotionDict[data[1]], ' ', end="")
        # # 参数1
        # # 亮度0-100%
        # print("次数:", data[2])
        # 参数2
        # 一些效果有
        # 参数3
        # 个别效果有
        s_expressioninfo += ("表情效果:" + str(eyeemotionDict[data[1]]) + ' ' + "次数:" + str(data[2]))
        # print(s_expressioninfo)
        # global expressioninfosignal
        # expressioninfosignal.emit(s_expressioninfo)
        self.expressioninfosignal.emit(s_expressioninfo)
    # actioninfosignal = pyqtSignal(str)

    def parse_action(self, data, s_baseinfo):
        s_actioninfo = s_baseinfo


        # 控制字
        # b15 1覆盖方式执行/0队列缓存执行
        # b14 1停止全部效果/0增加执行效果
        # b13：0，保留
        if (data[0] & 0x8000) >> 15 == 1:
            # print("覆盖方式执行", ' ', end="")
            s_actioninfo += ("覆盖方式执行" + ' ')
        elif (data[0] & 0x8000) >> 15 == 0:
            # print("队列缓存执行", ' ', end="")
            s_actioninfo += ("队列缓存执行" + ' ')

        if (data[0] & 0x4000) >> 14 == 1:
            # print("停止全部效果", ' ', end="")
            s_actioninfo += ("停止全部效果" + ' ')
        elif (data[0] & 0x4000) >> 14 == 0:
            # print("增加执行效果", ' ', end="")
            s_actioninfo += ("增加执行效果" + ' ')

        # A动作编号
        # actionDict,记录了对应编号
        # print("A动作编号:", actionDict[data[1]], ' ', end="")
        # # A动作参数
        # print("类型:", actioncatgoryDict[(data[2] & 0x7000) >> 12], ' ', end="")
        # print("参数:", (data[2] & 0x0FFF), ' ', end="")
        s_actioninfo += ("A动作编号:"+str(actionDict[data[1]])+' '+"类型:"+str(actioncatgoryDict[(data[2] & 0x7000) >> 12])+' '+"参数:"+str(data[2] & 0x0FFF)+' && ')

        # B动作编号
        # print("B动作编号:", actionDict[data[3]], ' ', end="")
        # # B动作参数
        # print("类型:", actioncatgoryDict[(data[4] & 0x7000) >> 12], ' ', end="")
        # print("参数:", (data[4] & 0x0FFF), ' ', end="")
        s_actioninfo += ("B动作编号:"+str(actionDict[data[3]])+' '+"类型:"+str(actioncatgoryDict[(data[4] & 0x7000) >> 12])+' '+"参数:"+str(data[4] & 0x0FFF)+' && ')

        # C动作编号
        # print("C动作编号:", actionDict[data[5]], ' ', end="")
        # # C动作参数
        # print("类型:", actioncatgoryDict[(data[6] & 0x7000) >> 12], ' ', end="")
        # print("参数:", (data[6] & 0x0FFF))
        s_actioninfo += ("C动作编号:"+str(actionDict[data[5]])+' '+"类型:"+str(actioncatgoryDict[(data[6] & 0x7000) >> 12])+' '+"参数:"+str(data[6] & 0x0FFF))

        # print(s_actioninfo)
        # global actioninfosignal
        # actioninfosignal.emit(s_actioninfo)

        self.actioninfosignal.emit(s_actioninfo)
