arquivos_entrada="$1"
arquivo_saida="$2"

for f in $(ls -1 | grep "$arquivos_entrada");
do csvcut -c 3,7 "$f"; done > "$arquivo_saida"
