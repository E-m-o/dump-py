def read_notes():
    
    filepath = input('Enter file name\n') + '.txt'

    word = input('Enter word to be searched\n')

    with open(filepath, 'r') as fi:
        lines = fi.readlines()
    
    for line in lines:
        if word in line.strip().split(' '):
            print(line)

