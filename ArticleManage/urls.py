from django.urls import path
from . import views as v


urlpatterns = [
    path('indexUser/', v.indexUser, name='indexUser'),
    path('userArticles/', v.showUserArticles, name='allUserArticles'),
    path('createArticle/', v.createArticle, name='createArticle'),
    path('saveArticle/', v.saveArticle, name='saveArticle'),
    path('deleteArticle/<int:article_id>/', v.deleteArticle, name='deleteArticle'),
    path('userCategories/', v.userCategories, name='userCategories'),
    path('createCategorie/', v.createCategorie, name='createCategorie'),
    path('saveCategorie/', v.saveCategorie, name='saveCategorie'),
    path('userArticlesFl/', v.filterByCategory, name='filterByCategory'),
    path('createResponse/<int:article_id>', v.createResponseForm, name='createResponse'),
    path('saveResponse/<int:article_id>', v.createResponse, name='saveResponse'),
    path('listResponses/<int:article_id>', v.listResponses, name='listResponses'),
    path('addLike/<int:id>/<int:art_id>', v.addLike, name='addLike'),
    path('addDislike/<int:id>/<int:art_id>', v.addDisLike, name='addDislike'),
]