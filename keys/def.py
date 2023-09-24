import json
import random
import string


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


# Decryption
with open('data_encrypted.json', 'r') as file:
    data = json.load(file)

for entry in data:
    if 'content' in entry:
        entry['content'] = decrypt(entry['content'])

with open('data_decrypted.json', 'w') as file:
    json.dump(data, file, indent=4)

print("decryption complete.")
