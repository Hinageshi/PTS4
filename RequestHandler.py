import urllib.request
import json
from Agent import Agent

class RequestHandler:

    countryShort = ['ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'ao', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gd', 'ge', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gq', 'gr', 'gt', 'gu', 'gw', 'gy', 'hk', 'hn' 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'ks', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz','va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'za', 'zm', 'zw']
    
    def getOneAgent(self, agentNumber):
        #get one precise agent
        url = "http://pplapi.com/" + str(agentNumber) + ".json"
        result = json.loads(urllib.request.urlopen(url).read().decode())
        jsonAgent = Agent(result['id'], result['country_name'], result['latitude'], result['longitude'], result['sex'], result['date_of_birth'],
                  result['age'], result['language'], result['religion'], result['income'], result['internet'], result['openness'],
                  result['conscientiousness'], result['extraversion'], result['agreeableness'], result['neuroticism'], result['id_str'])
        return jsonAgent
        
    def getRandomAgent(self):
        #get a random agent
        url = "http://pplapi.com/random.json"
        result = json.loads(urllib.request.urlopen(url).read().decode())
        jsonAgent = Agent(result['id'], result['country_name'], result['latitude'], result['longitude'], result['sex'], result['date_of_birth'],
                  result['age'], result['language'], result['religion'], result['income'], result['internet'], result['openness'],
                  result['conscientiousness'], result['extraversion'], result['agreeableness'], result['neuroticism'], result['id_str'])
        return jsonAgent

    def getRandomAgentFromCountry(self, country):
        #get a random agent in a precise country
        if country in countryShort:
            url = "http://pplapi.com/country/" + country + "/random.json"
            result = json.loads(urllib.request.urlopen(url).read().decode())
            jsonAgent = Agent(result['id'], result['country_name'], result['latitude'], result['longitude'], result['sex'], result['date_of_birth'],
                      result['age'], result['language'], result['religion'], result['income'], result['internet'], result['openness'],
                      result['conscientiousness'], result['extraversion'], result['agreeableness'], result['neuroticism'], result['id_str'])
            return jsonAgent
        else:
            print("This country doesn't exist.")
