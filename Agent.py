import urllib.request
import json

class Agent:
    # properties = dict
    def __init__(self, properties):
        self.properties = properties
        
    def getInfo(self):
        return "Agent #" + str(self.properties['id']) + "\nLocation :\n\tCountry : " + self.properties['country_name'] + "\n\tGPS : (" + str(self.properties['latitude']) + ", " + str(self.properties['longitude']) + ")\nDemographics :\n\tSex : " + self.properties['sex'] + "\n\tDate of Birth : " + self.properties['date_of_birth'] + "\n\tAge : " + str(self.properties['age']) + "\n\tLanguage : " + self.properties['language'] + "\n\tReligion : " + self.properties['religion'] + "\n\tIncome : $" + str(self.properties['income']) + "\n\tInternet : " + str(self.properties['internet']) + "\nPersonality :\n\tOpenness : " + str(self.properties['openness']) + "\n\tConcientiousness : " + str(self.properties['conscientiousness']) + "\n\tExtraversion : " + str(self.properties['extraversion']) + "\n\tAgreeableness : " + str(self.properties['agreeableness']) + "\n\tNeuroticism : " + str(self.properties['neuroticism']) + "\nMapping :\n\tAlpha ID : " + self.properties['id_str']

