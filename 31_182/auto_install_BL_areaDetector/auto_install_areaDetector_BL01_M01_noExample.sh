#!/bin/bashi

# areaDetector
cd /opt/egcs/epics/modules/areaDetector_BL01_M01/configure
echo "`pwd`"
sed -i "s/areaDetector_BL18_M01/areaDetector_BL01_M01/g" RELEASE_PATHS.local
cd ../
make clean
make -j4

#ADnED
cd ADnED/example/configure
echo "`pwd`"
sed -i "s/areaDetector_BL18_M01/areaDetector_BL01_M01/g" RELEASE

cd ../../
make clean 
make -j4

#setup.sh

cd example
sed -i "s/BL18/BL01/g" setup_example.sh
#sed -i "s/monitor1/monitor2/g"  setup_example.sh

#macro
cd exampleApp/Db
echo "`pwd`"
#sed -i "s/M1/M2/g" example.substitutions

#example.db
cd ../../iocBoot/iocexample
echo "`pwd`"
sed -i "s/areaDetector_BL18_M01/areaDetector_BL01_M01/g" envPaths

#sed -i "s/M1/M2/g" st.cmd
sed -i "s/areaDetector_BL18_M01/areaDetector_BL01_M01/g" st.cmd
cd ../../
#make -j4


cd db

sed -i "s/BL18/BL01/g" example.db
#sed -i "s/M1/M2/g" add_record.db
#chmod ugo+w example.db
#cat add_record.db >> example.db


