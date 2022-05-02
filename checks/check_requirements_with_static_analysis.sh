python3 $1 &> sa_output.txt

if [ ! $? -eq 0 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm erfüllt mindestens eine Anforderung aus der Aufgabenstellung nicht:" | fold -s
	echo "	"
	cat sa_output.txt | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm erfüllt alle Anforderungen aus der Aufgabenstellung:" | fold -s
	echo "	"
	cat sa_output.txt | fold -s
	echo "	"
	echo "###############################################################################"
fi
