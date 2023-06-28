from django.urls import path

from fruit_app.fruit import views

urlpatterns = [
    path('create', views.fruit_create, name='fruit-create'),
    path('<int:pk>/edit', views.fruit_edit, name='fruit-edit'),
    path('<int:pk>/details', views.fruit_details, name='fruit-details'),
    path('<int:pk>/delete', views.fruit_delete, name='fruit-delete'),
]