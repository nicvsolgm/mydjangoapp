from django.urls import path
from .import views
from .views import ArticleListView, ArticleCreateView, ArticleDetailView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    #path('', views.home, name='article-home'),
    path('', ArticleListView.as_view(), name='article-home'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk/', ArticleDetailView.as_view(), name='article-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
