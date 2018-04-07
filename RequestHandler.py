import urllib.request
import json
from Agent import Agent

class RequestHandler:

    countryShort = ['ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'ao', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gd', 'ge', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gq', 'gr', 'gt', 'gu', 'gw', 'gy', 'hk', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'ks', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz','va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'za', 'zm', 'zw']
    countryLong = ['Andorra', 'United Arab Emirates', 'Afghanistan', 'Antigua and Barbuda', 'Anguilla', 'Albania', 'Armenia', 'Angola', 'Argentina', 'American Samoa', 'Austria', 'Australia', 'Aruba', 'Åland Islands', 'Azerbaijan', 'Bosnia and Herzegovina', 'Barbados', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'Saint Barthélemy', 'Bermuda', 'Brunei Darussalam', 'Plurinational State of Bolivia', 'Brazil', 'Bahamas', 'Bhutan', 'Botswana',  'Belarus', 'Belize', 'Canada', 'Cocos (Keeling) Islands', 'The Democratic Republic of the Congo', 'Central African Republic', 'Congo', 'Switzerland', 'Côte d Ivoire', 'Cook Islands', 'Chile', 'Cameroon', 'China', 'Colombia', 'Costa Rica', 'Cuba', 'Cabo Verde', 'Curaçao', 'Christmas Island', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic', 'Algeria', 'Ecuador', 'Estonia', 'Egypt', 'Western Sahara', 'Eritrea', 'Spain', 'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'Federated States of Micronesia', 'Faroe Islands', 'France', 'Gabon', 'Grenada', 'Georgia', 'Guernsey', 'Ghana', 'Gibraltar', 'Greenland', 'Gambia', 'Guinea', 'Equatorial Guinea', 'Greece', 'Guatemala', 'Guam', 'Guinea-Bissau', 'Guyana', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'Isle of Man', 'India', 'Iraq', 'Islamic Republic of Iran', 'Iceland', 'Italy', 'Jersey', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Comoros', 'Saint Kitts and Nevis', 'Democratic People s Republic of Korea', 'Republic of Korea', 'Kosovo', 'Kuwait', 'Cayman Islands', 'Kazakhstan', 'Lao People s Democratic Republic', 'Lebanon', 'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Libya', 'Morocco', 'Monaco', 'Republic of Moldova', 'Montenegro', 'Saint Martin (French part)', 'Madagascar', 'Marshall Islands', 'The former Yugoslav Republic of Macedonia', 'Mali', 'Myanmar', 'Mongolia', 'Macao', 'Northern Mariana Islands', 'Mauritania', 'Montserrat', 'Malta', 'Mauritius', 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'Niue', 'New Zealand', 'Oman', 'Panama', 'Peru', 'French Polynesia', 'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Saint Pierre and Miquelon', 'Pitcairn', 'Puerto Rico', 'State of Palestine', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Romania', 'Serbia', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Solomon Islands', 'Seychelles', 'Sudan', 'Sweden', 'Singapore', 'Saint Helena, Ascension and Tristan da Cunha', 'Slovenia', 'Svalbard and Jan Mayen', 'Slovakia', 'Sierra Leone', 'San Marino', 'Senegal', 'Somalia', 'Suriname', 'South Sudan', 'Sao Tome and Principe', 'El Salvador', 'Sint Maarten (Dutch part)', 'Syrian Arab Republic', 'Swaziland', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Timor-Leste', 'Turkmenistan', 'Tunisia', 'Tonga', 'Turkey', 'Trinidad and Tobago', 'Tuvalu', 'Taiwan, Province of China', 'United Republic of Tanzania', 'Ukraine', 'Uganda', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Holy See', 'Saint Vincent and the Grenadines', 'Bolivarian Republic of Venezuela', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Viet Nam', 'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']
    
    def APIRequest(self, agentNumber=None, numberOfAgents=1, country=None):
        url = "http://pplapi.com/"
        if(agentNumber is None):
            if(numberOfAgents == 1):
                if(country is None):
                    url += "random.json"
                else:
                    if(country in self.countryLong):
                        url += "country/" + self.countryShort[self.countryLong.index(country)] + "/random.json"
                    else:
                        print("This country doesn't exist.")
            elif(numberOfAgents > 1):
                if(country is None):
                    url += "batch/" + str(numberOfAgents) + "/sample.json"
                else:
                    if(country in self.countryLong):
                        url += "batch/" + str(numberOfAgents) + "/country/" + self.countryShort[self.countryLong.index(country)] + "/sample.json"
                    else:
                        print("This country doesn't exist.")
        else:
            url += str(agentNumber) + ".json"
        #print(url)
        return json.loads(urllib.request.urlopen(url).read().decode())
    """
    def getOneAgent(self, agentNumber):
        #get one precise agent
        url = "http://pplapi.com/" + str(agentNumber) + ".json"
        result = json.loads(urllib.request.urlopen(url).read().decode())
        jsonAgent = Agent(result)
        return jsonAgent
        
    def getRandomAgent(self):
        #get a random agent
        url = "http://pplapi.com/random.json"
        result = json.loads(urllib.request.urlopen(url).read().decode())
        jsonAgent = Agent(result)
        return jsonAgent

    def getRandomAgentFromCountry(self, country):
        #get a random agent from a precise country
        if country in self.countryShort:
            url = "http://pplapi.com/country/" + country + "/random.json"
            result = json.loads(urllib.request.urlopen(url).read().decode())
            jsonAgent = Agent(result)
            return jsonAgent
        else:
            print("This country doesn't exist.")

    def getSampleRandomAgents(self, numberOfAgents):
        #get a sample of n random agents
        sample = []
        url = "http://pplapi.com/batch/" + str(numberOfAgents) + "/sample.json"
        result = json.loads(urllib.request.urlopen(url).read().decode())
        for agent in result:
           sample.append(Agent(agent))
        return sample

    def getSampleRandomAgentsFromCountry(self, numberOfAgents, country):
        #get a sample of n random agents from a precise country
        if(country in self.countryShort):
            sample = []
            url = "http://pplapi.com/batch/" + str(numberOfAgents) + "/country/" + country + "/sample.json"
            result = json.loads(urllib.request.urlopen(url).read().decode())
            for agent in result:
               sample.append(Agent(agent))
            return sample
        else:
            print("This country doesn't exist.")
    """
    def getMetrics(self):
        #get API metrics
        url = "http://pplapi.com/metrics.json"
        result = json.loads(urllib.request.urlopen(url).read().decode())
        metrics = {}
        metrics['database_size'] = result['database_size']
        metrics['algorithm'] = result['checksum']['algorithm']
        metrics['parameters'] = result['checksum']['parameters']
        metrics['agent_space'] = result['checksum']['agent_space']
        metrics['population'] = result['population']
        return metrics

    def printCountries(self):
        for i in range (0, len(self.countryShort)):
            print(self.countryShort[i] + " - " + self.country[i])
        print("countryShort : " + str(len(self.countryShort)))
        print("country : " + str(len(self.country)))
