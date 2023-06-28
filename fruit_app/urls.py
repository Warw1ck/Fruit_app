
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruit_app.common.urls')),
    path('profile/', include('fruit_app.accounts.urls')),
    path('fruit/', include('fruit_app.fruit.urls')),

]
