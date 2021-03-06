import labrad
from twisted.internet.defer import inlineCallbacks, returnValue

from common.lib.servers.abstractservers.script_scanner.scan_methods import experiment
from barium.lib.scripts.pulse_sequences.MicrowaveSweep133 import microwave_sweep as main_sequence

from config.FrequencyControl_config import FrequencyControl_config
from config.multiplexerclient_config import multiplexer_config

import time
from labrad.units import WithUnit
import numpy as np
import datetime as datetime


class microwave_sweep(experiment):

    name = 'Microwave Sweep'

    exp_parameters = []

    # Add the parameters from the required subsequences
    exp_parameters.extend(main_sequence.all_required_parameters())

    @classmethod
    def all_required_parameters(cls):
        return cls.exp_parameters


    def initialize(self, cxn, context, ident):
        self.ident = ident
        self.cxn = labrad.connect(name = 'Microwave Sweep')
        self.cxnwlm = labrad.connect('10.97.111.8', name = 'Microwave Sweep', password = 'lab')


        self.wm = self.cxnwlm.multiplexerserver
        self.pulser = self.cxn.pulser
        self.grapher = self.cxn.grapher
        self.dv = self.cxn.data_vault
        self.HPA = self.cxn.hp8672a_server
        self.pv = self.cxn.parametervault

        # Define variables to be used
        self.p = self.parameters
        self.cycles = self.p.MicrowaveSweep133.Sequences_Per_Point
        self.start_frequency = self.p.MicrowaveSweep133.Start_Frequency
        self.stop_frequency = self.p.MicrowaveSweep133.Stop_Frequency
        self.step_frequency = self.p.MicrowaveSweep133.Frequency_Step

        # Need to map the gpib address to the labrad conection
        self.device_mapA = {}
        self.device_mapB = {}
        self.get_device_map()
        self.HPA.select_device(self.device_mapA['GPIB0::19'])

        self.set_up_datavault()

    def run(self, cxn, context):

        freq = np.linspace(self.start_frequency['MHz'],self.stop_frequency['MHz'],\
                    int((abs(self.stop_frequency['MHz']-self.start_frequency['MHz'])/self.step_frequency['MHz']) +1))

        # program sequence to be repeated
        pulse_sequence = main_sequence(self.p)
        pulse_sequence.programSequence(self.pulser)

        for i in range(len(freq)):
            if self.pause_or_stop():
                break

            self.disc = self.pv.get_parameter('StateReadout','state_readout_threshold')
            self.HPA.set_frequency(WithUnit(freq[i],'MHz'))
            time.sleep(.3) # time to switch frequencies
            counts = 0
            self.pulser.start_number(int(self.cycles))
            self.pulser.wait_sequence_done()
            self.pulser.stop_sequence()
            counts = self.pulser.get_readout_counts()
            self.pulser.reset_readout_counts()
            bright = np.where(counts >= self.disc)
            fid = float(len(bright[0]))/len(counts)
            self.dv.add(freq[i] , fid)

    def set_up_datavault(self):
        # set up folder
        date = datetime.datetime.now()
        year  = `date.year`
        month = '%02d' % date.month  # Padded with a zero if one digit
        day   = '%02d' % date.day    # Padded with a zero if one digit
        trunk = year + '_' + month + '_' + day
        self.dv.cd(['',year,month,trunk],True)
        dataset = self.dv.new('MicrowaveSweep',[('run', 'arb u')], [('Counts', 'Counts', 'num')])
        # add dv params
        for parameter in self.p:
            self.dv.add_parameter(parameter, self.p[parameter])

        # Set live plotting
        self.grapher.plot(dataset, 'microwave_sweep', False)


    def set_wm_frequency(self, freq, chan):
        self.wm.set_pid_course(chan, freq)

    def get_device_map(self):
        gpib_listA = FrequencyControl_config.gpibA
        gpib_listB = FrequencyControl_config.gpibB

        devices = self.HPA.list_devices()
        for i in range(len(gpib_listA)):
            for j in range(len(devices)):
                if devices[j][1].find(gpib_listA[i]) > 0:
                    self.device_mapA[gpib_listA[i]] = devices[j][0]
                    break



    def finalize(self, cxn, context):
        self.cxn.disconnect()
        self.cxnwlm.disconnect()

if __name__ == '__main__':
    cxn = labrad.connect()
    scanner = cxn.scriptscanner
    exprt = microwave_sweep(cxn = cxn)
    ident = scanner.register_external_launch(exprt.name)
    exprt.execute(ident)




