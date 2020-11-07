#! /bin/bash 
epochs="10 20 30 40"
dropouts="0.3 0.4 0.5"
for fm in ./featModel/*; do
	for epoch in $epochs; do
		for drop in $dropouts; do
			./launch_grid.sh $fm $epoch $drop
		done
	done
done
