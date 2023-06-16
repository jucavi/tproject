import requests

class TMDBClient:

    base_url = 'https://api.themoviedb.org/3/'

    def __init__(self, token):
        """Constructor

        Args:
            token (str): Api token for themoviedb.org

            see: https://www.themoviedb.org API documentation
        """
        self.headers = {
                "accept": "application/json",
                "Authorization": "Bearer " + token
            }


    def get_id(self, query, first_air_date_year=None, include_adult=False, language='en-US', page=1, year=None):
        """Search for TV shows by their original, translated and also known as names, and return the corresponding identifier

        Args:
            query (str): Tv show title
            first_air_date_year (str, optional): First air date year. Defaults to None.
            include_adult (bool, optional): Includes adult. Defaults to False.
            language (str, optional): Language. Defaults to 'en-US'.
            page (int, optional): Pages. Defaults to 1.
            year (str, optional): Year. Defaults to None.

        Returns:
            int: identifier or None if not found
        """
        payload = {
            "query": query,
            "first_air_date_year": first_air_date_year,
            "include_adult": include_adult,
            "language": language,
            "page": page,
            "year": year
        }

        response = requests.get(self.base_url + 'search/tv', headers=self.headers, params=payload)

        if response.status_code == 200:
            results = response.json()['results']
            if len(results) > 0:
                return results[0]['id']

        return None


    def get_seasons_details(self, series_id, append_to_response=None, language='es-US'):
        """Returns a list of the number of chapters in the specified serie.

        Args:
            series_id (int): Identifier for the serie
            append_to_response (dict, optional): Append extra requests to any top level namespace. Defaults to None.
            language (str, optional): Language. Defaults to 'es-US'.

        Returns:
            list: Number of chapters in the specified serie for season
        """
        payload = {
            "append_to_response": append_to_response,
            "language": language
        }

        response = requests.get(self.base_url + 'tv/{}'.format(series_id), headers=self.headers, params=payload)

        if response.status_code == 200:
            result = response.json()
            seasons_caps = []

            for season in result['seasons']:
                if 'temporada' in season['name'].lower():
                    seasons_caps.append(season['episode_count'])


        return seasons_caps

