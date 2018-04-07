import json
import matplotlib.pyplot as plt

class DisplayHandler:

    criterionShort = ["neuroticism", "language", "country_tld", "age", "income", "sex", "religion", "extraversion", "date_of_birth", "agreeableness", "conscientiousness", "openness", "internet"]
    criterionLong = ["Neuroticism", "Language", "Country", "Age", "Income", "Sex", "Religion", "Extraversion", "Date of Birth", "Agreeableness", "Conscientiousness", "Openness", "Internet"]
    criterionEquals = ["sex", "language", "country_tld", "religion", "internet"]
    
    def display(self, jsonData, mainCriterion, criteria=None):
        if(mainCriterion in self.criterionShort):
            if(criteria is None):
                valuesToDisplay = []
                nbData = 0
                avg = 0
                avgs = []
                if(isinstance(jsonData, dict)):
                    nbData = 1
                    valuesToDisplay.append(jsonData[mainCriterion])
                elif(isinstance(jsonData, list)):
                    for data in jsonData:
                        nbData += 1
                        valuesToDisplay.append(data[mainCriterion])
                for value in valuesToDisplay:
                    avg += value
                avg = avg / nbData
                for i in range(nbData):
                    avgs.append(avg)
                plt.title(self.criterionLong[self.criterionShort.index(mainCriterion)])
                plt.plot(valuesToDisplay)
                plt.plot(avgs, "r--", label= str(avg))
                plt.ylabel(self.criterionLong[self.criterionShort.index(mainCriterion)])
                plt.legend()
                plt.show()
            else:
                values = []
                for data in jsonData:
                    values.append(data)
                for key, val in criteria.items():
                    print(str(key) + " " + str(val))
                    print(str(val[0]) + ' ' + str(val[1]))
                    if(key not in self.criterionEquals):
                        print("not only equal")
                        if(val[1] == 'eq'):
                            for data in values:
                                if(data[key] != val[0]):
                                    print("not equal")
                                    print(data)
                                    values.remove(data)
                        elif(val[1] == 'sup'):
                            for data in values:
                                if(data[key] < val[0]):
                                    print("not superior")
                                    print(data)
                                    values.remove(data)
                        elif(val[1] == 'inf'):
                            for data in values:
                                if(data[key] > val[0]):
                                    print("not inferior")
                                    print(data)
                                    values.remove(data)
                    else:
                        print("only equal")
                        for data in values:
                            if(data[key] != val[0]):
                                print("not equal")
                                print(data)
                                values.remove(data)
                    print(values)
                print(values)
        else:
            print("mainCriterion isnt right")
            
