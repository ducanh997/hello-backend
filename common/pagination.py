import math
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class StandardPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100000

    def get_paginated_response(self, data):
        page_number = int(self.request.query_params.get(self.page_query_param, 1))
        page_size = self.get_page_size(self.request)

        return Response(OrderedDict([
            ('total_items', self.page.paginator.count),
            ('page_size', page_size),
            ('page', page_number),
            ('results', data),
            ('total_pages', math.ceil(self.page.paginator.count / page_size))
        ]))
