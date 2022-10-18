#!/bin/bash
#source /home/egcs/.bash_profile
export EPICS_CA_ADDR_LIST="10.1.31.182:7000 10.1.31.182:8100"
echo $EPICS_CA_ADDR_LIST
python initial_checkout.py
