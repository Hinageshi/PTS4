from RequestHandler import *
from Agent import *
from tkinter import *

rh = RequestHandler()
"""
a = rh.getRandomAgent()
print(a.getInfo())
a2 = rh.getOneAgent(6352373083)
print(a2.getInfo())
a3 = rh.getRandomAgentFromCountry('kk')
print(a3.getInfo())
for agent in rh.getSampleRandomAgents(5):
    print(agent.getInfo())
for agent in rh.getSampleRandomAgentsFromCountry(5, 'fr'):
    print(agent.getInfo())
"""
rh.getMetrics()
"""
fen = Tk()
cadre = Frame(fen, width=500, height=750, borderwidth=1)
cadre.pack(fill=BOTH)
label = Label(fen, text="Agent")
label.pack()
bouton = Button(fen, text="Fermer", command=fen.quit)
bouton.pack()
fen.mainloop()
"""
