import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from collections import Counter

# Set up the URL and headers
url = "https://www.google.com/search?q=software+Developer+canada&ibp=htl;jobs&sa=X&ved=2ahUKEwj99J7in9X9AhUikmoFHQ9LCV8QutcGKAF6BAgNEAU&sxsrf=AJOqlzUrF1wO-zV4GgtuiO7XaRrApCq8dA:1678584826024#htivrt=jobs&htidocid=inJ0us9iTNsAAAAAAAAAAA%3D%3D&fpstate=tldetailhttps://www.google.com/search?q=software+Developer+canada&ibp=htl;jobs&sa=X&ved=2ahUKEwj99J7in9X9AhUikmoFHQ9LCV8QutcGKAF6BAgNEAU&sxsrf=AJOqlzUrF1wO-zV4GgtuiO7XaRrApCq8dA:1678584826024#htivrt=jobs&htidocid=inJ0us9iTNsAAAAAAAAAAA%3D%3D&fpstate=tldetail"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# Get the HTML content and parse it using BeautifulSoup
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Define a function to extract text from the HTML
def get_span(soup, class_name):
    return soup.find('span', class_=class_name).get_text()

# Extract the desired text and count the words
class_name = 'HBvzbc'
text = get_span(soup, class_name)
word_count = Counter(text.split())

# Define the search words and find the counts of each one in the text
search_words = {"Excel", "UX", "Python", "JavaScript", 'SQL', "Java",
                "UI", "Rust", "React", "React Native", "MongoDB", "Express", "Node", "PostGreSQL", "Vue", "Tailwind", "SAAS", "Flask", "Django", "ExpressJS", "Swift", "C#", "C", "C++", "HTML", "CSS"}
results = {word: word_count[word] for word in search_words if word in word_count}
print (results)

# Create a bar chart of the results
# plt.bar(range(len(results)), list(results.values()), align='center')
# plt.xticks(range(len(results)), list(results.keys()), rotation=90)
# plt.xlabel('Search words')
# plt.ylabel('No. of times this skill is mentioned on Job Postings')
# plt.title('Skill required on Job Postings')
# plt.show()
