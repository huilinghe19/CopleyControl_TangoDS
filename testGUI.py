import sys
from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.panel import TaurusForm
from taurus.qt.qtgui.button import TaurusCommandButton
from taurus.qt.qtgui.plot import TaurusTrend


app = TaurusApplication(sys.argv)
panel = Qt.QWidget()
vlayout = Qt.QVBoxLayout()
panel.setLayout(vlayout)

hlayout = Qt.QHBoxLayout()
vlayout.addLayout(hlayout)

panel1 = TaurusForm()
props = [ 'state', 'status', 'position', 'velocity', 'acceleration']
model = [ 'stepnet01/%s' % p for p in props ]
panel1.setModel(model)
hlayout.addWidget(panel1)

button =  TaurusCommandButton(command = "RunMacro", 
                              parameters=['ascan','stepnet01','0','10000','5','1'],
                              icon=None)
button.setCustomText('Ascan')
button.setModel('Door/demo2/1')
hlayout.addWidget(button)

panel2 = TaurusTrend()
model2 = ['stepnet01/position']
panel2.setXIsTime(True) 
panel2.setModel(model2)
vlayout.addWidget(panel2)

panel.show()
sys.exit(app.exec_())