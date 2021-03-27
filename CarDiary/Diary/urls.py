from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
#    path('g/<int:gameid>/', views.gotogame, name='g' )

]
