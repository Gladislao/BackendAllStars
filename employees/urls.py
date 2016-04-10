from .views import CustomObtainAuthToken, employee_list, employee
from .views import top
from django.conf.urls import url


urlpatterns = [
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
    url(r'^list/$', employee_list, name='employee_list'),
    url(r'^list/top/(?P<kind>\w+)/(?P<quantity>\d+)/$', top, name='employee_list_top'),
    url(r'^(?P<employee_id>\d+)/$', employee, name='employee_detail'),
]
