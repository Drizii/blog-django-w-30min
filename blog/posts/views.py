from django.views.generic import ListView, DetailView

from .models import Post as PostModel


class PostListView(ListView):
    model = PostModel

    def get_queryset(self):
        return PostModel.object.published()
        # return Post.object.published()


class PostDetailView(DetailView):
    model = PostModel