import requests
import json
import matplotlib.pyplot as plt
from flask import Flask, render_template
import plotly.graph_objs as go
import plotly
from bs4 import BeautifulSoup
from collections import Counter


url = "https://www.google.com/search?q=software+Developer+canada&ibp=htl;jobs&sa=X&ved=2ahUKEwj99J7in9X9AhUikmoFHQ9LCV8QutcGKAF6BAgNEAU&sxsrf=AJOqlzUrF1wO-zV4GgtuiO7XaRrApCq8dA:1678584826024#htivrt=jobs&htidocid=inJ0us9iTNsAAAAAAAAAAA%3D%3D&fpstate=tldetailhttps://www.google.com/search?q=software+Developer+canada&ibp=htl;jobs&sa=X&ved=2ahUKEwj99J7in9X9AhUikmoFHQ9LCV8QutcGKAF6BAgNEAU&sxsrf=AJOqlzUrF1wO-zV4GgtuiO7XaRrApCq8dA:1678584826024#htivrt=jobs&htidocid=inJ0us9iTNsAAAAAAAAAAA%3D%3D&fpstate=tldetail"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# app = Flask(__name__)

# @app.route("/")

def get_span(soup, class_name):
    span = str(soup.find_all('span', class_=class_name)).replace('<br/>', '^')
    span = BeautifulSoup(span, 'html.parser').get_text().replace('^', '<br/>')
    return span


class_name = 'HBvzbc'
text = get_span(soup, class_name)


words = text.split()
word_count = Counter(words)

search_words = {"Excel", "UX", "Python", "JavaScript", 'SQL', "Java", "Angular",
                "UI", "Oracle", "Jira", "MS SQL Server", "Attention to detail", "Excellent communication skills", "Windows", "NoSQL", "GraphQL", "Rust", "React", "React Native", "MongoDB", "Express", "Node", "PostGreSQL", "Vue", "Tailwind", "SAAS", "Flask", "Django", "ExpressJS", "Swift", "C#", "C", "C++", "HTML", "CSS", ".Net", "Gitlab", "XML", "Jenkins", "Kafka", "Redis", "Ruby", "Git", "Microsoft Azure", "Amazon Web Services", "Google Cloud Platform", "Dockers", "Linux", "Kubernetes", "Ubuntu"}

results = {}

for word in search_words:
    if word in word_count:
        results[word] = word_count[word]

#create a bar chart of the results
def create_bar_chart():
    plt.bar(range(len(results)), list(results.values()), align='center')
    plt.xticks(range(len(results)), list(results.keys()), rotation=90)
    plt.xlabel('Skills / Programming Languages')
    plt.ylabel('No. of times this skill is mentioned on Job Google Job Board')
    plt.title('Google Job Board Data')
    plt.show()

create_bar_chart()
