#!bin/bash

cd $AREA_M1_PATH/ADnEDApp/src/
sed -i "s/7110000/7110000/g" ADnED.cpp

cp $AREA_M1_PATH/ADnEDApp/src/ADnED.cpp $AREA_M2_PATH/ADnEDApp/src/
cp $AREA_M1_PATH/ADnEDApp/src/ADnED.h $AREA_M2_PATH/ADnEDApp/src/
cd $AREA_M2_PATH/ADnEDApp/src/
sed -i "s/7110000/8110000/g" ADnED.cpp


cp $AREA_M1_PATH/ADnEDApp/src/ADnED.cpp $AREA_M3_PATH/ADnEDApp/src/
cp $AREA_M1_PATH/ADnEDApp/src/ADnED.h $AREA_M3_PATH/ADnEDApp/src/
cd $AREA_M3_PATH/ADnEDApp/src/
sed -i "s/7110000/9110000/g" ADnED.cpp
