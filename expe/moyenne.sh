#! /bin/bash
moyenne=0
path=$1
nbfile=$(ls $path -lRrt |grep "\.res" | wc -l)
for file in $path/*.res 
do
	tmp=$(cat $file | awk '{print $2}')
	echo $tmp
	moyenne=$(python3 -c  "print( $moyenne + $tmp)")
done
echo moyenne 1
python3 -c "print($moyenne/$nbfile)" > $path/moyenne

moyenne=0
for file in $path/*.res 
do
	tmp=$(cat $file | awk '{print $3}')
	echo $tmp
	moyenne=$(python3 -c  "print( $moyenne + $tmp)")
done
echo moyenne 2
python3 -c "print($moyenne/$nbfile)" >> $path/moyenne
