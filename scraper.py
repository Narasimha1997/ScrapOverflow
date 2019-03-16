import requests
from bs4 import BeautifulSoup
import operator

class ScrapOverflow :

    def __init__(self, show_count = 5) :

        self.URL = "https://stackoverflow.com/search"
        self.COUNTS = show_count
        self.query_answer = None
    
    def get_html(self, question) :

        data = requests.get(self.URL, params = {
            "q" : question
        })

        self.query_answer = data.url

        return data.text
    
    def get_answers(self, html_data) :

        #performs data 
        soup = BeautifulSoup(html_data, 'html.parser')

        elements = soup.findAll("div", {"class" : "question-summary search-result"})

        formatted_answers = []

        print(len(elements))

        for element in elements :

            #prepare summary : 
            sub_soup = element
            votes = sub_soup.find("span", {"class" : 'vote-count-post'})
            answers = sub_soup.find("div", {"class" : "status answered"})

            #prepare Titles : 

            title = sub_soup.find('a', {"class" : "question-hyperlink"})

            data = {
                "votes" : int(votes.find("strong").text),
                
                "title" : title['title'],

                "URL" : "https://stackoverflow.com" + title["href"]
            }

            formatted_answers.append(data)

        
        #sort them according to votes : 

        formatted_answers.sort(key = operator.itemgetter('votes'), reverse = True)

        response =  {
            'answers' : formatted_answers if len(formatted_answers) < self.COUNTS else formatted_answers[:self.COUNTS],
            'more' : self.query_answer
        }

        return response




        