class Logicas: 

    def __init__(self):
        self.operations=['~','-','*','^','+']
        self.letter={}
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
        result=[]
        file=[]
        parenthesis=['(','[']
        closeparenthesis=[')',']']

        #Algotimo
        for x in line:
            if x in parenthesis:
                file.append(x)
            elif x.isalpha():
                result.append(x)
            elif x in self.operations:
                if len(file)==0:
                    file.append(x)
                elif file[len(file)-1] in parenthesis:
                    file.append(x)
                else:
                    #Vacia la fila
                    result.append(file.pop())
                    file.append(x)
            elif x in closeparenthesis:
                #Vaciar hasta que encontremos su pareja
                
                result.append(file.pop())
                if len(file)>0:
                    file.pop()
        result=result+file
        print(result)

                    
                
        

        

string="[(p<->q)^p]->q"
Logicas().Solve(string)


#p q -> q ~ r v r q -> <->
'''
Algoritmo
si el elemento es ( [ se añade a una fila
si el elemento es un letra se añade al resultado
si el elemento es un operador se verifa en el fila no esten elementos si ya hay
elementos se vacia y se añade el nuevo elemento solo si el ultimo en la fila no es un parenthesis 
si es un parentesis solo se añade a la fila
si el elemento es ) ] se tiene q vaciar todos los elementos que esten entre () o []

'''
