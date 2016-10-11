# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

from display import Ui_MyMainWindow


class mywindow(QtWidgets.QMainWindow, Ui_MyMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def DisplayStop_click(self):
        QtWidgets.QMessageBox.critical(self.pushButton, "关于", "这是第一个PyQt5 GUI程序")

if __name__ == '__main__':
    '''
    主函数
    '''

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
