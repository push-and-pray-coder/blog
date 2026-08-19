from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView): # GET Request -> List
    # template_name attribute renders specific html file
    template_name = "posts/list.html"
    # models attribute let django know which model (table) to retrieve data from
    model = Post
    # context-Object_name attribute allos changes to the name or how its called inside of templates
    context_object_name = "posts"

    # SELECT * FROM posts

class PostDetailView(DeleteView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): # post Request -> New Object /Empty form (HTML)
    template_name = "posts/new.html"
    model = Post
    # fields attribute is a list that allow us to enable/disable the inputs to render in the form
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        # This function helps us run vadliations before object creation
        form.instance.author = User.objects.last()
        return super().form_valid(form)

class PostUpdateView(UpdateView):  # POST Request -> A form to update an existing object
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView): # POST Request -> A form to delete an existing object
    template_name = "posts/delete.html"
    model = Post
    # success_url attribute allow us to redirect the user to another view if the request is successful
    success_url = reverse_lazy("post_list")