
import random

class Object:
        def __repr__(self):
                return '<%s>' % getattr(self,'__name__',self.__class__.__name__)

class Agent(Object):

        def __init__(self):
                def program(percept): abstract
                self.program=program


loc_A,loc_B='A','B'

class vacuumEnvironment(Object):

        def __init__(self):
                self.status={

                        loc_A:random.choice(['Dirty','Clean']),
                        loc_B:random.choice(['Dirty','Clean']),
                        }

        def default_location(self):
                return random.choice([loc_A,loc_B])

        def add_object(self,agent,location=None):
                agent.location=location or self.default_location()

        def percept(self,agent):
                return (agent.location,self.status[agent.location])

        def execute_action(self,agent,action):
                
                if action=='Right': agent.location=loc_B
                elif action=='Left': agent.location=loc_A
                elif action=='Suck':
                        self.status[agent.location]='Clean'


class tableDrivenAgent(Agent):

        def __init__(self,table):
                Agent.__init__(self)

                percepts=[]

                def program(percept):
                        percepts.append(percept)
                        action=table.get(tuple(percepts))
                        
                        print("Agent Has Perceived: ",percepts," and Returned Action: ",action)

                        return action

                self.program=program
                        


##def createTableDrivenAgent():
##        return tableDrivenAgent(table)

table={
        (('A', 'Dirty'),):'Suck',
        (('A', 'Clean'),):'Right',
        (('B', 'Dirty'),):'Suck',
        (('B', 'Clean'),):'Left',

        (('A', 'Dirty'), ('A', 'Clean')):'Right',
        (('A', 'Dirty'), ('A', 'Dirty')):'Suck',
        (('A', 'Clean'), ('B', 'Clean')):'Left',
        (('A', 'Clean'), ('B', 'Dirty')):'Suck',


        (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty')):'Suck'

        }

        


tAgent=tableDrivenAgent(table)
env=vacuumEnvironment()
env.add_object(tAgent)



for i in range(10):
        agentsPercept=env.percept(tAgent)
        action=tAgent.program(agentsPercept)
        env.execute_action(tAgent,action)
