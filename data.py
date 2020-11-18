import requests
import random
from bs4 import BeautifulSoup

top100movies = []
top100series = []
top5 = []
rating = []
top100 = []
years = []
random5 = []

def main():
    getMovies()
    #random5movies()
    #getSeries()
    #randomFilm()
    #print(randomFilm())

def getMovies():
    
    url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    movies = soup.find(id="main")
    movie_titles = movies.find_all("td", class_="titleColumn")
    movie_rating = movies.find_all("td", class_="ratingColumn imdbRating")

    for titles in movie_titles:
        title = titles.find("a").text.strip()
        year = titles.find("span", class_="secondaryInfo").text.strip()
        top100movies.append(title + " " + year)

    
    rating = [ratings.text.strip() for ratings in movie_rating]
    
    
    n = 1
    for i in range(0,100):
        if rating[i] != "":
            top100.append(str(n) + ". " + top100movies[i] + " [IMDB rating " + rating[i] + "]")
            n += 1
        else:
            top100.append(str(n) + ". " + top100movies[i] + " (not released)")
            n += 1
       
    #print(top100)

def randomFilm():
    top100.clear()
    getMovies()
    return random.choice(top100)


def getSeries():

    url = "https://www.imdb.com/chart/tvmeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=DTMQQVAXH0N3GCPXSM69&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_5"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    shows = soup.find(id="main")
    show_titles = shows.find_all("td", class_="titleColumn")
    show_rating = shows.find_all("td", class_="ratingColumn imdbRating")

    for titles in show_titles:
        title = titles.find("a").text.strip()
        year = titles.find("span", class_="secondaryInfo").text.strip()
        top100series.append(title + " " + year)
        
    rating = [ratings.text.strip() for ratings in show_rating]

    n = 1
    for i in range(0,100):
        if rating[i] != "":
            top100.append(str(n) + ". " + top100series[i] + " [IMDB rating " + rating[i] + "]")
            n += 1
        else:
            top100.append(str(n) + ". " + top100series[i] + " (not released)")
            n += 1

def randomSeries():
    top100.clear()
    getSeries()
    return random.choice(top100)

def top5movies():
    top100.clear()
    getMovies()
    top5 = top100[:5]
    temp = "\n"
    return (temp.join(top5))

def top5series():
    top100.clear()
    getSeries()
    top5 = top100[:5]
    temp = "\n"
    return (temp.join(top5))

def random5movies():
    start = 0
    end = 5
    top100.clear()
    random5.clear()
    getMovies()
    temp = "\n"
    while (start < end):
        random5.append(random.choice(top100))
        if len(random5) == len(set(random5)):
            start += 1
        else:
            random5.pop(start)
            start -= 1

    if (len(random5) != 5):
        random5.pop()
    
    return (temp.join(random5))

def random5series():
    start = 0
    end = 5
    top100.clear()
    random5.clear()
    getSeries()
    temp = "\n"
    while (start < end):
        random5.append(random.choice(top100))
        if len(random5) == len(set(random5)):
            start += 1
        else:
            random5.pop(start)
            start -= 1
    
    if (len(random5) != 5):
        random5.pop()
    
    return (temp.join(random5))


main()          # call main function 


""""film - Get a random film suggestion from the top 100 list
series - Get a random TV show suggestion from the top 100 list
film5 - Get the top 5 movies right now
series5 - Get the top 5 TV shows right now
randomfilms - Get 5 random films from the list
randomseries - Get 5 random TV shows from the list"""


