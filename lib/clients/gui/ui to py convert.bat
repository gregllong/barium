ref START cmd /k "pyuic4 %~dp0MassSpecExperiment_gui.ui > %~dp0gui1.py"
ref START cmd /k "pyuic4 %~dp0CommandLine_gui.ui > %~dp0gui2.py"
ref START cmd /k "pyuic4 %~dp0SaveDirectory_gui.ui > %~dp0gui3.py"
START cmd /k "pyuic4 %~dp0Scalar_gui.ui > %~dp0gui4.py"
ref START cmd /k "pyuic4 %~dp0LabRADconnection_gui.ui > %~dp0gui5.py"