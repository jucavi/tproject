import requests

url = "https://api.themoviedb.org/3/search/tv?query={}&include_adult=false&language=en-US&page=1".format("yellowjacket")

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjOWM0MjFhNWQ2ZDFjZTdjM2IwNWJhMjMzMzU1ODkzZCIsInN1YiI6IjY0ODg3YjQxNmY4ZDk1MDBjODhiNGEzMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ur4nFIgDIWTiFuDUjDXFgpYdXN39HBu6ZWH2XJQyb7w"
}

response = requests.get(url, headers=headers)

print(response.json()['results'][0]['id'])