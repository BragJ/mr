#!bin/bash

cd  $AREA_M3_PATH
cd ../
git init
git add -A
git commit -m "first commit"
git remote add origin git@github.com:BragJ/areaDetector_BL18_M03.git
git push -u origin master

