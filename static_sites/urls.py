from django.urls import path

from . import views

urlpatterns=[
    path('', views.show_landing_page, name="show_landing_page"),
    path('about/', views.show_about_page, name="show_about_page"),
    path('legal/', views.show_legal_page, name="show_legal_page"),
    path('admin-login/', views.AdminLogin.as_view(), name="show_admin_login"),
    path('example-pages/', views.show_example_pages, name="show_example_pages"),
]