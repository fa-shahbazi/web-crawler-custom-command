from rest_framework.pagination import PageNumberPagination


class VerySmallPagination(PageNumberPagination):
    page_size = 3
