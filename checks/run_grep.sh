if [ -z "$2" ]; then
	grep -E -f $1 output.txt -i &> /dev/null
else
	NUM_MATCHED_LINES=`grep -E -f $1 output.txt -i 2> /dev/null | wc -l`
	[ $NUM_MATCHED_LINES -gt 1 ]
fi

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
	sed "s/\[\+[^]]\+\]\++\?/ /g" $1
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
	sed "s/\[\+[^]]\+\]\++\?/ /g" $1
	echo "	"
	echo "###############################################################################"
fi
