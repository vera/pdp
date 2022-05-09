#TODO Test für Nutzereingabe -999999999, 0, 1, 256, 999999999 (jeweils gefolgt von 0)
# TODO Test für Nutzereingabe nicht gefolgt von 0 -> läuft weiter

# Input 0 to end loop immediately
python3 -c 'print("0")' | timeout 3 ./$1 > /dev/null

if [ $? -eq 0 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm hat sich nach Eingabe von 0 beendet." | fold -s
	echo "	"
	echo "###############################################################################"
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm hat sich nach Eingabe von 0 nicht sofort beendet!" | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi

# Input valid number and no 0 to check if loop continues running
python3 -c 'print("256")' | timeout 3 ./$1 > /dev/null

if [ $? -eq 124 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm hat sich nicht beendet, als keine 0 eingegeben wurde." | fold -s
	echo "	"
	echo "###############################################################################"
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm hat sich beendet, obwohl keine 0 eingegeben wurde!" | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi

# Input valid numbers to receive square values, then input 0 to end loop
echo ""
for y in {1..999}
do
	echo -ne "Teste mit gültigen Eingaben ($y/999)...\r"
	python3 -c "print(\"$y\n0\")" | timeout 3 ./$1 > output.txt
	grep -q `expr $y \* $y` output.txt

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
		cat output.txt
		echo "	"
		echo "enthält nicht den erwarteten Wert: `expr $y \* $y`"
		echo "	"
		echo "###############################################################################"
		exit 1
	fi
done

echo "	"
echo "	"
echo "###############################################################################"
echo "	"
echo "Super! Dein Programm hat für alle gültigen Eingaben das korrekte Ergebnis ausgegeben und sich dann nach Eingabe von 0 beendet." | fold -s
echo "	"
echo "###############################################################################"

# Input -999999999 to cause error recovery, then input valid number, then input 0 to end loop
python3 -c 'print("-999999999\n256\n0")' | ./$1 > output_large_negative.txt

if [ $? -eq 0 ]; then
	grep -q 65536 output_large_negative.txt
	if [ $? -eq 0 ]; then
		echo "	"
		echo "###############################################################################"
		echo "	"
		echo "Super! Dein Programm hat nach einer negative Eingabe Fehlerbehandlung mit Recovery durchgeführt und sich dann nach Eingabe von 0 beendet." | fold -s
		echo "	"
		echo "###############################################################################"
	fi
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm hat nach einer negative Eingabe keine Fehlerbehandlung mit Recovery durchgeführt!" | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi

# Input 999999999 to cause error recovery, then input valid number, then input 0 to end loop
python3 -c 'print("999999999\n256\n0")' | ./$1 > output_large_positive.txt

if [ $? -eq 0 ]; then
	grep -q 65536 output_large_positive.txt
	if [ $? -eq 0 ]; then
		echo "	"
		echo "###############################################################################"
		echo "	"
		echo "Super! Dein Programm hat nach einer zu großen Eingabe Fehlerbehandlung mit Recovery durchgeführt und sich dann nach Eingabe von 0 beendet." | fold -s
		echo "	"
		echo "###############################################################################"
	fi
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm hat nach einer zu großen Eingabe keine Fehlerbehandlung mit Recovery durchgeführt!" | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi
