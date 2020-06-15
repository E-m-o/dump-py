class SpecialString:
    def __init__(self,string):
        self.string = string

    def print_string(self):
        i = 0
        while i-4 < len(self.string):
            print('*',end = '')
            i += 1
        print('\n*', self.string, '*')
        i = 0
        while i-4 < len(self.string):
            print('*',end = '')
            i += 1
        print('\n')
    

def class_practice(value1,value2):
    X = SpecialString(value1)
    X.print_string()
    X.string = value2
    X.print_string()
    