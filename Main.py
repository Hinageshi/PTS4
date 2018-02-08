from RequestHandler import RequestHandler
from Agent import Agent

rh = RequestHandler();
a = rh.getRandomAgent();
print(a.getInfo());
