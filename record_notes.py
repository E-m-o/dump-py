def record_notes():
    
    filepath = input('Enter file name\n') + '.txt'

    line = str()
    e = 'n'        

    with open(filepath, 'a') as fo:
        while True:
            line = input('-> ')
            if line == 'exit':
                e = input('-----------------------------------------------\nAre you sure you want to exit the program?(y/n)\n-----------------------------------------------\n-> ')
            
                if e == 'y':
                    print('-----------------------------------------------\n                  Exiting program\n-----------------------------------------------''')
                    fo.close()
                    break
                else:
                    x = input('-----------------------------------------------\nDo you want to append \'exit\' to the file?(y/n)\n-----------------------------------------------\n-> ')
            
                if x == 'y':
                    continue
            fo.write('\n' + line)