from django.urls import path

from . import views

urlpatterns = [
    path('', views.options, name='options'),
    path('add/', views.add, name='add'),
    path('sub/', views.sub, name='sub'),
    path('mul/', views.mul, name='mul'),
    path('div/', views.div, name='div'),
    path('nuts/', views.nuts, name='nuts'),
    path('add/caladd', views.caladd, name='caladd'),
    path('sub/calsub/', views.calsub, name='calsub'),
    path('mul/calmul/', views.calmul, name='calmul'),
    path('div/caldiv/', views.caldiv, name='caldiv'),
    path('nuts/calnuts/', views.calnuts, name='calnuts'),
]
