import imp
from django.urls import path
from .views import SnacksListView , SnackDetailView

urlpatterns = [
    path('snack_list',SnacksListView.as_view(), name='snack_list'),
    path('detail-view/<int:pk>',SnackDetailView.as_view(), name='snack_detail'),

]