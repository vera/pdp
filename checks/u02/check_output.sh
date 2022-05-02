for y in 1 5 10 999
do
	echo $y | ./$1 | grep -q `expr 2 \* 4 \* 4 / $y`

	if [ ! $? -eq 0 ]; then
		echo "	"
		echo "###############################################################################"
		echo "	"
		echo "Die Ausgabe deines Programms ist nicht richtig:" | fold -s
		echo "	"
		echo "Nutzereingabe: $y"
		echo "	"
		echo "Deine Ausgabe: "
		echo "	"
		echo $y | ./$1
		echo "	"
		echo "enthält nicht den erwarteten Wert: `expr 2 \* 4 \* 4 / $y`"
		echo "	"
		echo "###############################################################################"
		exit 1
	fi
done

echo "	"
echo "###############################################################################"
echo "	"
echo "Super! Die Ausgabe deines Programms ist korrekt." | fold -s
echo "	"
echo "###############################################################################"

