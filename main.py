from PyQt5.QtCore import Qt , QUrl
from PyQt5.QtWidgets import QApplication, QWidget , QLineEdit , QPushButton , QHBoxLayout , QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
#init interface
app = QApplication([])
win = QWidget()
inp = QLineEdit()
gob = QPushButton('Go')
undob = QPushButton('undo')
redob = QPushButton('redo')
updateb = QPushButton('update')
web = QWebEngineView()
main = QVBoxLayout()
top = QHBoxLayout()
main.addLayout(top)
top.addWidget(undob)
top.addWidget(redob)
top.addWidget(updateb)
top.addWidget(inp)
top.addWidget(gob)
main.addWidget(web)
#create global changed

urlhist = []
nowurl = -1


def serf():
    global nowurl
    urlhist.append(QUrl(inp.text()))
    nowurl +=1
    web.setUrl(QUrl(inp.text()))

def undo():
    global nowurl
    if nowurl -1 <= 1 :
        nowurl -= 1
        web.setUrl(urlhist[nowurl])
    else:
        pass


def redo():
    global nowurl
    if nowurl + 1 <= len(urlhist)  -1:
        nowurl += 1
        web.setUrl(urlhist[nowurl])

def update():
    web.reload()


def change(ok):
    global nowurl
    inp.text = web.url().url()
    if web.url() != urlhist[nowurl]:
        urlhist.append(web.url())
        nowurl += 1

gob.clicked.connect(serf)
web.loadFinished.connect(change)
win.setLayout(main)
win.show()
win.resize(800 , 600)
app.exec_()

