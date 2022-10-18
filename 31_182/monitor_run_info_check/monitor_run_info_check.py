import   datetime, time, json, os
import requests
import time
from epics import caget,caput

def get_value(pv_list_info):
	for pv_name in pv_list_info:
		if pv_name != 'EXP_IB2_RM:soft:cmd':
			pv_value  = caget(pv_name)
			pv_dict_info[pv_name] = pv_value  
			#print pv_name,'=', pv_dict_info[pv_name]
		else:
			pv_value  = caget(pv_name)
			pv_dict_info[pv_name] = cmd_info[pv_value]
			#print pv_name,'=',pv_dict_info[pv_name]

def send_data(pv_alarm_name,pv_alarm_value):
	result = []	
	record = {}
        record['endpoint'] = "gppd_pv"
        record['step'] = 60
        record['counterType'] = 'GAUGE'
        record['metric'] =  pv_alarm_name
        time_st = int(time.time())
        record['value'] = float(pv_alarm_value)
        record['timestamp'] = time_st
	result.append(record)
	requests.post("http://10.1.26.63:1988/v1/push", data=json.dumps(result))

	
def overview_alarm(fo):
	record_data=[]
	overview_list = []  
	for k in pv_dict_info:
		overview_list.append(pv_dict_info[k]) 
 	overview_list_tmp = list(set(overview_list))
	print overview_list
	fo.writelines(str(overview_list))
	print len(overview_list_tmp)
	if len(overview_list_tmp) != 2:
		pv_alarm_value = 0	
	else:
		pv_alarm_value = 1
	pv_alarm_name = 'EXP_IB2_RM:Monitor:FileAlarm:bi'
	send_data(pv_alarm_name,pv_alarm_value)

     		

if __name__ == "__main__":
	pv_dict_info = {
		'EXP_IB2_RM:soft:ctrl_cmd':'EXIT',
		'EXP_IB2_RM:soft:run_no':0,
		'EXP_IB2_RM:M1:startExp':'EXIT',	
		'EXP_IB2_RM:M1:runNo':0,
	}
	pv_list_info = pv_dict_info.keys()
	cmd_info = ['CONF','START','STOP','EXIT','CANCEL','GO']
	while 1:
		fo = open('log.dat','a+')
		get_value(pv_list_info)
		overview_alarm(fo)	
		print "\n\n"
                fo.writelines("\n\n")
                fo.close()
		time.sleep(30)

