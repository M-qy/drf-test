from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filtersets import UserFilter
from .models import User
from .serializers import UserSerializer
from test_db.settings import LOG_OBJ


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        print('page: ', page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)

        print("serializer.data: ", serializer.data)
        print(type(serializer.data))
        result = Response(serializer.data)
        print(type(result.data[0]))
        print("result.data: ", result.data)
        print(type(result.data))
        return result


class UserRouteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    @action(detail=False, methods=['get'])
    def test(self, request):
        LOG_OBJ.debug('111111111111111111')
        return Response('haha')
