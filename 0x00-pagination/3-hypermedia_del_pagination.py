#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hyper index disct of pagination treating delete rows' situation
        """
        assert isinstance(index, int) and isinstance(page_size, int)
        assert index >= 0 and page_size > 0
        assert index is not None and index < len(self.indexed_dataset())

        data = []

        next_index = index + page_size

        i = index
        while (i < next_index):
            if not self.indexed_dataset().get(i):
                next_index += 1
            else:
                data.append(self.indexed_dataset()[i])
            i += 1

        hyper_data = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
            }

        return hyper_data
