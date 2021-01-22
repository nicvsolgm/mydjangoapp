from django.shortcuts import render
from .models import Article
from ckeditor.fields import RichTextField
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


#from . import forms
# Create your views here.


# def home(request):
#    header = 'Press Release'
#    context = {
#        "articles": Article.objects.all().order_by('-a_date_posted'),
#        "header": header
#    }
#    return render(request, 'article/home.html', context)


class ArticleListView(ListView):
    model = Article
    template_name = 'article/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'articles'
    ordering = ['-a_date_posted']
    paginate_by = 1


# @login_required()
# def article_create(request):
#    if request.method == 'POST':
#        form = forms.CreateArticle(request.POST, request.FILES)
#        if form.is_valid():
#            instance = form.save(commit=False)
#            instance.author = request.user
#            instance.save()
#            return redirect('article-home')
#    else:
#        form = forms.CreateArticle()
#    return render(request, 'articles/article_create.htm', {'form': form})

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['a_title', 'a_content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
