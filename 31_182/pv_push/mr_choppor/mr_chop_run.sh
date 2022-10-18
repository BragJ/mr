#!/bin/bash
export EPICS_CA_ADDR_LIST="10.1.31.166 10.1.31.183"
echo $EPICS_CA_ADDR_LIST
python3 mr_chop_run.py 
