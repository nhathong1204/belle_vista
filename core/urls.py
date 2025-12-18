from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("", views.index, name="index"),
    path("privacy-policy/", views.privacy_policy, name="privacy-policy"),
    path("blogs/", views.list_blogs, name="blogs"),
    path("blogs/<str:slug>/", views.blog_detail, name="blog-detail"),
    path("ajax-contact-form", views.ajax_contact_form, name="ajax-contact-form"),
]
