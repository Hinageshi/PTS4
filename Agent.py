import urllib.request
import json

class Agent:
    
    def __init__(self, id, country_name, latitude, longitude, sex, date_of_birth, age, language, religion, income, internet, openness, conscientiousness, extraversion, agreeableness, neuroticism, id_str):
        self.id = id
        self.country_name = country_name
        self.latitude = latitude
        self.longitude = longitude
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.age = age
        self.language = language
        self.religion = religion
        self.income = income
        self.internet = internet
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism
        self.id_str = id_str
        
        
    def getInfo(self):
        return "Agent #" + str(self.id) + "\nLocation :\n\tCountry : " + self.country_name + "\n\tGPS : (" + str(self.latitude) + ", " + str(self.longitude) + ")\nDemographics :\n\tSex : " + self.sex + "\n\tDate of Birth : " + self.date_of_birth + "\n\tAge : " + str(self.age) + "\n\tLanguage : " + self.language + "\n\tReligion : " + self.religion + "\n\tIncome : $" + str(self.income) + "\n\tInternet : " + str(self.internet) + "\nPersonality :\n\tOpenness : " + str(self.openness) + "\n\tConcientiousness : " + str(self.conscientiousness) + "\n\tExtraversion : " + str(self.extraversion) + "\n\tAgreeableness : " + str(self.agreeableness) + "\n\tNeuroticism : " + str(self.neuroticism) + "\nMapping :\n\tAlpha ID : " + self.id_str


