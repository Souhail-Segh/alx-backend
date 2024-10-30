#!/usr/bin/env python3
"""FIFO caching module
"""
from typing import Dict, Any, Union
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFOCache Class
    Using FIFO caching principal
    """

    def __init__(self):
        """initiate BasicCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: Any, item: Any):
        """put key and item in the dict
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.cache_data.popitem(last=False)
                print(f'DISCARD: {discard}\n')
            self.cache_data[key] = item

    def get(self, key: Any) -> Union[Dict, None]:
        """get value assigned to key
        """
        if key is not None:
            if key in self.cache_data:
                return self.cache_data[key]
        return None
