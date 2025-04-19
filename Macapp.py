import sys
from PyQt6.QtWidgets import QApplication,QWidget

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App') # ウィンドウのタイトル
        self.setGeometry(320,150,900,600) # ウィンドウの位置と大きさ

qAp = QApplication(sys.argv)
App = Test()
App.show()
qAp.exec()