class PostFija:
    def __init__(self):
        self.operadores={ 
                '^':3
                ,'*':2
                ,'/':2,
                '+':1,
                '-':1
                }
    def IsNumber(self,x):
        try:
            float(x)
            return True
        except:
            return False

    def MakeFormat(self,line):
        operadores=['+','-','*','/','^','(',')']
        lineformat=[]
        cadenaaux=""
        for x in line:
            if x in operadores:
                if cadenaaux!="":
                    lineformat.append(cadenaaux)
                    cadenaaux=""
                lineformat.append(x)

            else:
                cadenaaux+=x
        if len(cadenaaux)>0:
            lineformat.append(cadenaaux)
        print(lineformat)
        return lineformat

    def Solve(self,line):
        pila=[]
        result=[]
        for x in self.MakeFormat(line):
            if self.IsNumber(x)==False:
                if len(pila)==0:
                    pila.append(x)
                else:
                    self.SortOut(pila,x,result)
            else:
                result.append(x)
        while len(pila)>0:
            result.append(pila.pop())        
        return result
    def SortOut(self,pila,x,result):
        if x=='(':
            pila.append(x)
        else:
            if x==')':
                #Tenemos q desapilar
                self.Desapilar(pila,result)
            else:
                if pila[len(pila)-1]=='(':
                    pila.append(x)
                else:
                    if self.operadores[x]>self.operadores[pila[len(pila)-1]]:
                        pila.append(x)
                    else:
                        while len(pila)>0:
                            result.append(pila.pop())
                        pila.append(x)
                        
    def Desapilar(self,pila,result):
        x=pila[len(pila)-1]
        while pila[len(pila)-1]!='(':
            x=pila.pop()
            result.append(x)
        pila.pop()

    def SolveStack(self,result):
        i=0
        while len(result)>1:
            if self.IsNumber(result[i])==False:
                result=self.DoOperation(result,i)
                i=0
            else:
                i+=1
        return result

    def DoOperation(self,result,i):
        num1=float(result[i-2])
        num2=float(result[i-1])
        operation=0
        if result[i]=="+":
            operation=num1+num2
            pass
        if result[i]=="-":
            operation=num1-num2
            pass
        if result[i]=="*":
            operation=num1*num2
            pass
        if result[i]=='/':
            operation=num1/num2
            pass

        if result[i]=='^':
            operation=num1**num2
            pass
        #Rebuilt the result
        resultado=[]
        positions=[i-2, i-1, i]
        for x in range (len(result)):
            if x ==i-2:
                resultado.append(operation)
            if x not in positions:
                resultado.append(result[x])
        return resultado





