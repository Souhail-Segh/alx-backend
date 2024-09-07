import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page, page_size):
        """Returns a tuple with the first and last indexes of a pagination
        """
        start_pos = (page - 1) * page_size
        end_pos = page * page_size
        tuple_pos = (start_pos, end_pos)
        return (tuple_pos)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get sub-list using pagination indexes
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        ds = self.dataset()
        indexes = self.index_range(page, page_size)

        if len(ds) > indexes[1]:
            return (ds[indexes[0]:indexes[1]])
        return ([])
