from django.db.models import Sum, Avg, Count, Aggregate
from django.http import FileResponse, HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_redis import get_redis_connection

from .filtersets import UserFilter
from .serializers import *
from .models import *
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
    def test(self, request, *args, **kwargs):
        LOG_OBJ.debug('111111111111111111')
        return Response('haha')

    @action(detail=True, methods=['get'])  # http://localhost:8888/user/1/test_detail/
    def test_detail(self, request, *args, **kwargs):
        return Response(f'{kwargs.get("pk")} {type(kwargs.get("pk"))}')

    @action(detail=False, methods=['get'])
    def redis_test(self, request, *args, **kwargs):
        conn = get_redis_connection("default")
        conn.set('key', 'helloworld!!!')
        result = conn.get('key').decode('utf-8')
        return Response(result)

    @action(detail=False, methods=['get'])
    def get_file(self, request, *args, **kwargs):
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
    def get_file_content(self, request, *args, **kwargs):
        with open('data.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        return Response(content)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=False, methods=['get'])
    def test(self, request, *args, **kwargs):
        model = self.get_serializer().Meta.model
        obj = model.objects.filter(id__in=model.objects.order_by("id").values('id')[1:3]).order_by("-member").first()
        return Response(obj.name)


class ConcatAggregate(Aggregate):
    function = 'STRING_AGG'
    template = "%(function)s(%(expressions)s, ',')"
    allow_distinct = True

    def __rand__(self, other):
        pass

    def __ror__(self, other):
        pass


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def test_group_by(self, request, *args, **kwargs):
        queryset = Book.objects.values('type').annotate(total_price=Sum('price'), avg_price=Avg('price'), num_books=Count('id'))
        result = Book.objects.values('type').annotate(names_concat=ConcatAggregate('name'))
        return JsonResponse(list(queryset) + (list(result)), safe=False)  # 字典设置True


class ZhtestViewSet(viewsets.ModelViewSet):
    queryset = Zhtest.objects.all()
    serializer_class = ZhtestSerializer

    @action(detail=False, methods=['get'])
    def add_desc(self, request, *args, **kwargs):
        import random
        eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        chi = ['一', '二', '三', '四', '五', '六', '七', '八', '九']
        shu = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for _ in range(100):
            save_list = []
            for _ in range(5000):
                i = random.sample(eng, 3)
                j = random.sample(chi, 3)
                k = random.sample(shu, 3)
                description = i[0] + j[1] + k[2] + i[1] + j[2] + k[0] + i[2] + j[0] + k[1]
                obj = Zhtest()
                obj.description = description
                save_list.append(obj)
            Zhtest.objects.bulk_create(save_list)
