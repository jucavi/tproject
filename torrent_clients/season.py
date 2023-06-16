class Season:
    """Class representing season in the series."""

    def __init__(self, name, url, episodes=0, torrents=[]):
        """Constructor

        Args:
            name (str): Season name
            url (str): Season url
            episodes (int, optional): Number of episodes for the season. Defaults to 0.
            torrents (list, optional): List of torrents urls for episodes downloads. Defaults to [].
        """
        self.name = name
        self.url = url
        self.episodes = episodes
        self.torrents = torrents


    def __str__(self):
        return """
    title: {}
    episodes: {}
    torrents: {}
    """.format(self.name, self.episodes, self.torrents)

