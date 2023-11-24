from django.urls import path

from . import views

app_name = 'motors'
urlpatterns = [
    path('', views.MotorListView.as_view(), name='index'),
    path('search/', views.search_motors, name='search'),
    path('create/', views.create_motor, name='create'),
    path('<int:pk>/', views.MotorDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.update_motor, name='update'),
    path('delete/<int:pk>/', views.delete_motor, name='delete'),
    path('<int:pk>/comment/', views.create_comment, name='comment'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/create', views.CategoryCreateView.as_view(), name='create-category'),
]