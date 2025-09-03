from django.urls import path

from blog_app import views
urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("draft-list/", views.draft_list, name="draft-list"),
    path("draft-detail/<int:pk>/", views.DraftDetailView.as_view, name="draft-detail"),
    path("post-create/", views.post_create, name="post-create"),
    path("post-update/<int:pk>/", views.post_update, name="post-update"),
    path("draft-publish/<int:pk>/", views.drafts_publish, name="draft-publish"),
]