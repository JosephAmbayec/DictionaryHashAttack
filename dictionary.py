import hashlib
import datetime

# Input
pass_hash = input('Enter the MD5 hash: ')
dictionary_path = input('Enter the filepath to your dictionary (dict.txt): ')

# Start Timer
start = datetime.datetime.now()

# Read Dictionary
dict = open(dictionary_path, 'r')
dict_lines = dict.readlines()

# Main Loop
for line in dict_lines:
    line = line.strip('\n')
    hash = hashlib.md5(line.encode()).hexdigest()
    if (pass_hash == hash):
        print("Found password: " + line)
        break

# End Timer
end = datetime.datetime.now()
total = end - start

print(f"It took {total.total_seconds()} seconds to run...")
input("Press Enter to Close...")
