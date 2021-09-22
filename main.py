import NumbersLetters
import PostFija
numeros= NumbersLetters.NumberLetter()
calculator=PostFija.PostFija()
def menu():
    print('1.-Expresiones aritmeticas')
    print("2.-Exprecion logica")
    print("3.-Expresion logica v2")
    print("4.-Salir")
    print("....")

def SelectOption():
    menu()
    opc=int(input())
    if opc==1:
        print('Ingrese la operacion')
        resultado=calculator.SolveStack(calculator.Solve(input())) 
        print('El resultado es', resultado)
        pass
    elif opc==2:
        pass
    elif opc==3:
        print('Ingresa la cadena')
        string=numeros.GetLine(input())
        numeros.CountNumbersAndLetters(string)
        pass
    elif opc==4:
        print('Bye')
        return False
    else:
        print('No se reconocio el dato')
    return None

while(SelectOption()!=False):
    pass

