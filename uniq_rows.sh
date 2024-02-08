column_number=1
input_file="$1"
output_file="$2"
awk -F',' '!seen[$'$column_number']++' "$input_file" > "$output_file"
