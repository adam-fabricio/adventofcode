#!/usr/bin/env bash
#
#  day_19.sh
#
#---------------------------------Start Date----------------------------------#
#
#    1679265755 -> 19/03/23 19:42:35
#
#----------------------------------Data input---------------------------------#
if [[ "$1" == test ]]
then
    data_input="data/day_19_test"
    echo Use test data input
else
    data_input="data/day_19"
    echo "use source data input"
fi
#----------------------------------Read data input----------------------------#
function calc_resource () {
	local time=$1
	local robots=( $2 $3 $4 $5 )
	local resources=( $6 $7 $8 $9 )
	local purchase_list=( "none" )
	local time_elapsed=0

	#  Pontos de parada
	let time++
	time_left=$(( time_limit - time ))
	echo "$time->robots( ${robots[@]} )->resources( ${resources[@]} )"
	[[ robots[2] -le 1 ]] && [[ time -gt 12 ]] && return
	[[ time -gt obsidian_robot[2] ]] && [[ robots[1] -eq 0 ]] && return

	[[ time -gt geode_robot[3] ]] && [[ robots[2] -eq 0 ]] && return

	[[ resources[0] -ge ore_robot[0] ]] && purchase_list+=( "ore_robot" )
	[[ resources[0] -ge clay_robot[0] ]] && purchase_list+=( "clay_robot" )
	[[ resources[0] -ge obsidian_robot[0] ]] &&\
		[[ resources[1] -ge obsidian_robot[1] ]] &&\
		purchase_list+=( "obsidian_robot" )
	[[ resources[0] -ge geode_robot[0] ]] &&\
		[[ resources[2] -ge geode_robot[2] ]] &&\
		purchase_list+=( "geode_robot" )
	
	for i in {0..3}; do
		resources[$i]=$(( resources[$i] + robots[$i] ))
	done
	
	[[ crack_geode -lt resources[3] ]] && crack_geode=${resource[3]}

	[[ time_left -le 0 ]] && return
	for purchase in ${purchase_list[@]}; do
		case "$purchase" in
			none)
				calc_resource $time ${robots[@]} ${resources[@]}
				;;
			ore_robot)
				new_robots=( ${robots[@]} )
				new_resources=( ${resources[@]} )
				let new_robot[0]++
				new_resources[0]=$(( new_resources[0] - ore_robot[0] ))
				calc_resource $time ${new_robots[@]} ${new_resources[@]}
				;;
			clay_robot)
				new_robots=( ${robots[@]} )
				new_resources=( ${resources[@]} )
				let new_robots[1]++
				new_resources[0]=$(( new_resources[0] - clay_robot[0] ))	
				calc_resource $time ${new_robots[@]} ${new_resources[@]}
				;;
			obsidian_robot)
				new_robots=( ${robots[@]} )
				new_resources=( ${resources[@]} )
				let new_robots[2]++
				new_resources[0]=$(( new_resources[0] - obsidian_robot[0] ))
				new_resources[1]=$(( new_resources[1] - obsidian_robot[1] ))
				calc_resource $time ${new_robots[@]} ${new_resources[@]}
				;;
			geode_robot)
				new_robots=( ${robots[@]} )
				new_resources=( ${resources[@]} )
				new_resources[0]=$(( new_resources[0] - geode_robot[0] ))
				new_resources[2]=$(( new_resources[2] - geode_robot[2] ))
				let new_robots[3]++
				calc_resource $time ${new_robots[@]} ${new_resources[@]}
				;;
		esac
	done
}


id=1
while read -a line; do
	time_limit=24
	crack_geode=0
	ore_robot=( "${line[6]}" )
	clay_robot=( "${line[12]}" )
	obsidian_robot=( "${line[18]}" "${line[21]}" "1" )
	geode_robot=( "${line[27]}" "0" "${line[30]}" "1" )
	for (( i=0; i < geode_robot[2]; geode_robot[3]++)); do
		i=$(( geode_robot[3] + i ))
	done
	geode_robot[3]=$(( time_limit - geode_robot[3] + 1 ))
	for (( i=0; i < obsidian_robot[1]; obsidian_robot[2]++ )); do
		i=$(( obsidian_robot[2] + i ))
	done
	obsidian_robot[2]=$(( geode_robot[3] - obsidian_robot[2] + 1 ))

	echo "$id -> ore_robot[ ${ore_robot[@]} ] clay_robot[ ${clay_robot[@]} ]\
 obsidian_robot[ ${obsidian_robot[@]} ] geode_robot[ ${geode_robot[@]} ]"
	calc_resource 0 1 0 0 0 0 0 0 0
	echo $crack_geode

	let id++
	exit
done < "$data_input"
#--------------------------------------|--------------------------------------#
