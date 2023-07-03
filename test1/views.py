from django.http import FileResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_redis import get_redis_connection

from .filtersets import UserFilter
from .serializers import *
from test_db.settings import LOG_OBJ


class UserTestViewSet(viewsets.ReadOnlyModelViewSet):
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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    @action(detail=False, methods=['get'])
    def test(self, request):
        LOG_OBJ.debug('111111111111111111')
        return Response('haha')

    @action(detail=False, methods=['get'])
    def redis_test(self, request):
        conn = get_redis_connection("default")
        conn.set('key', 'helloworld!!!')
        result = conn.get('key').decode('utf-8')
        return Response(result)

    @action(detail=False, methods=['get'])
    def get_file(self, request):
        file_path = 'data.txt'  # 本地文件路径

        try:
            # 打开文件并创建FileResponse对象
            file = open(file_path, 'rb')
            response = FileResponse(file)
            response['Content-Disposition'] = 'attachment; filename="file.txt"'  # 设置下载的文件名

            return response
        except FileNotFoundError:
            # 处理文件未找到的情况
            return HttpResponse('File not found')

    @action(detail=False, methods=['get'])
    def get_file_content(self, request):
        with open('data.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        return Response(content)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=False, methods=['get'])
    def test(self, request):
        model = self.get_serializer().Meta.model
        obj = model.objects.filter(id__in=model.objects.order_by("id").values('id')[1:3]).order_by("-member").first()
        return Response(obj.name)
