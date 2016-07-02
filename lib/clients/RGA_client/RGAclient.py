from barium.lib.clients.gui.RGA_gui import RGA_UI
from twisted.internet.defer import inlineCallbacks, returnValue
from PyQt4 import QtGui, QtCore


class RGA_Client(RGA_UI):
    def __init__(self, reactor, host_ip, host_name, parent = None):
        from labrad.units import WithUnit
        self.U = WithUnit
        super(RGA_Client, self).__init__()
        self.reactor = reactor
        self.initialize(host_ip, host_name)
    @inlineCallbacks
    def initialize(self, host_ip, host_name):
        self.connect(host_ip, host_name)
        self.setupUi()
        self.signal_connect()
        yield None
    @inlineCallbacks
    def connect(self, host_ip, host_name):
        from labrad.wrappers import connectAsync
        self.cxn = yield connectAsync(host=host_ip, name="RGA Client")
        try:
            self.rga = self.cxn.rga_server
            print 'Connected to RGA Server.'
        except:
            print 'RGA Server Unavailable. Client is not connected.'
    @inlineCallbacks
    def signal_connect(self):
        filament_state = self.rga_filament_checkbox.isChecked()
        voltage = self.rga_voltage_spinbox.value()
        mass = self.rga_mass_lock_spinbox.value()
        self.rga_filament_checkbox.toggled.connect(lambda state=filament_state :self.set_filament_state(state))
        self.rga_voltage_spinbox.valueChanged.connect(lambda value=voltage :self.set_voltage(value))
        self.rga_mass_lock_spinbox.valueChanged.connect(lambda value=mass :self.set_mass_lock(value))
        self.rga_id_button.clicked.connect(lambda :self.get_id())
        self.rga_fl_button.clicked.connect(lambda :self.get_filament_status())
        self.rga_hv_button.clicked.connect(lambda :self.get_voltage())
        self.rga_read_buffer_button.clicked.connect(lambda :self.read_buffer())
        self.rga_clear_button.clicked.connect(lambda :self.clear_buffer())
        yield None
    @inlineCallbacks
    def set_filament_state(self,state):
        if state==True:
            bit = 1
        else:
            bit = 0
        yield self.rga.filament(bit)
    @inlineCallbacks
    def set_voltage(self,value):
        yield self.rga.high_voltage(value)
    @inlineCallbacks
    def set_mass_lock(self,value):
        yield self.rga.mass_lock(value)
    @inlineCallbacks
    def get_id(self):
        yield self.rga.identify()
    @inlineCallbacks
    def get_filament_status(self):
        yield self.rga.filament()
    @inlineCallbacks
    def get_voltage(self):
        yield self.rga.high_voltage()
    @inlineCallbacks
    def read_buffer(self):
        message = yield self.rga.read_buffer()
        self.rga_buffer_text.appendPlainText(message)
    @inlineCallbacks
    def clear_buffer(self):
        self.rga_buffer_text.clear()
        yield None
    @inlineCallbacks
    def closeEvent(self,x):
        self.set_voltage(0)
        self.set_filament_state(False)
        reactor.stop()
        yield None

import sys

if __name__ == "__main__":
    a = QtGui.QApplication( [] )
    from common.lib.clients import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor
    from socket import gethostname

    client = RGA_Client(reactor,'127.0.0.1',gethostname())
    client.show()

    reactor.run()
