#!/bin/bash
#Showcases a build using bash
echo "Welcome!"
firstline=$(head -n 1 source/changelog.md)

read -a splitfirstline <<< $firstline

version=${splitfirstline[1]}

echo "You are building version" $version

echo 'Do you want to continue? (Enter "1" for yes, "0" for no)'

read versioncontinue

if [ $versioncontinue -eq 1 ]
then
  echo "OK"
  
  for file in source/*
  do
    echo $file
    
    if [ $file == "source/secretinfo.md" ]
  then
    echo "Not copying" $file
  else
    echo "Copying" $file
    cp $file build
  fi
  done
  
else
  echo "Come back when you're ready"
fi

cd build
echo "Build version $version contains"
ls
cd ../
