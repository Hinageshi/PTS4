from RequestHandler import *
from DisplayHandler import *
from Agent import *
from tkinter import *
import matplotlib.pyplot as plt

rh = RequestHandler()
dh = DisplayHandler()
"""
preciseAgent = rh.APIRequest(agentNumber = 260798)
print(preciseAgent)
randomAgent = rh.APIRequest(numberOfAgents = 1)
print(randomAgent)
randomAgentFr = rh.APIRequest(numberOfAgents = 1, country = "France")
print(randomAgentFr)
"""
randomAgents = rh.APIRequest(numberOfAgents = 10)
"""
randomAgentsFr = rh.APIRequest(numberOfAgents = 5, country = "France")
print(randomAgentsFr)
"""
testCriteria = {'age': [50, 'sup'], 'income': [1000, 'sup'], 'sex': ['Female', 'eq']}
#agent = Agent(preciseAgent)
#print(agent.getInfo())
#dh.display(jsonData=preciseAgent, mainCriterion='neuroticism')
dh.display(jsonData=randomAgents, mainCriterion='age', criteria=testCriteria)
"""
a = rh.getRandomAgent()
print(a.getInfo())
a2 = rh.getOneAgent(6352373083)
print(a2.getInfo())
a3 = rh.getRandomAgentFromCountry('fr')
print(a3.getInfo())
for agent in rh.getSampleRandomAgents(5):
    print(agent.getInfo())
for agent in rh.getSampleRandomAgentsFromCountry(5, 'fr'):
    print(agent.getInfo())

income = []
avgs = []
avg = 0
i = 1
for agent in rh.getSampleRandomAgents(100):
    print("#" + str(i) + " : $" + str(agent.properties['income']) + " USD")
    income.append(agent.properties['income'])
    i+= 1
    avg += agent.properties['income']
avg /= len(income)
for i in range (0, len(income)):
    avgs.append(avg)
plt.title("Income of Agents")
plt.plot(income)
plt.plot(avgs, "r--", label="Average : $" + str(avg) + " USD")
plt.ylabel('Income ($USD)')
plt.legend()
plt.show()

fen = Tk()
cadre = Frame(fen, width=500, height=750, borderwidth=1)
cadre.pack(fill=BOTH)
label = Label(fen, text="Agent")
label.pack()
bouton = Button(fen, text="Fermer", command=fen.quit)
bouton.pack()
fen.mainloop()
"""
