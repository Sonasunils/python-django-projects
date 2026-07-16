from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    # Dynamic Integer URL
    path('vlog/<int:vlog_id>/', views.vlog),

    # Dynamic String URL
    path('category/<str:category_name>/', views.category),

    # Multiple Dynamic Parameters
    path('category/<str:category_name>/<int:vlog_id>/', views.vlog_details),
]