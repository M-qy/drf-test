from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationPlus(LimitOffsetPagination):
    max_limit = 100
