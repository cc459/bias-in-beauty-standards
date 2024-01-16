import query_llama
import csv
import sys

def evaluate_completions(input_tsv, output_tsv):
    # Read the input TSV file
    with open(input_tsv, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')
        lines = list(reader)

    # Process each prompt and write results to the output TSV file
    with open(output_tsv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='\t')

        for line in lines:
            if len(line) >= 3:  # Check number of columns
                prompt = line[2]  # Third column as the prompt
                completion = query_llama.completion_query(prompt)  # Process the prompt
                line.append(completion)  # Add the completion to the original line
                writer.writerow(line)  # Write the updated line to the output file

def main():
    if len(sys.argv) < 3:
        print("Usage: python test_llama_1.py input_tsv output_tsv")
        sys.exit(1)

    input_tsv = sys.argv[1]
    output_tsv = sys.argv[2]

    try:
        evaluate_completions(input_tsv, output_tsv)
        print(f"Processed completions written to {output_tsv}")
    except Exception as e:
        print({e})

if __name__ == "__main__":
    main()