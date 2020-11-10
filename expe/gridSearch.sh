#! /bin/bash 
epochs="40"
dropouts="0.5"
for fm in ./featModel/*; do
	for epoch in $epochs; do
		for drop in $dropouts; do
			./launch_grid.sh $fm $epoch $drop
		done
	done
done
