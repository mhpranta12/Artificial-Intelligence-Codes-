
x1={'a':6,'b':5,'c':4,'d':1,'e':3,'f':5,'g':3,'h':2}
x2={'a':8,'b':7,'c':1,'d':2,'e':6,'f':6,'g':0,'h':1}
x3={'a':2,'b':3,'c':9,'d':2,'e':1,'f':2,'g':8,'h':5}
x4={'a':4,'b':1,'c':8,'d':5,'e':2,'f':0,'g':9,'h':4}
def iterate(x1,x2):
    for i,v in enumerate (zip(x1,x2)):
  
                                    print(x1[i])
                                    print(x2[v])

def fitness(ar):
    #for i,v in enumerate(ar):
        #sum=0
        
       # print(i)
        #print(v)
        
        #print(f"sum = {sum}")
    sum=0
    fitness=0
    sum2=0
    temp1=(ar['a']+ar['b'])
    temp2=(ar['c']+ar['d'])
    temp3=(ar['e']+ar['f'])
    temp4=(ar['g']+ar['h'])
    
    sum=(temp1-temp2)
    print(sum)
    sum2=(temp3-temp4)
    print(sum2)
    fitness=sum+sum2
    print(f"Fitness Value for (ar) = {fitness}")        
    return fitness
def sort(x1,x2,x3,x4):
    sort_array={'max1':0,'max2':0,'max3':0,'max4':0}
    max=0
    if x1>x2 and x1>x3 and x1>x4:
        sort_array['max1']=x1
    elif x2>x1 and x2>x3 and x2>x4:
        sort_array['max1']=x2
    elif x3>x1 and x3>x2 and x3>x4:
        sort_array['max1']=x3
    elif x4>x1 and x4>x3 and x4>x3:
        sort_array['max1']=x4
    return sort_array
def getsorted(x1,x2,x3,x4):
    numbers=[]
    numbers.append(x1)
    numbers.append(x2)
    numbers.append(x3)
    numbers.append(x4)

    numbers.sort() #Sorting the array into as usual and by default Ascending Order
    numbers.sort(reverse=True) #Reversing the array to get into Inverse(Descending) Order

    return numbers
        
t1=fitness(x1)
t2=fitness(x2)
t3=fitness(x3)
t4=fitness(x4)
total_fitness_original=t1+t2+t3+t4
print(f"Total Fitness  of original function  = {total_fitness_original}")
maximum=getsorted(t1,t2,t3,t4)
print(f"Total Sorted Order  of original function  = {maximum}")


    
