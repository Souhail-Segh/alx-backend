#!/usr/bin/env python3
"""Dict caching module
"""
from typing import Dict, Any, Union
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class
    Using Dict caching principal
    """

    def __init__(self):
        """initiate BasicCache
        """
        super().__init__()

    def put(self, key: Any, item: Any):
        """put key and item in the dict
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: Any) -> Union[Dict, None]:
        """get value assigned to key
        """
        if key is not None:
            if key in self.cache_data:
                return self.cache_data[key]
        return None
