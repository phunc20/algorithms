#!/bin/sh

names=("verne" "bobsey" "lewis" "arabian" "churchill" "onemillion" "tenmillion" "shakespeare" "bacon")
mkdir -p dataset

head="https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/"
#for i in $(seq 1 ${#names[@]}); do
for i in ${!names[@]}; do
  j=$(( i+1 ))
  #j=`expr $i+1`
  filename="t${j}.${names[$i]}.txt"
  printf "Downloading ${head}${filename} ...\n"
  curl -o "dataset/${filename}" "${head}${filename}" 
  #curl -o "dataset/" "${head}${filename}" 
  #curl -OL "${head}${filename}" 
done
