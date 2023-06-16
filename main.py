import configparser
from torrent_clients.clients.marcianoTorrent import MarcianoTorrentClient

config = configparser.ConfigParser()
config.read('config.ini')

client = MarcianoTorrentClient()
series = []

# Se cargan todos los titulos de las series del archivo
with open('series_list.txt') as file:
    titles = [line.strip() for line in file]

# Se la información necesaria de cada titulo si se encuentra
for title in titles:
    serie = client.get_serie_by_title(title)
    if serie:
        series.append(serie)
        print(serie)


