import json
import random
import string

# Function to split a word into two parts
def split_word(word):
    length = len(word)
    if length % 2 == 0:
        mid = length // 2
    else:
        mid = length // 2 + 1
    return word[:mid], word[mid:]

# Function to generate a random two-character prefix
def generate_prefix():
    return ''.join(random.choice(string.ascii_letters) for _ in range(2))

# Function to perform encryption
def encrypt(content):
    words = content.split()
    encrypted_words = []
    for word in words:
        prefix = generate_prefix()
        first_part, second_part = split_word(word)
        encrypted_word = prefix + second_part + first_part
        encrypted_words.append(encrypted_word)
    return ' '.join(encrypted_words)

# Function to perform decryption
def decrypt(content):
    words = content.split()
    decrypted_words = []
    for word in words:
        prefix = word[:2]
        word_without_prefix = word[2:]
        decrypted_word = word_without_prefix[len(word_without_prefix)//2:] + word_without_prefix[:len(word_without_prefix)//2]
        decrypted_words.append(decrypted_word)
    return ' '.join(decrypted_words)

# Encryption
with open('data.json', 'r') as file:
    data = json.load(file)

for entry in data:
    if 'content' in entry:
        entry['content'] = encrypt(entry['content'])

with open('data_encrypted.json', 'w') as file:
    json.dump(data, file, indent=4)

# Decryption
with open('data_encrypted.json', 'r') as file:
    data = json.load(file)

for entry in data:
    if 'content' in entry:
        entry['content'] = decrypt(entry['content'])

with open('data_decrypted.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Encryption and decryption complete.")
