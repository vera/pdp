if [ ! -s $1 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Die Datei $1 ist noch leer." | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi

gcc -Wall -Werror $1 -o $2 &> /dev/null

if [ ! $? -eq 0 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm kompiliert nicht ohne Fehlermeldungen und Warnungen. Kompiliere das Programm selbst mit folgendem Befehl:" | fold -s
	echo "	"
	echo "gcc -Wall $1"
	echo "	"
	echo "Behebe dann alle Fehlermeldungen und Warnungen."
	echo "	"
	echo "###############################################################################"
	exit 1
else	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm kompiliert ohne Fehlermeldungen und Warnungen." | fold -s
	echo "	"
	echo "###############################################################################"
fi
