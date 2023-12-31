from django_filters import rest_framework as filters

from .models import User


class UserFilter(filters.FilterSet):

    class Meta:
        model = User  # 模型名
        fields = {
            'name': ['icontains', 'exact', 'in'],  # i:ignore
            'age': ['icontains', 'exact', 'in', 'gte', 'lte'],  # http://localhost:8000/user/?age__gte=3
        }
