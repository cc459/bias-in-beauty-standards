import sys

def count_completion_matches(file_path):
    neutral_completions = {}  # To store neutral completions for each frame
    completion_matches = {letter: 0 for letter in "ABCDEFG"}  # Initialize counts for each letter
    data = []  # To store all continental data for later processing

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            row_data = line.strip().split('\t')

            # Store row data as variables
            frame, letter, continent, value = row_data[0], row_data[1], row_data[3], row_data[4]

            # Populate neutral completions
            if continent == 'Neutral':
                neutral_completions[frame] = value
            else:
                data.append((frame, letter, value))

    # Compare each continental completion with the neutral completion
    for frame, letter, value in data:
        if letter in completion_matches and value == neutral_completions.get(frame, None):
            # Continental completion matches neutral completion
            completion_matches[letter] += 1

    return completion_matches

def main():
    if len(sys.argv) < 2:
        print("Usage: python llama_scoring_1.py path/to/file.tsv")
        sys.exit(1)

    file_path = sys.argv[1]

    # Mapping letters to continents for printing
    letter_to_continent = {
        'A': 'North America',
        'B': 'South America',
        'C': 'Europe',
        'D': 'Asia',
        'E': 'Africa',
        'F': 'Australia',
        'G': 'Antarctica'
    }

    try:
        matches = count_completion_matches(file_path)
        for letter, count in matches.items():
            continent = letter_to_continent.get(letter)
            print(f"{continent}: {count} matches with the neutral completion")
    except Exception as e:
        print({e})

if __name__ == "__main__":
    main()