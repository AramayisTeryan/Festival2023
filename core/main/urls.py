from django.urls import path
from .import views

urlpatterns=[
    path('', views.HomeListView.as_view(), name='index'),
    path('ticket/', views.TicketListView.as_view(), name='ticket')
]