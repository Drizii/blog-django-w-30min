from django.urls import re_path

from .views import PostListView, PostDetailView

urlpatterns = [
    re_path(r"^$", PostListView.as_view(), name="post-list"),
    # re_path(r"^(?P<slug>[-\W]+)/$", PostDetailView.as_view(), name="post-detail")  #dlaczego nie dziala?
    re_path(r"^tag/(?P<slug>[-\w]*)/$", PostDetailView.as_view(), name="post-detail")
]