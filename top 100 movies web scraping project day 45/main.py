from bs4 import BeautifulSoup
import requests
import lxml

response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_html_code=response.text

soup=BeautifulSoup(website_html_code,'html.parser')

movies_html_list=soup.select(selector=".listicleItem_listicle-item__title__BfenH")
movies_list=[i.get_text() for i in movies_html_list]
movies_list_sorted=[]

for i in range(0,len(movies_list)):
    movies_list_sorted.append(movies_list[len(movies_list)-1-i])

print(movies_list_sorted)

with open("movie_list.txt","w") as file:
    for i in movies_list_sorted:
        file.write(i+"\n")
