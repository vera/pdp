# Input 0 to cause runtime error, then input 1 to end loop if there is error handling with recovery
python3 -c 'print("0\n1")' | ./$1

if [ $? -eq 136 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm enthält keine funktionierende Fehlerbehandlung. Es ist aufgrund einer ungültigen Operation (Division durch 0) beendet worden." | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm hat den Laufzeitfehler behandelt." | fold -s
	echo "	"
	echo "###############################################################################"
fi
