from torrent_clients.abstract.abstract_torrent import AbstractTorrentClient
from bs4 import BeautifulSoup
from lxml import etree
import requests
from torrent_clients.serie import Serie
from torrent_clients.season import Season


class MarcianoTorrentClient(AbstractTorrentClient):

    base_url = 'https://marcianotorrent.net'

    def __extract_url(self, link_element):
        """Extract href from anchor tag element

        Args:
            link_element (Tag): Anchor tag element

        Returns:
            str: href of the anchor tag element
        """
        return link_element['href']

    def __extract_season_name(self, link_element):
        """Extract the season name from anchor tag element

        Args:
            link_element (tag): Anchor tag element

        Returns:
            str: Season name normilized to "{number}ª Temporada"
        """
        img_element = link_element.find('img')
        full_name = img_element['alt']

        season_name = full_name.split('-')[-1].strip()
        season_name = season_name.replace('[720p]', '')

        return season_name.strip()

    def __extract_episodes_count(self, season_soup):
        """Extract the number of episodes for the given season

        Args:
            season_soup (BeautifullSoup): Beautifull soup object

        Returns:
            int: The number of episodes for the given season
        """
        dom = etree.HTML(str(season_soup))
        str_epidodes_count = dom.xpath(
            '/html/body/div[1]/section/div/div/div[1]/div[2]/p[1]/span[2]')[0].text

        return int(str_epidodes_count)

    def __extract_torrents(self, season_soup):
        """Returns a list of torrents for a season

        Args:
            season_soup (BeautifullSoup): Beautiful soup object

        Returns:
            list: List of torrents for a season
        """
        table_body = season_soup.find('tbody')

        torrents_links = table_body.find_all('a')

        return [self.__extract_url(torrent_link) for torrent_link in torrents_links]

    def __make_season(self, name, season_url):
        """Returns a season object for a given season url

        Args:
            name (str): Season name
            season_url (str): Season url

        Returns:
            Season: Season object or None if an error occurred
        """
        response = requests.get(season_url)

        if response.status_code == 200:
            season_soup = BeautifulSoup(response.text, 'html.parser')

            torrents = self.__extract_torrents(season_soup)
            episodes = self.__extract_episodes_count(season_soup)

            return Season(name, season_url, episodes, torrents)

        return None

    def __get_seasons_from_cards(self, soup):
        """Returns a list of all the seasons in the given beatifull soup object

        Args:
            soup (BeautifullSoup): Beautifull soup object

        Returns:
            list: List of all the seasons for the given Serie
        """
        seasons = []
        container = soup.find('div', {'class': 'search-list'})

        links = container.find_all('a')

        for link in links:
            url = self.__extract_url(link)

            if not url.startswith(self.base_url):
                url = self.base_url + url

            name = self.__extract_season_name(link).strip()

            if not any(name == season.name for season in seasons):
                season = self.__make_season(name, url)

                if season:
                    seasons.append(season)

        return seasons

    # Override
    def get_serie_by_title(self, title):
        """Returns a Serie object with all the information about it.

        Args:
            title (str): Series name to search for

        Returns:
            Serie: Series object if results are found or None otherwise
        """
        url = self.base_url +  '/busqueda'
        payload = {
            'q': title
        }

        response = requests.get(url, params=payload)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            seasons = self.__get_seasons_from_cards(soup)

            return Serie(title.title(), seasons)

        return None