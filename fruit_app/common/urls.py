from django.urls import path

from fruit_app.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('dashboard', views.dashboard_page, name='dashboard')
]