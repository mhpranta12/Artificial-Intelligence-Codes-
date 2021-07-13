import copy    #importing the copy package to use
x1={'a':6,'b':5,'c':4,'d':1,'e':3,'f':5,'g':3,'h':2}        #declaring the sets and assinging value to each keys
x2={'a':8,'b':7,'c':1,'d':2,'e':6,'f':6,'g':0,'h':1}
x3={'a':2,'b':3,'c':9,'d':2,'e':1,'f':2,'g':8,'h':5}
x4={'a':4,'b':1,'c':8,'d':5,'e':2,'f':0,'g':9,'h':4}
def iterate(x1):
    for i,v in enumerate(x1):
        print(x1[v],end=" ") #we can use this  additional end parameter and can provide its value to define how the printed elemen will end and the next one will start 
           
                                    

def fitness(ar):
    
    sum=0
    fitness=0
    sum2=0
    temp1=(ar['a']+ar['b'])  #Here is the formula of determining fitness 
    temp2=(ar['c']+ar['d'])
    temp3=(ar['e']+ar['f'])
    temp4=(ar['g']+ar['h'])
    
    sum=(temp1-temp2)
    
    sum2=(temp3-temp4)
  
    fitness=sum+sum2
    print(f"\n Fitness Value for array = {fitness}")        
    return fitness
def getmax(x1,x2,x3,x4):
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
    numbers.append(x1)      #Inserting(Appending) each of the inputted parameters in an array in order to do operations
    numbers.append(x2)
    numbers.append(x3)
    numbers.append(x4)

    numbers.sort() #Sorting the array into as usual and by default Ascending Order
    numbers.sort(reverse=True) #Reversing the array to get into Inverse(Descending) Order

    return numbers
def onepointcrossover(ar1,ar2):
    new_ar1=copy.copy(ar1)      #copying the values of inputted array 1 and 2 . Thats why they don't alter/change the original Set that we declared.
    new_ar2=copy.copy(ar2)

    # We will ecxhange only last 4 elements
    ar1copy={'e':ar1['e'],'f':ar1['f'],'g':ar1['g'],'h':ar1['h']} #Firstly storing(Coping) the values of Array1(that we want to exchange with Array2) that we can get back them to xchng
    
    new_ar1['e']=new_ar2['e'] #Simply exchanging all of the values between 2 sets by pointer
    new_ar1['f']=new_ar2['f']
    new_ar1['g']=new_ar2['g']
    new_ar1['h']=new_ar2['h']
    
    new_ar2['e']=ar1copy['e']
    new_ar2['f']=ar1copy['f']
    new_ar2['g']=ar1copy['g']
    new_ar2['h']=ar1copy['h']
    
    print(f"\nAfter One point CrossOver Occurence :\n The values are :\n")
    iterate(new_ar1)        #Invoking the iterate function to print all the elements

    print(f"\nand\n")
    
    iterate(new_ar2)        #Invoking the iterate function to print all the elements
    
    fitness_new_ar1=fitness(new_ar1)
    fitness_new_ar2=fitness(new_ar2)
    
    
    return fitness_new_ar1+fitness_new_ar2

