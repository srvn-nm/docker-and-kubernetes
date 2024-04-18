import requests

def imdb(query):
    url = f"https://imdb-movies-web-series-etc-search.p.rapidapi.com/{query}.json"

    headers = {
	"X-RapidAPI-Key": "4f572370c6mshea36af5374dcaa6p10e8ddjsn40a8eb8b2bf2",
	"X-RapidAPI-Host": "imdb-movies-web-series-etc-search.p.rapidapi.com"
}

    response = requests.get(url, headers=headers)
    print(response.json())
    return response.json()