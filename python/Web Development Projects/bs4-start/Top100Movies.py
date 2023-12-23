from bs4 import BeautifulSoup
import requests

info = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

all_info = BeautifulSoup(info, "html.parser")
movies = []
movies = [movie.getText() + '\n' for movie in all_info.find_all(name="h3", class_="title")][::-1]

with open("Top 100 Movies To Watch.txt", mode='w') as file:
    file.writelines(movies)