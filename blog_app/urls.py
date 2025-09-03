from django.urls import path

from blog_app import views
urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("draft-list/", views.draft_list, name="draft-list"),
    path("draft-detail/<int:pk>/", views.draft_detail, name="draft-detail"),
    path("post-create/", views.post_create, name="post-create"),
]