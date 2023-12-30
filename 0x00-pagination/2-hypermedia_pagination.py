#!/usr/bin/env python3
""" Hypermedia pagination """
import csv
import math
from typing import List, Tuple, Dict, Any


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ getter function """
        if self.__dataset is None:
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader]
        return self.__dataset


    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ return a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()[start:end]
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        return self.get_hyper(page, page_size)['data']
    
