from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('child1/',child1,name='child1'),
    path('child2/',child2,name='child2'),
]