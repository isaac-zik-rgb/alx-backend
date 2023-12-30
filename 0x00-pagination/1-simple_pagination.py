#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters. """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """ Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ initialize instance. """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ getter function """
        if self.__dataset is None:
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return the appropriate page of the dataset. """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
