#!/bin/bash
export EPICS_CA_ADDR_LIST="10.1.31.182:7000 10.1.31.181 10.1.31.183 10.1.29.102"
echo $EPICS_CA_ADDR_LIST
python monitor_run_info_check.py




