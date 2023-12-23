from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
artical_text = []
artical_link = []
all_anchor_tags = soup.find_all(class_ = "titleline")
for tag in all_anchor_tags:
    artical_text.append(tag.a.getText())
    artical_link.append(tag.a.get("href"))

up_votes = soup.find_all(name="span", class_ = "score")
artical_upvote = [int(score.getText().split(" ")[0]) for score in up_votes]

# Get the most popular article
highest_upvote = artical_upvote.index(max(artical_upvote))
print(artical_text[highest_upvote])
print(artical_link[highest_upvote])

"""
with open('website.html', mode = 'r') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.title.string)
all_anchor_tags = soup.find_all(name = "a")
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

# find h1 with id = name
heading = soup.find_all(name = "h1", id = "name")
print(heading)

section_heading = soup.find_all(name = "h3", class_ = "heading")
print(section_heading)

# select the anchor inside p
company_url = soup.select_one(selector="p a")
print(company_url)
"""