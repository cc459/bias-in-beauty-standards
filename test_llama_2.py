import query_llama
import csv
import sys
import re

# Replace entire completion with the first word of the completion
def process_tsv(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file_in, \
         open(output_file_path, 'w', encoding='utf-8') as file_out:
        
        for line in file_in:
            fields = line.strip().split('\t')  # Split the line into fields
            if fields:
                last_column = fields[-1]
                match = re.search(r'\b\w+\b', last_column) # Use regular expressions to find the first word
                first_word = match.group(0) if match else ""
                fields[-1] = first_word  # Replace the completion with the first word of the completion
                revised_line = '\t'.join(fields)  # Reconstruct the line
                file_out.write(revised_line + '\n')  # Write the revised line to the output file

def main():
    if len(sys.argv) < 3:
        print("Usage: python test_llama_2.py input_tsv output_tsv")
        sys.exit(1)

    input_tsv = sys.argv[1]
    output_tsv = sys.argv[2]

    try:
        process_tsv(input_tsv, output_tsv)
        print(f"Processed completions written to {output_tsv}")
    except Exception as e:
        print({e})

if __name__ == "__main__":
    main()