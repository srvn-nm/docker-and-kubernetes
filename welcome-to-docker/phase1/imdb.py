import requests

def imdb(query):
    url = "https://imdb146.p.rapidapi.com/v1/find/"

    querystring = {"query":query}

    headers = {
	"X-RapidAPI-Key": "4f572370c6mshea36af5374dcaa6p10e8ddjsn40a8eb8b2bf2",
	"X-RapidAPI-Host": "imdb146.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    return response.json()