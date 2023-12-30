#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            pass
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return pagination information
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = []
        data_index = self.get_hyper_index(page, page_size)
        next_index = data_index.get('next_index')
        prev_index = data_index.get('prev_index')

        for i in range(page_size):
            row = self.dataset().get(next_index + i)
            if row:
                data.append(row)
            else:
                break

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if next_index else None,
            'prev_page': page - 1 if prev_index else None,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return requested page
        """
        return self.get_hyper(page, page_size)['data']
