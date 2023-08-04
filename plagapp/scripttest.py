from plagiarism_detector import plagiarism_detector

# Read the contents of 'test11.txt' and 'test2.txt'
with open('test11.txt', 'r', encoding='utf-8') as file:
    document1 = file.read()

with open('test2.txt', 'r', encoding='utf-8') as file:
    document2 = file.read()

is_plagiarized = plagiarism_detector(document1, document2)
print(f"Plagiarism Detected: {is_plagiarized}")
