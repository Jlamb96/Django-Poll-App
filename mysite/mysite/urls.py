
from django.contrib import admin
from django.urls import include, path
admin.site.site_header = "Jeremy's Portfolio Django Project"
admin.site.index_title = "Welcome to my Django project"
urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
