import random as r

from django.shortcuts import render, redirect
from .models import Article, Categorie, UserResponse
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
        

    
