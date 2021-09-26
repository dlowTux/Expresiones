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
        line=line.replace(' ','').replace('(','').replace(')','').replace('[','').replace(']','')
        self.Evaluate(table,line)
    def Evaluate(self,table,line):
        operacion=""
        for t in table:
            for x in line:
                if x not in self.operations:
                     operacion+=str(t[self.letter[x]])[0]
                else:
                    operacion+=x
            self.MakeOperation(operacion)
            operacion=""
    
    def MakeOperation(self,operacion):
        cadena=list(operacion)
        #Realizando primero las negadas
        while '~' in cadena:
            for x in range(len(cadena)):
                if cadena[x]=='~':
                    resultdo=self.Negada(cadena[x+1])
                    cadena[x]=resultdo
                    cadena[x+1]=None
        cadena=self.CleanStack(cadena)
        
        while len(cadena)>1:
            i=0
            for x in cadena:
                if x in self.operations:
                    auxresult=self.DoOperation(cadena,i)
                    cadena[i]=auxresult
                    cadena[i-1]=None
                    cadena[i+1]=None
                    cadena=self.CleanStack(cadena)
                    break
                i+=1
            pass
        print(cadena)
    def DoOperation(self,cadena,x):
        if cadena[x]=='-':
            if cadena[x-1]=='T' and cadena[x+1]=='F':
                return 'F'
            else:
                return 'T'
        if cadena[x]=='*':
            if cadena[x-1]==cadena[x+1]:
                return 'T'
            else:
                return 'F'

        if cadena[x]=='^':
            if cadena[x-1]=='T' and cadena[x+1]=='T':
                return 'T'
            else:
                return 'F'
        if cadena[x]=='+':
            if cadena[x-1]=='F' and cadena[x+1]=='F':
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


    


