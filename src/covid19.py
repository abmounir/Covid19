from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import requests 

class Covid:
    def __init__(self):
        self.countries = []
        self.total_cases = []
        self.new_cases = []
        self.total_deaths = []
        self.new_deaths = []
        self.total_recovered = []
        self.active_cases = []
        self.critical = []
        self.tot_cases_1m_pop = []
        self.deaths_1m_pop = []
        self.total_tests = []
        self.tests_1m_pop = []
        self.population = []
        self.link = 'https://www.worldometers.info/coronavirus/'
        self.page = requests.get(self.link)
        self.soup = bs(self.page.content, 'html.parser')
        for tr in self.soup.tbody.find_all('tr')[7:]:
            self.countries.append(tr.find_all('td')[1].text)
            self.total_cases.append(tr.find_all('td')[2].text)
            self.new_cases.append(tr.find_all('td')[3].text)
            self.total_deaths.append(tr.find_all('td')[4].text)
            self.new_deaths.append(tr.find_all('td')[5].text)
            self.total_recovered.append(tr.find_all('td')[6].text)
            self.active_cases.append(tr.find_all('td')[7].text)
            self.critical.append(tr.find_all('td')[8].text)
            self.tot_cases_1m_pop.append(tr.find_all('td')[9].text)
            self.deaths_1m_pop.append(tr.find_all('td')[10].text)
            self.total_tests.append(tr.find_all('td')[11].text)
            self.tests_1m_pop.append(tr.find_all('td')[12].text)
            self.population.append(tr.find_all('td')[13].text)
    def get_total_cases(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.total_cases[index]
    def get_new_cases(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.new_cases[index]
    def get_total_deaths(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.total_deaths[index]
    def get_new_deaths(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.new_deaths[index]
    def get_total_recovered(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.total_recovered[index]
    def get_active_cases(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.active_cases[index]
    def get_critical(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.critical[index]
    def get_population(self,country):
        i=0
        index=0
        for c in self.countries:
            if str(country).lower()==c.lower():
                index=i
            else:
                i+=1
        return self.population[index]

    def get_country_data(self, country):
        i = 0
        index = 0
        for c in self.countries:
            if str(country).lower() == c.lower():
                index = i
            else:
                i += 1
        data_dict={}
        data_dict['new_cases'] = self.new_cases[index]
        data_dict['total_cases'] = self.total_cases[index]
        data_dict['total_deaths'] = self.total_deaths[index]
        data_dict['new_deaths'] = self.new_deaths[index]
        data_dict['total_recovered'] = self.total_recovered[index]
        data_dict['active_cases'] = self.active_cases[index]
        data_dict['critical'] = self.critical[index]
        data_dict['tot_cases_1m_pop'] = self.tot_cases_1m_pop[index]
        data_dict['deaths_1m_pop'] = self.deaths_1m_pop[index]
        data_dict['total_tests'] = self.total_tests[index]
        data_dict['tests_1m_pop'] = self.tests_1m_pop[index]
        data_dict['population'] = self.population[index]
        return data_dict
    


# cv=Covid()
# print(Covid().get_population('algeria'))


    
