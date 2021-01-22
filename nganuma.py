import sys
from nganu import *
class MyForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.file.triggered.connect(self.file)
        self.ui.webb.triggered.connect(self.webb)
        self.ui.help.triggered.connect(self.help)
        self.ui.openfile.clicked.connect(self.file)
        self.ui.crawl.clicked.connect(self.webb)
        self.ui.summ.clicked.connect(self.help)
        
        
    def file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')
        
        with file:
            text = file.read()
            self.rawtext.setText(text)
    def webb(self):
        print('anu')
            
    def help(self):
        print('nganu')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

