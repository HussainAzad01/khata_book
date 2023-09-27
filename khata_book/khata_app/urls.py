from django.urls import path
from . import views

urlpatterns = [
    path("", views.signupUser, name='signup'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path("add-client", views.add_client, name='add-client'),
    path("client-list", views.client_list, name='client-list'),
    path("client-khata/<str:client_name>", views.client_detail_view, name='client-khata'),
    path("add-client/<str:client_name>", views.add_client, name='add-goods'),
    path("delete-goods/<str:client_name>/<str:good_id>", views.delete_goods, name='delete-goods'),
    path('search', views.search, name='search'),
]