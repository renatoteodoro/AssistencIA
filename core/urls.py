from django.contrib import admin
from django.urls import include, path

from core.views import DashboardView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
