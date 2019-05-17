#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from taurus.qt.qtgui.display import *
from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.panel import TaurusForm
from taurus.qt.qtgui.button import TaurusCommandButton, QButtonBox
from taurus.qt.qtgui.plot import TaurusTrend

Door_name = 'Door/demo2/1'
app = TaurusApplication(sys.argv)
panel = Qt.QWidget()
mainLayout = Qt.QVBoxLayout()
panel.setLayout(mainLayout)

settingLayout = Qt.QHBoxLayout()
mainLayout.addLayout(settingLayout)

statelayout = Qt.QVBoxLayout()
scanlayout = Qt.QVBoxLayout()
settingLayout.addLayout(statelayout)
settingLayout.addLayout(scanlayout)

panel1 = TaurusForm()
props = [ 'state', 'status', 'position', 'velocity', 'acceleration']
model = [ 'stepnet01/%s' % p for p in props ]
panel1.setModel(model)
statelayout.addWidget(panel1)

scanmainLayout = Qt.QHBoxLayout()
scanButtonLayout = Qt.QHBoxLayout()
scanlayout.addLayout(scanmainLayout)
scanlayout.addLayout(scanButtonLayout)

lableLayout = Qt.QVBoxLayout()
parametersLayout= Qt.QVBoxLayout()
scanmainLayout.addLayout(lableLayout)
scanmainLayout.addLayout(parametersLayout)

l1 = TaurusLabel('Start position')
l2= TaurusLabel('Final position')
l3= TaurusLabel('Interval')
l4= TaurusLabel('Integration time')

lableLayout.addWidget(l1)
lableLayout.addWidget(l2)
lableLayout.addWidget(l3)
lableLayout.addWidget(l4)

w1 = Qt.QLineEdit()
w2 = Qt.QLineEdit()
w3 = Qt.QLineEdit()
w4 = Qt.QLineEdit()
parametersLayout.addWidget(w1)
parametersLayout.addWidget(w2)
parametersLayout.addWidget(w3)
parametersLayout.addWidget(w4)
def getResult(widget):
    text = widget.displayText() 
    return text.encode('utf-8')
   
scanbutton = TaurusCommandButton(command = "RunMacro", icon=None)
scanbutton.setCustomText('Ascan')
scanbutton.setModel(Door_name) 
def setScan():
    startPos = getResult(w1)
    endPos = getResult(w2)
    intervals = getResult(w3)
    integrationTime = getResult(w4)
    scanbutton.setParameters(['ascan', 'stepnet01', getResult(w1), getResult(w2), getResult(w3), getResult(w4)])

setParameterbutton = Qt.QPushButton("Apply")
setParameterbutton.clicked.connect(setScan)    
scanButtonLayout.addWidget(setParameterbutton)
scanButtonLayout.addWidget(scanbutton)

panel2 = TaurusTrend()
model2 = ['stepnet01/position']
panel2.setXIsTime(True) 
panel2.setModel(model2)
mainLayout.addWidget(panel2)

panel.show()
panel.setWindowTitle("Copley Controller: Stepnet01")
sys.exit(app.exec_())