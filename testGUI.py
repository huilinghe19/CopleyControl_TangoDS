#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from taurus.qt.qtgui.display import *
from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.panel import TaurusForm
from taurus.qt.qtgui.button import TaurusCommandButton, QButtonBox
from taurus.qt.qtgui.plot import TaurusTrend
from taurus.qt.qtgui.plot import TaurusPlot

Door_name = 'Door/python3tangods/1'
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
model = [ 'tango://dide17.basisit.de:10000/motor/copleyctrl/1/%s' % p for p in props ]
panel1.setModel(model)
statelayout.addWidget(panel1)
panel1.show()


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
   
scanbutton = TaurusCommandButton(command = "RunMacro", icon=None)
scanbutton.setCustomText('Ascan')
scanbutton.setModel(Door_name) 

def getResult(widget):
    text = widget.displayText() 
    print("text: ", text)
    print(type(text))
    print(text.encode('utf-8'))
    #return text.encode('utf-8')
    return text
def getStartPos():
    print("Start:", getResult(w1))
    print(type(getResult(w1)))
    return str(getResult(w1))
def getEndPos():
    return str(getResult(w2))
def getIntervals():
    return int(getResult(w3))
def getIntegrationTime():
    return str(getResult(w4))
scanbutton = TaurusCommandButton(command = "RunMacro", icon=None)
scanbutton.setCustomText('Ascan')
scanbutton.setModel(Door_name) 
def setScan():
    scanbutton.setParameters(['ascan', 'tango://dide17.basisit.de:10000/motor/copleyctrl/1', getStartPos(), 
                              getEndPos(), 
                              getIntervals(), 
                              getIntegrationTime()])

setParameterbutton = Qt.QPushButton("Apply")
setParameterbutton.clicked.connect(setScan)    
scanButtonLayout.addWidget(setParameterbutton)
scanButtonLayout.addWidget(scanbutton)




panel2 = TaurusTrend()
model2 = ['tango://dide17.basisit.de:10000/motor/copleyctrl/1/position', 'tango://dide17.basisit.de:10000/motor/copleyctrl/2/position']
#panel2.setXIsTime(True) 
panel2.setModel(model2)
mainLayout.addWidget(panel2)

panel.show()
panel.setWindowTitle("Copley Controller: Stepnet3")


#panelKeithley = Qt.QWidget()
#mainLayout2 = Qt.QVBoxLayout()
#panelKeithley.setLayout(mainLayout2)

#panel3 = TaurusForm()
#props = [ 'state', 'value']
#model = [ 'keithleySpannung/%s' % p for p in props ]
#panel3.setModel(model)
#mainLayout2.addWidget(panel3)


#panel4 = TaurusTrend()
#model4 = ['keithleySpannung/value']
#panel4.setXIsTime(True) 
#panel4.setModel(model4)
#mainLayout2.addWidget(panel4)
#panelKeithley.show()
#panelKeithley.setWindowTitle("Keithley2000 Spannung")


panelmotors = Qt.QWidget()
mainLayout9 = Qt.QVBoxLayout()
panelmotors.setLayout(mainLayout9)

panel9 = TaurusForm()
model9 = [ 'tango://dide17.basisit.de:10000/motor/copleyctrl/1','tango://dide17.basisit.de:10000/motor/copleyctrl/2','tango://dide17.basisit.de:10000/motor/copleyctrl/1/position', 'tango://dide17.basisit.de:10000/motor/copleyctrl/2/position']
panel9.setModel(model9)
mainLayout9.addWidget(panel9)

scanbutton10 = TaurusCommandButton(command = "RunMacro", icon=None)
scanbutton10.setCustomText('Start Scan')
scanbutton10.setModel(Door_name) 
scanbutton10.setParameters(['ascan', 'tango://dide17.basisit.de:10000/motor/copleyctrl/1', 1000, 10000, 5, 2])                      
mainLayout9.addWidget(scanbutton10)

panelmotors.show()
panelmotors.setWindowTitle("Motors Status")

sys.exit(app.exec_())
