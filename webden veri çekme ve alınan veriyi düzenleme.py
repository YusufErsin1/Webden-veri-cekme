import requests
from bs4 import BeautifulSoup
#a=float(input("kaç üstü filmler bulmak istersiniz:"))
url="https://www.imdb.com/chart/top/"
response=requests.get(url)
print(response)
html_content=response.content
soup=BeautifulSoup(html_content,"html.parser")
#for i in soup.find_all("td",{"class":"titleColumn"}):
 #   print(i.text)
  #  print("-------------")
titles=soup.find_all("td",{"class":"titleColumn"})
ratings=soup.find_all("td",{"class":"ratingColumn"})#ikisininde uzunluğu aynı
#title ile rating sayısı aynı 
print(len(titles),len(ratings))
for title,rating in zip(titles,ratings):
    title=title.text
    rating=rating.text
    title=title.strip()
    title=title.replace("\n","")
    rating=rating.strip()
    rating=rating.replace("\n","")
    #if (a>float(rating)): yine çıkmayacak çünkü harfli sonuc var
        #print("filmin ismi:{} filmin ratingi".format(title,rating))
    print(title)
    print(rating)
    print("-----------")
