from django.urls import path
from dashboards.views import (AppealList
                              )

app_name = 'dashboards'

urlpatterns = [
    path('', AppealList.as_view(), name="dashboard"),

]
