from django.conf.urls import url
from .views import EmployeeViewSet

urlpatterns = [
    url(
        r'^employee/$',
        EmployeeViewSet.as_view({
            'get': 'list',
            'post': 'create'}),
        name="employee-all"
    ),
    url(
        r'^employee/(?P<pk>[0-9]+)$',
        EmployeeViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update'}),
        name="employee-single"
    ),
]
