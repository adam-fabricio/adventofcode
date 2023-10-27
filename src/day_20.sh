#!/usr/bin/env bash
#
#  day_20.sh
#
#---------------------------------Start Date----------------------------------#
#
#    1698098317 -> 23/10/23 18:58:37
#
#----------------------------------Data input---------------------------------#
if [[ "$1" == test ]]
then
    data_input="data/day_20_test"
    echo Use test data input
else
    data_input="data/day_20"
    echo "use source data input"
fi
#----------------------------------Read data input----------------------------#
declare -a list
declare -i line_number=1

while read line
do
	#  cria lista
	list+=("$line|1")
done < "$data_input"
#-----------------------------------functions---------------------------------#
move_item(){
	position=$i
	normalized_value=$(( value % ( lenght - 1 )  ))
	[[ value -lt 0 ]] && normalized_value=$(( lenght + normalized_value -1))
	new_position=$(( position + normalized_value))
	if [[ new_position -ge $(($lenght)) && value -gt 0 ]]; then
		new_position=$((new_position%(lenght) +1 ))
	fi

	#  move o valor
	#  remove item of list
	list=(${list[@]::$position} ${list[@]:$((position+1))})
	#  add item to list
	list=(${list[@]::$new_position} "$value|$flag" ${list[@]:$new_position})

}
#-----------------------------------main--------------------------------------#
#  tamanho da lista
lenght=${#list[@]}

#  iterar sobre os itens da lista

p=0

for (( i = 0; i < lenght; i++ )); do
	IFS="|" read value flag <<< ${list[$i]}
	echo $i
	#  if number is alredy moved continue
	[[ flag -eq 0 ]] && continue
	#  set item as read
	flag=0
	list[$i]="$value|$flag"
	# if number is 0 do not move
	[[ value -eq 0 ]] && continue
	move_item
	let i--
	[[ p -eq 0 ]] && declare -p list && let p++
	let p++
done
echo $p
for (( i = 0; i < lenght; i++ )); do
	IFS="|" read value flag <<< ${list[$i]}
	[[ value -eq 0 ]] && id0=$i && break
done

declare -p list
echo "id0=$id0"
results=( ${list[$(((id0+1000)%lenght))]%|*} \
	${list[$(((id0+2000)%lenght))]%|*} \
	${list[$(((id0+3000)%lenght))]%|*} )

echo ${results[@]}

sum_result=0
for result in ${results[@]}; do
	sum_result=$((sum_result + result ))
done
echo "result= $sum_result"


