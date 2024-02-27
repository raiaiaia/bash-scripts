termo="$1"
arquivo="$2"

cp "{arquivo}.csv" "{arquivo}_backup.csv" 
sed -i "s/$termo//g" "${arquivo}.csv"
