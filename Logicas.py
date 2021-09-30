class Logicas: 

    def __init__(self):
        self.operations=['~','-','*','^','+']
        self.letter={}
        self.Parentesis=['(','[']
        self.ParentesisCierre=[']',')']
    #self.symbols=['~','^','v','->']
    def GetNumbersOfColums(self,line):
        elements={}
        for x in line:
            if x.isalpha():
                try:
                    elements[x]
                except:
                    elements[x]=x
                    
        self.SortOutLetter(elements)
        return len(elements)
    def SortOutLetter(self,elements):
        aux=""
        for e in elements:
            aux+=e
        i=0
        for x in sorted(aux):
            self.letter[x]=i
            i+=1

    def GenerateTable(self,colums):
        rows=2**colums
        #GenerateCount
        c=0
        auxrow=rows
        count=[]
        table=[]
        state=[]
        copiecount=[]
        while c<colums:
            state.append(True)
            auxrow=auxrow/2
            if auxrow>0:
                count.append(int (auxrow))
                copiecount.append(int(auxrow))
            else:
                count.append(1)
                copiecount.append(1)
            c+=1
        
        for r in range(0,rows):
            rowaux=[]
            for c in range(colums):

                rowaux.append(state[c])
                count[c]-=1
                if count[c]==0:
                    count[c]=copiecount[c]
                    state[c]=not state[c]

            table.append(rowaux)
        
        return table
        
    def Solve(self,line):
        line=line.replace('v','+')
        colums=self.GetNumbersOfColums(line)
        table=self.GenerateTable(colums)
        #We can get throght by the line
        line=line.replace('<->','*').replace('->','-')
        #Pasar a postfija
        linea=self.ConvertirPostfija(line)
        print(linea)
        #line=line.replace(' ','').replace('(','').replace(')','').replace('[','').replace(']','')
        self.Evaluate(table,linea)

    def ConvertirPostfija(self,linea):
        resultado=[]
        stack=[]
        for x in linea:
            if x in self.Parentesis:
                stack.append(x)
            else:
                if x.isalpha():
                    resultado.append(x)
                elif x in self.operations:
                    if len(stack)>0:
                        if stack[len(stack)-1] in self.Parentesis:
                            stack.append(x)
                        elif x=='~':
                            resultado.append(x)
                        else:
                            resultado.append(stack.pop())
                            stack.append(x)
                    else:
                        stack.append(x)

                elif x in self.ParentesisCierre:
                    apertura="("
                    if x==']':
                        apertura="["
                    while stack[-1]!=apertura:
                        ope=stack.pop()
                        if ope in self.operations:
                            resultado.append(ope)
                    if stack[-1]==apertura:
                        stack.pop()


        for z in stack:
            if z in self.operations:
                resultado.append(z)
        return resultado



    def Evaluate(self,table,line):
        operacion=""
        resultado=[]
        for t in table:
            for x in line:
                if x not in self.operations:
                     operacion+=str(t[self.letter[x]])[0]
                else:
                    operacion+=x
            r=self.MakeOperation(operacion)
            resultado.append(r)
            operacion=""
        print(resultado)
        if 'T' in resultado and 'F' in resultado:
            print('Contingencia')
        elif 'T' in resultado and 'F' not in resultado:
            print('Tautologia')
        else:
            print('Contradiccion')
    def MakeOperation(self,operacion):
        cadena=list(operacion)

        while len(cadena)>1:
            i=0
            for x in cadena:
                if x in self.operations:
                    auxresult=self.DoOperation(cadena,i)
                    cadena[i]=auxresult
                    cadena[i-1]=None
                    if len(cadena)>2:
                        cadena[i-2]=None
                    cadena=self.CleanStack(cadena)
                    break
                i+=1

        return cadena[0]
    def DoOperation(self,cadena,x):
        if cadena[x]=='-':
            if cadena[x-2]=='T' and cadena[x-1]=='F':
                return 'F'
            else:
                return 'T'
        if cadena[x]=='*':
            if cadena[x-2]==cadena[x-1]:
                return 'T'
            else:
                return 'F'

        if cadena[x]=='^':
            if cadena[x-2]=='T' and cadena[x-1]=='T':
                return 'T'
            else:
                return 'F'
        if cadena[x]=='+':
            if cadena[x-2]=='F' and cadena[x-1]=='F':
                return 'F'
            else:
                return 'T'
        if cadena[x]=='~':
            if cadena[x-1]=='T':
                return 'F'
            else:
                return 'T'

    def CleanStack(self,cadena):
        auxcadena=[]
        for x in cadena:
            if x!=None:
                auxcadena.append(x)
        return auxcadena


                    
    def Negada(self,valor):
        if valor=='T':
            return 'F'
        else:
            return 'T'


    

'''
[(p->q)^(q->r)]<->(p->r)

p q -> q r -> ^ p r -> <->

Si el elemento es un parentesis de apertura se apila sin importar cual sera el top
si el elemento es una letra se añade al resultado
si el elemento es un operado se verifica que
    el top de la pila es un parentensis de apertura -> se apila el elemento
    el top de pila es otro operador y es diferente a ~ -> se saca el top y se añade
    el nuevo operador
    el top elemento es ~ ->añade directamente al resultado siempre y cuando el top no sea ( [
si el elemento es un parentensis de cierre entonces vacia todo lo q este en medio de los 
parentensis y añadelo al resultado
    
    Ejemplo 

Paso 1
[ ( -> )
p q 

Paso 2
[ ^ ( -> )
p q -> q r

Paso 3
[ ^ ]
p q -> q r ->

Paso 4
<-> ( -> )
p q -> q r -> ^ p r

Paso 5
p q -> q r -> ^ q r -> <->

Ejemplo 2
[(p->q)^p]->q
Paso 1
[ ( -> )
p q

Paso 2
[  ^  ]
p q -> p

Paso 3
->
p q -> p ^ q

Paso 4

p q -> p ^ q ->
'''
