import json


def get_number_of_words(read_file):
	return len(read_file.split())

def get_character_count(read_file):
	char_count = {}
	for char in read_file:
		if not char.isalpha():
			continue
		if char_count.get(char.lower()):
			char_count[char.lower()] += 1
		else:
		    char_count[char.lower()] = 1
	return char_count


def main():
	frankenstein_file = "books/frankenstein.txt"
	file_contents = ""
	with open(frankenstein_file) as f:
		file_contents = f.read()
	print(get_number_of_words(file_contents))
	print(json.dumps(get_character_count(file_contents), indent=2))


if __name__ == "__main__":
    main()

