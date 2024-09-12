"""
URL configuration for CID project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.landing_page, name='landing'),
    path('home/', views.homepage, name="homepage"),
    path('download/', views.download),
    path('download/<str:filename>/', views.download_file, name='download_file'),
    path('BOMS/rocc_boms/', views.rocc_boms),
    path('report_bug/', views.report_bug, name='report_bug'),
    path('bug_report_success/', views.bug_report_success, name='bug_report_success'),
    path('login/', views.login_view, name='login'),
    path('drwgs/rocc_drwgs/', views.rocc_drawings, name="drawings"),
    path('download-zip/', views.download_zip, name='download_zip'),
    path('view-files/', views.list_files, name='list_files'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('search/', views.search_view, name='search'),
    path('request_account/', views.account_request_view, name='request_account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
