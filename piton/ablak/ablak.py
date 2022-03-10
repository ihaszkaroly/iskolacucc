from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.Qtwidgets import QLabel , QPushButton , QlineEdit
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        label1 = QLabel(self)
        label1.setText("Még nyílnak")
        label1.move(50,50)
        button1 = QPushButton(self)
        button1.setText("Mehet")
        button1.move(100, 140)
        button1.clicked.connect(self.on_click_mehet_button)

        self.edit1 = QlineEdit
        self.edit1.move(100,180)

        self.setGeometry(100, 100, 300, 200)   
        self.setWindowTitle("Itt vagyok")
        self.show()
    def on_click_mehet_button(self):
        szoveg = self.edit1.Text()
        print("működik")
        self.label1.setText(szoveg)
        self.setWindowTitle("Valami")

application = QApplication(sys.argv)
mainWindow = MainWindow
sys.exit(application.exec_())