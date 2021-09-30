import NumbersLetters
import PostFija
import Logicas
numeros= NumbersLetters.NumberLetter()
calculator=PostFija.PostFija()
logica=Logicas.Logicas()
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
        resultado=calculator.SolveStack(calculator.Solve('(9+22.12)*1/4^2-2')) 
        print('El resultado es', resultado)
        pass
    elif opc==2:
        string="~([(p->q)^p]->q)"
        #string="[(p->q)^(q->r)]<->(p->r)"
        print(string)
        logica.Solve(string)

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

