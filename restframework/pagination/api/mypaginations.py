from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2

    page_query_param = 'pg'
    page_size_query_param = 'records'
    max_page_size = 5
    last_page_strings = 'last'


from rest_framework.pagination import LimitOffsetPagination


class MyLimiteOffsetPagination(LimitOffsetPagination):
    max_limit = 6
    default_limit = 3


# same as above attribute

from rest_framework.pagination import CursorPagination


class MyCursorPaginations(CursorPagination):
    page_size = 2
    ordering = ['id','roll']

