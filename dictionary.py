import hashlib

pass_hash = input('Enter the password hash: ')
dictionary_path = input('Enter the filepath to your dictionary: ')
dict = open(dictionary_path, 'r')

dict_lines = dict.readlines()

for line in dict_lines:
    line = line.strip('\n')
    hash = hashlib.md5(line.encode()).hexdigest()
    if (pass_hash == hash):
        print("Found password: " + line)
        break