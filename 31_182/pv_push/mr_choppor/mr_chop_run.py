#!/bin/env python
#!-*- coding:utf8 -*-

import os
import time
import json
import tornado
import requests
import datetime
import tornado.gen
import tornado.ioloop

import logging
import sys
from epics import PV
from epics import caget
from datetime import datetime
from apscheduler.schedulers.tornado import TornadoScheduler
logger = logging.getLogger("simple_example")  
logger.setLevel(logging.DEBUG)  
# create file handler which logs even debug messages  
fh = logging.FileHandler("mr_chop_pv.log")  
fh.setLevel(logging.DEBUG)  
# create console handler with a higher log level  
ch = logging.StreamHandler()  
ch.setLevel(logging.ERROR)  
# create formatter and add it to the handlers  
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")  
ch.setFormatter(formatter)  
fh.setFormatter(formatter)  
# add the handlers to logger  
logger.addHandler(ch)  
logger.addHandler(fh) 
mr_chop_pv  = []
cache = {}
interval_time = 30 
err_count = 0


def read_pv_from_file(short_path):
    cur_path = os.getcwd() + '/'
    full_path = cur_path + short_path
    f = open(full_path, 'r')
    result = []
    lines = f.readlines()
    data_list = [word.strip() for word in lines]
    if '' in data_list:
        data_list.remove('')
    return data_list


@tornado.gen.coroutine
def create_record(pv):
    # raise tornado.gen.Return( pv )
    try:
        record = {}
        record['endpoint'] = "mr_chop_pv"
        record['step'] = 60
        record['counterType'] = 'GAUGE'
        record['metric'] = pv
        #tmp = caget(pv, interval_time=interval_time)
        tmp = caget(pv)
        if tmp == None:
            print("not find pv :%s",pv)
            record['value'] = None
            record['timestamp'] = int(time.time())
            logger.debug("%v : %v   None " % (pv, int(time.time())))

        else:
            record['value'] = float(tmp)
            record['timestamp'] = int(time.time())
    except:
        pass
    raise tornado.gen.Return(record)


@tornado.gen.coroutine
def job(pvs, index):
#    if index not in cache.keys(): cache[index] = [None] * len(pvs)
    rets = yield [ tornado.gen.Task(create_record, pv) for pv in pvs ]
#    print(rets)
    requests.post("http://10.1.26.63:1988/v1/push", data=json.dumps(rets))


if __name__ == '__main__':
    mr_chop_pv = read_pv_from_file('mr_chop_pvlist.txt')
    logger.debug('======begin==========')
    sched = TornadoScheduler()
    sched.add_job(job, 'interval', seconds=interval_time, max_instances=6, kwargs={"pvs": mr_chop_pv, "index": 2})
    sched.start()
    tornado.ioloop.IOLoop.instance().start()
