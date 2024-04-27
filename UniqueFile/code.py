import os
import hashlib

def calculate_md5(file_path):
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Create an MD5 hash object
        md5_hash = hashlib.md5()
        # Read the file in chunks to avoid loading the entire file into memory
        for chunk in iter(lambda: file.read(4096), b''):
            # Update the hash object with the data from the file
            md5_hash.update(chunk)
    # Return the hexadecimal representation of the hash digest
    return md5_hash.hexdigest()

directory = 'chal'  # Replace with the actual directory path

file_names = os.listdir(directory)

for count in range(len(file_names)):
    md5 = calculate_md5("chal/"+file_names[count])
    print(count,md5)

print(file_names[39])