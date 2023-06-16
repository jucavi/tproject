class Serie:
    """Class representing a TV Serie."""
    
    def __init__(self, title, seasons=[]):
        """Constructor

        Args:
            title (str): The title of the serie
            seasons (list, optional): List of Season objects of the serie. Defaults to [].
        """
        self.title = title
        self.seasons = seasons

    def __str__(self):
        return """
    title: {}
    seasons: {}
    """.format(self.title, self.seasons)