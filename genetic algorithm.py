import random
population = ['01101','11000','01000','10011']

def  xVal(population):
    positional_Val=[1,2,4,8,16]
    convintar=[]
    
    it=0;
    
    j=0
    i=int(j)
    
    itr=int(it)
    for i in population:
        seg= f"{i}\n"
        result=inttostringconv(seg)
        print(f"{result}\n")
        
        
def inttostringconv (seg):
    mult=int(16)
    s=int(0)
    for j in seg:
        for k in j:
                n=1;
                val=int(k)
                result=val*mult
                mult=mult-(mult/2)
                n=n+1
                s=s+result;
    return s
def intconv (population):
    for i in population:
        for j in i:
            print(int(j))
val1=['01101']
val2=['11000']
val3=['01000']
val4=['10011']

res1= inttostringconv(val1)
res2=inttostringconv(val2)
res3=inttostringconv(val3)
res4=inttostringconv(val4)
res1=int(res1)
print(f"1st string to Integer (Phenotypes):{res1} \n")
print(f"2nd string to Integer  (Phenotypes):{res2} \n")
print(f"3rd string to Integer  (Phenotypes):{res3} \n")
print(f"4th string to Integer  (Phenotypes):{res4} \n")
pheno1 =res1
pheno2 =res2
pheno3 =res3
pheno4 =res4
fitness1 = int(pheno1**2)
fitness2 = (pheno2**2)
fitness3 = (pheno3**2)
fitness4 = (pheno4**2)

print(f"fitness1  value : {fitness1}\n")
print(f"fitness2 value : {fitness2}\n")
print(f"fitness3 value :{fitness3}\n")
print(f"fitness4 value :{fitness4}\n")
total_sum=(fitness1+fitness2+fitness3+fitness4)
print(f"Total Sum :{total_sum}\n")
probability1=round((fitness1/total_sum),2)
probability2=round((fitness2/total_sum),2)
probability3=round((fitness3/total_sum),2)
probability4=round((fitness4/total_sum),2)
print(f"Probability of fitness1 value :{probability1}\n")
print(f"Probability of  fitness2 value :{probability2}\n")
print(f"Probability of  fitness3 value :{probability3}\n")
print(f"Probability of  fitness4 value :{probability4}\n")
var1=round(random.uniform(probability1,probability4),2)
range1=probability1
print(f"Randomly selected value 1 : {var1}")
range4 = probability1+probability2+probability3+probability4

var2=round(random.uniform(range1,range4),2)
range2=probability1+probability2
print(f"Randomly selected value 2 : {var2}")
var3=round(random.uniform(range1,range4),2)
range3=probability1+probability2+probability3
print(f"Randomly selected value 3 : {var3}")
var4=round(random.uniform(range1,range4),2)
print(f"Randomly selected value 4 : {var4}")
print(f"\n")
print(f"Heighest range1 = 0 to {range1}\nHeighest range2 = {probability1} to {range2}\nHeighest range3 = {probability1+probability2} to {range3}\n"
      f"Heighest range4 = {probability1+probability2+probability3} to {range4}\n")
floatpointarray=[]
floatpointarray.append(var1)
floatpointarray.append(var2)
floatpointarray.append(var3)
floatpointarray.append(var4)

for a in floatpointarray:
    if a>=0 and a<=probability1:
        print(f"{a} belongs to : {val1}")
    elif a>=probability1 and a<=(probability1+probability2):
        print(f"{a} belongs to : {val2}")
    elif a>=(probability1+probability2) and a<=(probability1+probability2+probability3):
        print(f"{a} belongs to : {val3}")
    elif a>=(probability1+probability2+probability3) and a<=(probability1+probability2+probability3+probability4):
        print(f"{a} belongs to : {val4}")
        
        

