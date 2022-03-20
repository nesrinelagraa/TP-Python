from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys
import webbrowser


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Customer")
        self.setFixedSize(800, 800)
        self.label1 = QLabel(" Enter your IP:", self)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 30)
        self.label2 = QLabel("Enter your API key:", self)
        self.label2.move(10, 60)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 90)
        self.label3 = QLabel("Enter the hostname:", self)
        self.label3.move(10, 120)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 150)
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 200)
        self.button = QPushButton("Send", self)
        self.button.move(10, 230)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        ip = self.text1.text()
        api = self.text2.text()
        hostname = self.text3.text()

        if ip == "" or api == "" or hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(ip,api,hostname)
            if res:
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #to open the link in Chrome
                self.label2.setText("Answer%s" % (res))
                webbrowser.get(chrome_path).open(res)
                self.label2.adjustSize()
                self.show()

    def __query(self,ip,api, hostname):
        url = "http://{}/ip/{}?key={}".format(hostname, ip,api)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()














'''import requests
from PyQt5.QtWidgets import QMessageBox

class Main():
    def query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":

    main = Main()
    hostname="127.0.0.1:8000"
    res = main.query(hostname)
    if res:
        print(res)'''

