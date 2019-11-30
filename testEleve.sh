#!/bin/bash

if [[ "$3" != "" ]]; then	
python3 $1 <<EOF
$2
$3
EOF
else
python3 $1 <<EOF
$2
EOF
fi

statut=$?
if [[ $statut != "0" ]] ; then
	echo Une erreur est survenue
	exit $statut
fi

echo ""
#Popur que le fichier est bien une dernière ligne:
echo "" >> $3

grep 'tracer(' $3
tracer_edit=$?
sed -i.bak -e 's/tracer(.+)/tracer(False)/g' $3
echo tracer_edit=$tracer_edit

grep 'speed(' $3
speed_edit=$?
sed -i.bak -e 's/speed(.+)/speed(0)/g' $3
echo speed_edit=$speed_edit

grep exitonclick $3
exit_edit=$?
sed -i.bak -e 's/exitonclick()/update();done();exitonclick()/g' $3
echo exit_edit=$exit_edit

if [[ "$tracer_edit" != "0" ]]; then
	cp $3 $3.tracer
	grep -B 100000000 import $3.tracer > $3
	echo "tracer(False)" >> $3
	echo "speed(False)" >> $3
	grep -A 100000000 import $3.tracer |grep -v import >> $3
	echo "" >> $3
	if [[ "$exit_edit" != "0" ]]; then
		echo "update() ; done() ; exitonclick() ; " >> $3
	fi
fi

python3 $3
