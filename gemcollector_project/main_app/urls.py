from django.urls import path
from . import views
from main_app.views import GemList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gems/', GemList.as_view(), name='index'),
    path('gems/<int:gem_id>/', views.gems_detail,name='detail'),
    path('gems/create/', views.GemCreate.as_view(), name='gem_create'),
    path('gems/<int:pk>/update/', views.GemUpdate.as_view(), name='gems_update'),
    path('gems/<int:pk>/delete/', views.GemDelete.as_view(), name='gems_delete'),
    path('gems/<int:pk>/add_jewelry/', views.add_jewelry, name='add_jewelry'),


    # Toy Assoc Path
    path('cats/<int:pk>/assoc_toy/<int:toy_pk>', views.assoc_toy, name='assoc_toy'),
    path('cats/<int:pk>/assoc_delete/<int:toy_pk>', views.assoc_delete, name='assoc_delete'),

    # Toys Pathing 
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]