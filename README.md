# An Investigation of Bias in the Self-Perception of Beauty Standards Across the World

## Running the code

### test_llama_1.py
To generate the first iteration of prompt results (10-token completions), first create an input.tsv file (prompts) and an output.tsv file (prompt results). Then, enter the following text into the command line:
"python test_llama_1.py input_tsv output_tsv"

### test_llama_2.py
To generate the second iteration of prompt results (first-word completions), create an output.tsv file (updated prompt results). Use the output of the first iteration as the input.tsv file. Then, enter the following text into the command line:
"python test_llama_2.py input_tsv output_tsv"

### llama_scoring_1.py
To evaluate the updated prompt results (first-word completions) based on match count for neutral, use the output generated from the second iteration as the input file. Then, enter the following text into the command line:
"python llama_scoring_1.py path/to/file.tsv"

### llama_scoring_2.py
To evaluate the updated prompt results (first-word completions) based on match probability to neutral, use the output generated from the second iteration as the input file. Then, enter the following text into the command line:
"python llama_scoring_2.py path/to/file.tsv"
