import   datetime, time, json, os
import time
from epics import caget,caput
#from interval import Interval
from interval import Interval


def checkout(fo, alarm_thread):
	## winner1
	DEV_w1_u = "EXP_IB1_GP:DET:HV:Winner1:u"
	DEV_SLOT_w1 = "EXP_IB1_GP:DET:HV:Winner1:SLOT"
	DEV_w2_u = "EXP_IB1_GP:DET:HV:Winner2:u"
	DEV_SLOT_w2 = "EXP_IB1_GP:DET:HV:Winner2:SLOT"

	m_bo = ":bo" 
	Vol_Read = ":Voltage_Read"
	Vol_Set = ":Voltage_Set"
	#ctrl_cmd = caget("EXP_IB1_FFF:soft:cmd:bi")
	ctrl_cmd  = caget("EXP_IB1_GP:soft:cmd")
        print datetime.datetime.now()
        current_date = "the date: " + str(datetime.datetime.now()) + "\n"
        fo.writelines(current_date)
	flag_num = 0

	slot_list_w1 = [0,1,3,4,6,7,9]
	if ctrl_cmd == 1:
	        slot_list_w1 = [0,1,3,4,6,7,9]
        	for slot_num in slot_list_w1:
			#EXP_IB1_GP:DET:HV:Winner1:SLOT01:bo
			slot_pv_name_alarm = DEV_SLOT_w1 + '{0:0>2}'.format(str(slot_num)) + m_bo
			caput(slot_pv_name_alarm,1 , wait=True, timeout=2)
			flag_num = 0
			
			for channel_num in range(0,16):
				if slot_num == 0:
					vol_pv_name_read = DEV_w1_u + str(channel_num) + Vol_Read
					vol_pv_name_set = DEV_w1_u + str(channel_num) + Vol_Set
				else:
					vol_pv_name_read = DEV_w1_u + str(slot_num) + '{0:0>2}'.format(str(channel_num)) + Vol_Read
					vol_pv_name_set = DEV_w1_u + str(slot_num) + '{0:0>2}'.format(str(channel_num)) + Vol_Set
				vol_pv_value_read = caget(vol_pv_name_read,timeout = 2)
				vol_pv_value_set = caget(vol_pv_name_set,timeout = 2)
			 
				normal_range = Interval(vol_pv_value_set - alarm_thread,vol_pv_value_set + alarm_thread)
				if vol_pv_value_read ==None or  vol_pv_value_read== None:	
					print "ioc is not start!!!"
					fo.writelines("ioc is shutdown!!!\n")
					caput(slot_pv_name_alarm,0 , wait=True, timeout=2)
				else:
					caput(slot_pv_name_alarm,1 , wait=True, timeout=2)

				if abs(vol_pv_value_read) in normal_range and flag_num == 0: 
				#if vol_pv_value_read in normal_range: 
					caput(slot_pv_name_alarm,1 , wait=True, timeout=2)
					print ("win1  <slot %d - channel %d> is normal, the set_voltage and read_voltage is %d and %d" % (slot_num,channel_num,vol_pv_value_set,vol_pv_value_read))	
				else:
					caput(slot_pv_name_alarm,0, wait=True, timeout=2)
					flag_num = flag_num + 1
					print ("win1 <slot %d - channel %d> is disnormal @@@@@@@ the set_voltage and read_voltage is %d and %d" % (slot_num,channel_num,vol_pv_value_set,vol_pv_value_read))	
					fo.writelines("<slot " + str(slot_num)+ "- channel" + str(channel_num) + ">is disnormal,set_voltage and read_voltage is " + str(vol_pv_value_set)+ " and " + str(vol_pv_value_read) + "\n")

       		slot_list_w2 = [0,2,4]
        	for slot_num in slot_list_w2:
			slot_pv_name_alarm = DEV_SLOT_w2 + '{0:0>2}'.format(str(slot_num)) + m_bo
			caput(slot_pv_name_alarm,1 , wait=True, timeout=2)
			flag_num = 0
			
			for channel_num in range(0,16):
				if slot_num == 0:
					vol_pv_name_read = DEV_w2_u + str(channel_num) + Vol_Read
					vol_pv_name_set = DEV_w2_u + str(channel_num) + Vol_Set
				else:
					vol_pv_name_read = DEV_w2_u + str(slot_num) + '{0:0>2}'.format(str(channel_num)) + Vol_Read
					vol_pv_name_set = DEV_w2_u + str(slot_num) + '{0:0>2}'.format(str(channel_num)) + Vol_Set
				vol_pv_value_read = caget(vol_pv_name_read,timeout = 2)
				vol_pv_value_set = caget(vol_pv_name_set,timeout = 2)
			 
				normal_range = Interval(vol_pv_value_set - alarm_thread,vol_pv_value_set + alarm_thread)
				if vol_pv_value_read ==None or  vol_pv_value_read== None:	
					print "ioc is not start!!!"
					fo.writelines("ioc is shutdown!!!\n")
					caput(slot_pv_name_alarm,0 , wait=True, timeout=2)
				else:
					caput(slot_pv_name_alarm,1 , wait=True, timeout=2)

				if abs(vol_pv_value_read) in normal_range and flag_num == 0: 
				#if vol_pv_value_read in normal_range: 
					caput(slot_pv_name_alarm,1 , wait=True, timeout=2)
					print ("win2 <slot %d - channel %d> is normal, the set_voltage and read_voltage is %d and %d" % (slot_num,channel_num,vol_pv_value_set,vol_pv_value_read))	
				else:
					caput(slot_pv_name_alarm,0, wait=True, timeout=2)
					flag_num = flag_num + 1
					print ("win2 <slot %d - channel %d> is disnormal @@@@@@@ the set_voltage and read_voltage is %d and %d" % (slot_num,channel_num,vol_pv_value_set,vol_pv_value_read))	
					fo.writelines("<slot " + str(slot_num)+ "- channel" + str(channel_num) + ">is disnormal,set_voltage and read_voltage is " + str(vol_pv_value_set)+ " and " + str(vol_pv_value_read) + "\n")


	else:
		print  "run is not start"
		fo.writelines("the run is not start!!!\n")
	

if __name__ == "__main__":
        while 1:
                fo = open('hv_log_.dat','a+')
                alarm_thread = 10
                checkout(fo, alarm_thread)
                fo.writelines("\n")
                fo.close()
                print "\n\n"
                time.sleep(60)

