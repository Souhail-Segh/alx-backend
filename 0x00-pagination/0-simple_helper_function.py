#!/usr/bin/env python3
"""
Start and  end index corresponding to the range of indexes
to return in a list for those particular pagination parameters
"""


def index_range(page, page_size):
    """
    index_range returns a tuple with the first and last indexes of a pagination
    """
    start_pos = (page - 1) * page_size
    end_pos = page * page_size
    tuple_pos = (start_pos, end_pos)
    return (tuple_pos)
