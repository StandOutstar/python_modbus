# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from display import Ui_MyMainWindow
from test_modbus_slave import *

import modbus_tk
import modbus_tk.defines as cst
# import modbus_tk.modbus as modbus
import modbus_tk.modbus_rtu as modbus_rtu
import modbus_tk.hooks as hoook
import serial
import time
import parse_modbus_request


def hookbefore_handle_request(requestpdu):
    # request is a str like '\x01\x06\x00\x01\x00\x01\x19\xca'
    # parse_modbus_request.parse_modbus_request(requestpdu)
    parse_modbus_request.parse_modbus_request(requestpdu)

# # 全局变量，端口名
port = ''


class mywindow(QtWidgets.QMainWindow, Ui_MyMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setupUi(self)
        self.thread = ParseModbusthread()

        # 把thread中的信号连接到自己的函数上。自己的函数实现显示。
        # self.thread.display1signal.connect(self.display1out)
        # self.thread.display2signal.connect(self.display2out)
        # self.thread.display3signal.connect(self.display3out)

    # 停止按钮信号槽
    def DisplayStop_click(self):
        # QtWidgets.QMessageBox.critical(self.pushButton, "关于", "这是第一个PyQt5 GUI程序")
        QCoreApplication.quit()

    # 连接按钮信号槽
    def startparse(self):
        global port
        port = self.lineEdit.text()  # 获取端口名
        # 解析线程
        self.thread.start()


class ParseModbusthread(QThread):
    def __int__(self):
        super(ParseModbusthread, self).__init__()

    def run(self):
        global port
        # 协议的解析阻塞了界面的显示,需要放到线程里
        # 安装钩子
        hoook.install_hook("modbus.Server.before_handle_request", hookbefore_handle_request)
        logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")
        # create server
        server = modbus_rtu.RtuServer(serial.Serial(port, baudrate=115200, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        try:
            slaver = server.add_slave(1)
            slaver.add_block("holdingResgiter", cst.HOLDING_REGISTERS, 0, 16383)
            slaver.set_values("holdingResgiter", 0x0000, (2, 3, 4, 5))
            server.start()
            print(slaver.get_values("holdingResgiter", 0x2000, 3))
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            logger.info("destory")
            # stop server
            server.stop()

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
