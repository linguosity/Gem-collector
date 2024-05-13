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


]