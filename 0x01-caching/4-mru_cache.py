#!/usr/bin/env python3
"""MRU caching module
"""
from typing import Dict, Any, Union
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUOCache Class
    Using Most recent used (MRU) caching principal
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
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard, _ = self.cache_data.popitem(last=True)
                print(f'DISCARD: {discard}')

    def get(self, key: Any) -> Union[Dict, None]:
        """get value assigned to key
        """
        if key is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key, last=True)
                return self.cache_data[key]
        return None
