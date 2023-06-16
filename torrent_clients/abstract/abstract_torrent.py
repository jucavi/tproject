from abc import ABC, abstractmethod


class AbstractTorrentClient(ABC):

    @abstractmethod
    def get_serie_by_title(self, title):
        pass
