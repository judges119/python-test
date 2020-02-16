from django.urls import path

from . import views

urlpatterns = [
    path('', views.CardList.as_view(), name='card_list'),
    path('<int:pk>', views.CardDetail.as_view(), name='card_detail'),
    path('create', views.CardCreate.as_view(), name='card_create'),
    path('delete/<int:pk>', views.CardDelete.as_view(), name='card_delete'),
]