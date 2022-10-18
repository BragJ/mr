import   datetime, time, json, os
import time
from epics import caget,caput,PV

p=PV('EXP_IB1_GP:soft:cmd')
print p.get()
print caget('EXP_IB1_GP:soft:cmd.ASG')
print caget('EXP_IB1_GP:soft:cmd.ZRST')

