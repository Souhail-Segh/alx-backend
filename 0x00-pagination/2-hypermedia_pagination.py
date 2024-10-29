#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page, page_size) -> Tuple[int, int]:
    """
    index_range returns a tuple with the first and last indexes of a pagination
    """
    start_pos = (page - 1) * page_size
    end_pos = page * page_size
    tuple_pos = (start_pos, end_pos)
    return (tuple_pos)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get sub-list using pagination indexes
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        ds = self.dataset()
        start, end = index_range(page, page_size)

        if (len(ds) > end):
            return (ds[start:end])
        return ([])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get dict with all sub-list pagination data and config
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        ds = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = len(ds) / page_size
        total_pages = math.ceil(total_pages)

        hyper = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < page_size else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper
