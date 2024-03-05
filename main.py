import  os
from  PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from  PyQt5 import  QtWidgets
import functions_text_summarization
from GUI_MAIN import Ui_MainWindow
from functions_text_summarization import *
from report import Ui_Dialog


class Example(QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.filename_in_directory = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.new_windows = QtWidgets.QDialog()
        self.dialog_report = Ui_Dialog()
        self.dialog_report.setupUi(self.new_windows)
        self.ui.toolButton.clicked.connect(self.open_directory)
        self.ui.toolButton_2.clicked.connect(self.open_directory)
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.actionClose.triggered.connect(lambda: self.close())
        self.ui.actionReport.triggered.connect(self.open_modal_windows)
        self.ui.pushButton.clicked.connect(self.start)

    def open_directory(self):
        try:
            filename_path = QFileDialog.getExistingDirectory(self,caption='Выбрать каталог', directory=os.getcwd())
            btn = self.sender()
            if btn.text() == "Open":
                self.filename_in_directory = filename_path
                self.ui.lineEdit.setText(filename_path)
                list_file = os.listdir(filename_path)
                self.ui.progressBar.setMaximum(len(list_file))
                self.ui.textEdit.setText("\n".join([f"{j+1}) {i}" for j,i in enumerate(list_file)]))
            elif btn.text() == "Save":
                self.ui.lineEdit_2.setText(filename_path)
            if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "":
                self.ui.pushButton.setEnabled(True)
                self.ui.pushButton_2.setEnabled(True)
        except:
            pass

    def open_modal_windows(self):
        self.new_windows.show()

    def start(self):
        os.chdir(self.filename_in_directory)
        for numbers, file in enumerate(os.listdir(os.getcwd())):
            self.ui.progressBar.setValue(numbers+1)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    windows = Example()
    windows.show()
    sys.exit(app.exec_())