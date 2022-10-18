import   datetime, time, json, os
import time
from epics import caget,caput

shutter_open_flag = caget("EXP_TB_SH:Shtr1:SHTR_ON:SW:bii",timeout = 10)
print shutter_open_flag
if shutter_open_flag == None: 
	print "okokok~~~"
