def get_freq_counts(encrypted_message):
    # Initialize a dictionary to store the frequency counts of each character
    freq_counts = {}
    
    # Loop over each character in the encrypted message
    for char in encrypted_message:
        # If the character is already in the dictionary, increment its count
        if char in freq_counts:
            freq_counts[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            freq_counts[char] = 1
    
    # Return the dictionary of frequency counts
    return freq_counts
  
# Read the encrypted message from ciphertext.txt
with open('ciphertext.txt', 'r') as f:
    encrypted_message = f.read().strip()

# Read the frequency count from freq.txt and convert it to a dictionary
with open('freq.txt', 'r') as f:
    freq_str = f.read().strip()
    freq_dict = {}
    for line in freq_str.split('\n'):
        char, count = line.split(':')
        if char.strip() == '':
            freq_dict[' '] = int(count.strip())
        else:
            freq_dict[char.strip()] = int(count.strip())

# Get the frequency counts of the encrypted message
encrypted_freq_counts = get_freq_counts(encrypted_message)

# Sort the encrypted frequency counts by count in descending order
encrypted_freq_counts = {k: v for k, v in sorted(encrypted_freq_counts.items(), key=lambda item: item[1], reverse=True)}

# Sort the frequency count by count in descending order
freq_dict = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)}

# Create a mapping from the most frequent character in the encrypted message to the most frequent character in the frequency count
mapping = {}
for i, char in enumerate(encrypted_freq_counts.keys()):
    if i < len(freq_dict):
        mapping[char] = list(freq_dict.keys())[i]

# Decrypt the message using the mapping
decrypted_message = ''
for char in encrypted_message:
    if char in mapping:
        decrypted_message += mapping[char]
    else:
        decrypted_message += char

# Print the decrypted message
print(decrypted_message)
