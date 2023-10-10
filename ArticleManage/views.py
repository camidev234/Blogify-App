import random as r

from django.shortcuts import render, redirect
from .models import Article, Categorie, UserResponse
from django.views.decorators.cache import never_cache
# Create your views here.


import random as r
from django.shortcuts import render
from .models import Article

def indexUser(request):
    articles = list(Article.objects.all())
    n = len(articles)
    user = request.user
    if n >= 1:
        numArticles = max(n, r.randrange(n))
        choiceArticles = r.sample(articles, numArticles)
        state = True
        return render(request, 'indexUser.html', {
            'allArticles': articles,
            'choiceArticles': choiceArticles,
            'user': user,
            'state': state
        })
    else:
        state = False
        message = 'Articles is empty'
        return render(request, 'indexUser.html', {
            'state': state,
            'message': message
        })
        
@never_cache
def showUserArticles(request):
    user = request.user
    userArticles = Article.objects.filter(user_id=user.id)
    
    articles = []
    
    for article in userArticles:
        articles.append(article)
    
    return render(request, 'userArticles.html', {
        'userArticles': userArticles,
        'user': user
    })
    
def createArticle(request):
    user = request.user
    categories = Categorie.objects.all()
    return render(request, 'createArticle.html', {
        'categories': categories,
        'user': user
    })
    
def saveArticle(request):
    user = request.user
    if request.method == 'POST':
        Article.objects.create(
            categorie_id = request.POST['categorie'],
            user_id = user.id,
            title = request.POST['title'],
            description = request.POST['description']
        )
        
        return redirect('indexUser')


    
