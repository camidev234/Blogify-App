from django.urls import path
from . import views as v


urlpatterns = [
    path('indexUser/', v.indexUser, name='indexUser'),
    path('userArticles/', v.showUserArticles, name='allUserArticles'),
    path('createArticle/', v.createArticle, name='createArticle'),
    path('saveArticle/', v.saveArticle, name='saveArticle'),
    path('userCategories/', v.userCategories, name='userCategories'),
    path('createCategorie/', v.createCategorie, name='createCategorie'),
    path('saveCategorie/', v.saveCategorie, name='saveCategorie'),
    path('userArticlesFl/', v.filterByCategory, name='filterByCategory'),
]