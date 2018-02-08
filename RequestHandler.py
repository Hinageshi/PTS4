import urllib.request
import json
from Agent import Agent

class RequestHandler:

    
    def getRandomAgent(self):
        #get a random agent
        url = "http://pplapi.com/random.json"
        result = json.loads(urllib.request.urlopen(url).read().decode())
        jsonAgent = Agent(result['id'], result['country_name'], result['latitude'], result['longitude'], result['sex'], result['date_of_birth'],
                  result['age'], result['language'], result['religion'], result['income'], result['internet'], result['openness'],
                  result['conscientiousness'], result['extraversion'], result['agreeableness'], result['neuroticism'], result['id_str'])
        return jsonAgent;
