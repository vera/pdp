python3 $1 &> sa_output.txt

if [ ! $? -eq 0 ]; then	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm erfüllt die Anforderungen aus der Aufgabenstellung nicht:" | fold -s
	echo "	"
	cat sa_output.txt
	echo "	"
	echo "###############################################################################"
	exit 1
else	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm erfüllt die Anforderungen aus der Aufgabenstellung." | fold -s
	echo "	"
	echo "###############################################################################"
fi
