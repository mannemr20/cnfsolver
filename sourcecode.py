import time
import os

directory='/home/rishi/Desktop/Myprojectspy/Assignment_2_200562_200003/testcases'
instrcution1="If 'y' then the code will give an output for each file in testcases folder"
instruction2="If 'n' the the code will take input from input.txt"
flag=input("Do you want to take input from testcase's folder?:"+"\n"+instrcution1+"\n"+instruction2+"\n"+"TYPE (y/n):  ")

def most_freq_in_min(formula):
    c=[]
    min=formula[0]
    for x in formula:
        if(len(x)<len(min)):
            min=x
        for y in x:
            c.append(y)
    counter = 0
    num = min[0]
     
    for i in min:
        presfreq = c.count(i)
        if(presfreq>counter):
            counter = presfreq
            num = i
 
    return num
    


def check(formula,model):
    for x in formula:
        flag=0
        for y in x:
            if(y in model):
                flag=1
                break
        if(flag==0):
            return False
    return True

def simplify(formula,val):
    formula=[x for x in formula if val not in x]
    formula=[list(set(x).difference({-val})) for x in formula ]
    return formula

def add(formula,val):
    if([val] not in formula):
        formula.append([val])
    return formula
    
def remove(formula,val):
    if([val] in formula):
        formula.remove([val])
    return formula

def unit_resolution(formula):
    solution=set()
    unit_clauses=[x for x in formula if len(x)==1]
    while(len(unit_clauses)!=0):
        for x in unit_clauses:
            if(-x[0] not in solution):
                solution.add(x[0])
            formula=simplify(formula,x[0])
        unit_clauses=[x for x in formula if len(x)==1]
    return solution,formula

def DPLL(F):
    S1,Fn=unit_resolution(F)
    if(len(Fn)==0):
        return S1
    if([] in Fn):
        return False
    L=most_freq_in_min(Fn)
    S2=DPLL(add(Fn,L))
    if(S2!=False):
        return S1.union(S2)
    Fn=remove(Fn,L)
    S3=DPLL(add(Fn,-L))
    if(S3!=False):
        return S1.union(S3)
    return False

def main():
    with open("output.txt","w") as f:
        f.write("")
    count=1
    global literals
    fileslist=[]
    for files in os.listdir(directory):
        fileslist.append(files)
    fileslist.sort()
    for filename in fileslist:
        if(flag=='n' or flag=='N'):
            f=open("input.txt")
        elif(flag=='y' or flag=='Y'):
            print(filename)
            f=open(directory+"/"+filename)
        formula=[]
        for line in f:
            if(line[0]=='c'):
                continue
            elif(line[0]=='p'):
                res=line.split()
                literals=int(res[2])
                continue
            else:
                res=line.split()
                clause=[]
                for i in res:
                    if(int(i)!=0):
                        clause.append(int(i))
                formula.append(clause)
        start=time.time()
        model=DPLL(formula)
        end=time.time()
        if(model!=False):
            model=list(model)
            for i in range(1,1+literals):
                if(i in model and -i in model):
                    model.remove(i)
                    if(check(formula,model)==False):
                        model.append(i)
                        model.remove(-i)
                if(not(i in model or -i in model)):
                    model.append(i)
            model.sort(key= lambda x: abs(x))
        with open("output.txt","a") as outfile:
            if(flag=='n' or flag=='N'):
                out="The time of execution for file input.txt is : %.3fs"%(end-start)
            else:
                out="The time of execution for file %i is : %.3fs"%(count,end-start)
            if(flag=='y' or  flag=='Y'):
                outfile.write("File-"+str(count)+" "+filename+'\n')
            outfile.write(out+'\n')
            count+=1
            if(model==False):
                outfile.write('UNSAT'+3*'\n')
            else:
                outfile.write('SAT'+'\n')
                outfile.write("check="+str(check(formula,model))+'\n')
                outfile.write(str(model)+3*'\n')
        f.close()
        if(flag=='n' or flag=='N'):
            break
main()
print("Output in stored in output.txt")