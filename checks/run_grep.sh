grep -E -f $1 output.txt -i &> /dev/null

if [ ! $? -eq 0 ]; then	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Die Ausgabe deines Programms enthält nicht die geforderte Ausgabe." | fold -s
	echo "	"
	echo "Deine Ausgabe lautet:"
	echo "	"
	cat output.txt
	echo "	"
	echo "Die geforderte Ausgabe lautet:"
	echo "	"
	sed "s/\[\[:space:\]\]+/ /g" $1
	echo "	"
	echo "(Unterschiede in den Leerzeichen und evtl. zusätzliche Ausgaben werden ignoriert.)" | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
else	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Die Ausgabe deines Programms enthält die geforderte Ausgabe." | fold -s
	echo "	"
	echo "Deine Ausgabe lautet:"
	echo "	"
	cat output.txt
	echo "	"
	echo "Die geforderte Ausgabe lautet:"
	echo "	"
	sed "s/\[\[:space:\]\]+/ /g" $1
	echo "	"
	echo "###############################################################################"
fi
