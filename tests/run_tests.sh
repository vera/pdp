./$1 &> tests_output.txt

if [ ! $? -eq 0 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Dein Programm besteht nicht alle Tests:" | fold -s
	echo "	"
	cat tests_output.txt | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Super! Dein Programm besteht alle Tests." | fold -s
	echo "	"
	echo "###############################################################################"
fi
