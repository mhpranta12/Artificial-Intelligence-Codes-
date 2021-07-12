import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)


class Agent(Object):
    
    def __init__(self):        
        def program(percept):abstract
        self.program=program


loc_A,loc_B='A','B'

class vaccumEnvironemt(Object):

    def __init__(self):
        
        self.status={
            loc_A:random.choice(['Clean','Dirty']),
            loc_B:random.choice(['Clean','Dirty'])
            }      
        
    def add_object(self,agent,location=None):
        agent.location=location or self.default_location()

    
    def default_location(self):
        return random.choice([loc_A,loc_B])


    def percept(self,agent):
        return (agent.location,self.status[agent.location])


    def execute_action(self,agent,action):

        if action == 'Right': agent.location=loc_B
        elif action == 'Left': agent.location=loc_A
        elif action== 'Suck':
            self.status[agent.location]='Clean'



table={
        (('A', 'Clean'),): 'Right',
        (('A', 'Dirty'),): 'Suck',
        (('B', 'Clean'),): 'Left',
        (('B', 'Dirty'),): 'Suck',
       

        (('A', 'Clean'), ('A', 'Clean')): 'Right',
        (('A', 'Clean'), ('A', 'Dirty')): 'Suck',
        (('A', 'Clean'), ('B', 'Clean')): 'Suck',
        (('A', 'Clean'), ('B', 'Dirty')): 'Suck',

        
        (('A', 'Dirty'), ('A', 'Clean')): 'Right',
        (('A', 'Dirty'), ('A', 'Dirty')): 'Suck',
        (('A', 'Dirty'), ('B', 'Clean')): 'Suck',
        (('A', 'Dirty'), ('B', 'Dirty')): 'Suck',


        (('B', 'Clean'), ('A', 'Clean')): 'Right',
        (('B', 'Clean'), ('A', 'Dirty')): 'Suck',
        (('B', 'Clean'), ('B', 'Clean')): 'Suck',
        (('B', 'Clean'), ('B', 'Dirty')): 'Suck',

        
        (('B', 'Dirty'), ('A', 'Clean')): 'Right',
        (('B', 'Dirty'), ('A', 'Dirty')): 'Suck',
        (('B', 'Dirty'), ('B', 'Clean')): 'Suck',
        (('B', 'Dirty'), ('B', 'Dirty')): 'Suck',


        (('A', 'Clean'), ('A', 'Clean'),('A', 'Clean')): 'Right',
        

        
    }

class tableDrivenAgent(Agent):

    def __init__(self,table):
        
        Agent.__init__(self)

        self.percepts=[]

        def program(percept):
            self.percepts.append(percept)
            action=table.get(tuple(self.percepts))
            print("Agent Has Perceived: ", tuple(self.percepts), " And Performed Action: ", action)
            return action


        self.program=program


class simpleReflexVacuumAgent(Agent):

    def __init__(self,table):
        
        Agent.__init__(self)

        def program(percept):
##            location=percept[0]
##            status=percept[1]
##            action=table.get(tuple(self.percepts))
##            if(status=='Dirty'): return action=='Suck'
##            elif (location=='A'): return 'Right'
##            elif (location=='B'): return 'Left'    


           
            action=table.get(tuple(self.percepts))
            if(status=='Dirty'): print("Agent Has Perceived: ", tuple(self.percept), " And Performed Action: ", 'Suck')
            elif(status=='Clean'): print("Agent Has Perceived: ", tuple(self.percept), " And Performed Action: ", 'Right')
            return action


            self.program=program
            print("Agent Has Perceived: ", percept, " And Performed Action: ", action)
            return action


        self.program=program



class modelBasedVacuumAgent(Agent):

    def __init__(self,table):
        
        Agent.__init__(self)

        def program(percept):
            print ("A")

##             (('B', 'Dirty'), ('A', 'Clean')): 'Right'
##             print("Agent Has Perceived: ", percept, " And Performed Action: ", action)
##             return action

sRAgent=simpleReflexVacuumAgent(table)
env=vaccumEnvironemt()
env.add_object(sRAgent)


agentsPercept=env.percept(sRAgent)
action=sRAgent.program(agentsPercept)
print (env.execute_action(sRAgent,action))



##        
##
#### WRITE YOUR OWN CODE HERE
##