def twopointcrossover(ar1,ar2):
    new_ar1=copy.copy(ar1)
    new_ar2=copy.copy(ar2)
    new_ar1['f']=5
    # We have to keep b and f fixed thats why they will remain unchanged of both arrays
    ar1copy={'a':ar1['a'],'c':ar1['c'],'d':ar1['d'],'e':ar1['e'],'g':ar1['g'],'h':ar1['h']} #Storing the original values of Array 1 in order to exchange
    print(f"\n \n \n e={(ar1['e'])}\n")

    
    #Array 1 part exchange part 
    new_ar1['a']=new_ar2['a']       #Simply exchanging all of the values between 2 sets by pointer
    new_ar1['c']=new_ar2['c']
    new_ar1['d']=new_ar2['d']
    new_ar1['e']=new_ar2['e']
    new_ar1['g']=new_ar2['g']
    new_ar1['h']=new_ar2['h']

    
    #Array 2 part exchange part 
    new_ar2['a']=ar1copy['a']       #Simply exchanging all of the values between 2 sets by pointer
    new_ar2['c']=ar1copy['c']
    new_ar2['d']=ar1copy['d']
    new_ar2['e']=ar1copy['e']
    new_ar2['g']=ar1copy['g']
    new_ar2['h']=ar1copy['h']
    print(f"\n \nAfter Two point CrossOver Occurence :\n The values are :\n")
    iterate(new_ar1)        #Invoking the iterate function to print all the elements

    print(f"\nand\n")
    
    iterate(new_ar2)        #Invoking the iterate function to print all the elements
    
    fitness_new_ar1=fitness(new_ar1)
    fitness_new_ar2=fitness(new_ar2)
    
    
    return fitness_new_ar1+fitness_new_ar2

def uniformcrossover(ar1,ar2):
    new_ar1=copy.copy(ar1)
    new_ar2=copy.copy(ar2)
    new_ar1['f']=5
    # We have to change only a ,d and f  .Rests will remain unchanged of both arrays
    ar1copy={'a':ar1['a'],'d':ar1['d'],'f':ar1['f']} #Storing the original values of Array 1 in order to exchange
    print(f"\n \n \n e={(ar1['e'])}\n")
    
    #Array 1 part exchange part 
    new_ar1['a']=new_ar2['a']    #Simply exchanging all of the values between 2 sets by pointer
    new_ar1['d']=new_ar2['d']
    new_ar1['f']=new_ar2['f']
    
    #Array 2 part exchange part 
    new_ar2['a']=ar1copy['a']   #Simply exchanging all of the values between 2 sets by pointer
    new_ar2['d']=ar1copy['d']
    new_ar2['f']=ar1copy['f']
    
    
    print(f"\n \nAfter  Uniform CrossOver Occurence :\n The values are :\n")
    iterate(new_ar1)        #Invoking the iterate function to print all the elements

    print(f"\nand\n")
    
    iterate(new_ar2)        #Invoking the iterate function to print all the elements
    
    fitness_new_ar1=fitness(new_ar1)
    fitness_new_ar2=fitness(new_ar2)
    
    
    return fitness_new_ar1+fitness_new_ar2
print(f"a b c d e f g h \n")
print(f"=X1   {iterate(x1)} \n")
print (f"=X2   {iterate(x2)} \n")
print(f"=X3    {iterate(x3)} \n")
print(f"=X4    {iterate(x4)} \n")

t1=fitness(x1)                  #Invoking the fitness function to calculate fitness
t2=fitness(x2)
t3=fitness(x3)
t4=fitness(x4)
total_fitness_original=t1+t2+t3+t4          #Sum up total fitness of original

print(f"Total Fitness  of original function  = {total_fitness_original}")
sortedlist=getsorted(t1,t2,t3,t4)           #Invoking the getsorted function and storing the returned value in sortedlist variable
print(f"Total Sorted Order  of original function  = {sortedlist}")


total_child_fitness1=onepointcrossover(x2,x1)  #Function calling and storing the returned value (summation of fitness among which crossover was occured) 
total_child_fitness2=twopointcrossover(x1,x3)
total_child_fitness3=uniformcrossover(x2,x3)

print("\n")
total_child_fitness=total_child_fitness1+total_child_fitness2+total_child_fitness3              #Sum up of all new generated child's fitness
print(f"Total fitness of all childs = {total_child_fitness}")
if total_child_fitness > total_fitness_original:            # Comparing the fitness of newly generated child and original's 
    print(f"{total_child_fitness}(Child's Fitness) > {total_fitness_original}(Original Fitness) Fitness was Increased!")
else :
    print(f"{total_fitness_original}(Original Fitness) > {total_child_fitness}(Child's Fitness)) Fitness was Decreased")

    
