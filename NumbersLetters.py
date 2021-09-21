class NumberLetter:
    #1 2 b 3 c 4 d 5 e
    def GetLine(self, line):
        return line.split(' ')
    def IsNumber(self,simbol):
        try:
            int(simbol)
            return True
        except:
            return False
            pass

    def CountNumbersAndLetters(self,array):
        numbers=[]
        letter=[]
        string=[]
        for simbol in array:
            if self.IsNumber(simbol)==True:
                numbers.append(simbol)
            else:
                if len(simbol)==1:
                    letter.append(simbol)
                else:
                    string.append(simbol)

        print('Los elementos que son numeros son: ',numbers)
        print("El numero de elementos es ",len(numbers))
        print("Los elementos chart son ",letter)
        print("El numero de elementos es ",len(letter))
        print("Los elementos string son ",string)
        print("El numero de elementos es ",len(string))
