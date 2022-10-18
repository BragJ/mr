import   datetime, time, json, os
import requests
import time
from epics import caget,caput

def get_value(pv_list_info):
	for pv_name in pv_list_info:
		if pv_name != 'EXP_IB2_RM:soft:ctrl_cmd':
			pv_value  = caget(pv_name)
			pv_dict_info[pv_name] = pv_value  
			#print pv_name,'=', pv_dict_info[pv_name]
		else:
			print pv_name,'=',pv_value
			pv_value  = caget(pv_name)
			pv_dict_info[pv_name] = cmd_info[pv_value]
def overview_alarm(fo,resetFlagNum):
	record_data=[]
	overview_list = []  
	for k in sorted(pv_dict_info):
		overview_list.append(pv_dict_info[k]) 
 	overview_list_tmp = list(set(overview_list))
	print overview_list
	print len(overview_list_tmp)
	#print pv_list_info
	#print cmd_info.index(overview_list[4]) - cmd_info.index(overview_list[1])
	'''
	if len(overview_list_tmp) != 2:
		print "it's not ok~~~"
		fo.writelines(str(overview_list))
		run_no_list =set([overview_list[5],overview_list[0],overview_list[2]])
		if len(run_no_list) == 1:
			resetFlagNum = resetFlagNum + 1
			#if resetFlagNum > 2:
			if cmd_info.index(overview_list[4]) - cmd_info.index(overview_list[1]) <=3:
				caput(pv_list_info[1],overview_list[4]) 
				fo.writelines("reset the M2 cmd!!\n")
			if cmd_info.index(overview_list[4]) - cmd_info.index(overview_list[3]) <=3:
				caput(pv_list_info[3],overview_list[4]) 
				fo.writelines("reset the M3 cmd!!\n")
		fo.writelines("\n\n")
		if  overview_list[5] > overview_list[0]:
			caput(pv_list_info[0],overview_list[5])	
		if  overview_list[5] > overview_list[2]:
			caput(pv_list_info[2],overview_list[5])		
	else:
		print "it's ok~~~"
		resetFlagNum = 0
	'''
     		

if __name__ == "__main__":
        pv_dict_info = {
                'EXP_IB2_RM:soft:ctrl_cmd':'EXIT',
                'EXP_IB2_RM:soft:run_no':0,
                'EXP_IB2_RM:M1:startExp':'EXIT',
                'EXP_IB2_RM:M1:runNo':0,
        }
	pv_list_info = sorted(pv_dict_info.keys())
	print pv_list_info
        resetFlagNum = 0
	#cmd_info = ['CONF','START','STOP','EXIT','CANCEL','GO']
	cmd_info = ['CONF','START','STOP','RESET']
	fo = open('log.dat','a+')
	while 1:
		get_value(pv_list_info)
		overview_alarm(fo,resetFlagNum)	
		print "\n\n"
		time.sleep(2)
	fo.close()

