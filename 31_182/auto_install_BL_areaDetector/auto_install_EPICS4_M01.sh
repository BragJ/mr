#!/bin/bashi

# areaDetector
cd /opt/egcs/epics/EPICS4/Neutron_Source_M01/neutronsDemoServer/srcIoc/src
echo "`pwd`"
sed -i "s/neutrons/monitor1/g" devNeutrons.cpp

cd ../../src/
sed -i "s/"neutrons"/"monitor1"/g" neutronServerMain.cpp
#exit 1

cd ..
make -j4

cd iocBoot/neutrons
sed -i "s/demo/monitor1/g" st.cmd


