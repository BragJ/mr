#!/bin/bashi

# areaDetector
cd /opt/egcs/epics/EPICS4/Neutron_Source_M02/neutronsDemoServer/srcIoc/src
echo "`pwd`"
sed -i "s/monitor1/monitor2/g" devNeutrons.cpp

cd ../../src/
sed -i "s/"monitor1"/"monitor2"/g" neutronServerMain.cpp
#exit 1

cd ..
make -j4

cd iocBoot/neutrons
sed -i "s/monitor1/monitor2/g" st.cmd


