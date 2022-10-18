import   datetime, time, json, os
import time
from epics import caget,caput

def checkout(fo,m2_thread):
	shutter_open_flag = caget("EXP_IB2_RM:2ndShutter:ON")
	ctrl_cmd  = caget("EXP_IB2_RM:soft:ctrl_stat")
	run_id = caget("EXP_IB2_RM:soft:run_no")
	print datetime.datetime.now()
	current_date = "the date: " + str(datetime.datetime.now()) + "\n"
	fo.writelines(current_date)
	fo.writelines("the shutter:" + str(shutter_open_flag) + " ,the run number:" + str(run_id) + " ,the cmd:" + str(ctrl_cmd) + "\n")		
	caput("EXP_IB2_MR:Monitor1:Checkout:bi",1 , wait=True, timeout=2)		
		
	m2_ioc_connect = 1
	m2_pulse_counter_pro = caget("EXP_IB2_RM:M1:PulseCounter_RBV",timeout = 2)
	if m2_pulse_counter_pro == None : 
		fo.writelines("error occured,the <m2> is exception,maybe the neros ioc is disconnected ~~\n")
		caput("EXP_IB2_MR:Monitor1:Checkout:bi",0 , wait=True, timeout=2)
		print "m2 ioc dis !!"
		m2_ioc_connect = 0
	print shutter_open_flag,ctrl_cmd,m2_ioc_connect

	if shutter_open_flag == 1 and ctrl_cmd == 'RUNNING' and m2_ioc_connect == 1:
		# checkout  whether the ros is connect
		time.sleep(3)

		# m2 pulse check 
		m2_pulse_counter_con = caget("EXP_IB2_RM:M1:PulseCounter_RBV")
		m2_delta_pulse = m2_pulse_counter_con - m2_pulse_counter_pro
		if m2_delta_pulse == 0 :   
			fo.writelines("error occured,the <m2> is exception,maybe the tcp is not conneted~~\n")
			caput("EXP_IB2_MR:Monitor1:Checkout:bi",0 , wait=True, timeout=2)		
		else : 
			print("the <m2> ros is normal,and the detla pusle is %d" % m2_delta_pulse)			
			fo.writelines("the <m2> ros is normal,and the <m2> detla pusle:" + str(m2_delta_pulse) + "\n")		
		#checkout whether the counting rate is normal

	else : 
		print "the run is not start!!!"
		fo.writelines("the run is not start!!!\n")		

if __name__ == "__main__":	
				
	while 1:
		fo = open('log.dat','a+')
		m2_thread = 10
		checkout(fo,m2_thread)
		fo.writelines("\n\n")
		fo.close()	
		print "\n\n"	
		time.sleep(60)










