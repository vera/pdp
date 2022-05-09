gcc -E -dM -include stdio.h - < /dev/null > stdio_macros
gcc -E -dM $1.c > student_macros
diff stdio_macros student_macros | grep -E "^> #define[[:space:]]+[a-zA-Z0-9_]*[[:space:]]+$2$" > /dev/null

if [ ! $? -eq 0 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm definiert nicht wie gefordert eine symbolische Konstante mit dem Wert $2." | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm definiert eine symbolische Konstante mit dem Wert $2." | fold -s
	echo "	"
	echo "###############################################################################"
fi

