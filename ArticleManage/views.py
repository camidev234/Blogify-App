import random as r

from django.shortcuts import render, redirect
from .models import Article, Categorie, UserResponse
from django.views.decorators.cache import never_cache
# Create your views here.


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
    userArticles = Article.objects.filter(user=user.id)
    userCategories = Categorie.objects.filter(user_id=user.id)
    articles = []
    for article in userArticles:
        articles.append(article)
    
    cont = len(userArticles)
    
    return render(request, 'userArticles.html', {
        'userArticles': userArticles,
        'user': user,
        'userCategories': userCategories,
        'cont': cont
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
    
   
def deleteArticle(request, article_id):
    article = Article.objects.get(id=article_id)
    
    if request.method == 'GET':
        article.delete()
        return redirect('allUserArticles')

    
def userCategories(request):
    user = request.user
    
    userCategories = Categorie.objects.filter(user_id=user.id)
    
    return render(request, 'userCategories.html', {
        'userCategories': userCategories
    })    

def createCategorie(request):
    user = request.user
    return render(request, 'createCategorie.html', {
        'user': user
    })
    
def saveCategorie(request):
    user = request.user
    if request.method == 'POST':
        Categorie.objects.create(
            user_id = user.id,
            categorie = request.POST['categorie']
        )
        
        return redirect('userCategories')
    else:
        return redirect('createCategorie')
    
def filterByCategory(request):
    categorie = request.POST['categorieFilter']
    articles = []
    if categorie == 'All':
        return redirect('allUserArticles')
    
    articlesByCategorie = Article.objects.filter(categorie_id=categorie)
    for article in articlesByCategorie:
        articles.append(article)
        
    cont = len(articles)
    
    categories = Categorie.objects.all()
    
    return render(request, 'userArticles.html', {
        'userArticles': articlesByCategorie,
        'userCategories': categories,
        'cont': cont
    })


def createResponseForm(request, article_id):
    article = Article.objects.get(id=article_id)
    
    return render(request, 'createResponse.html', {
        'article': article
    })

def createResponse(request, article_id):
    if request.method == 'POST':
        UserResponse.objects.create(
            user_id = request.user.id,
            article_id = article_id,    
            response = request.POST['response']
        )
    
        return redirect('indexUser')
    else:
        return redirect('indexUser')
    
def listResponses(request, article_id):
    articleResponses = UserResponse.objects.filter(article=article_id)
    article = Article.objects.get(id=article_id)
    cont = len(articleResponses)
    return render(request, 'articleResponses.html', {
        'articleResponses': articleResponses,
        'article': article,
        'cont': cont
    })
    

def addLike(request, id, art_id):
    if request.method == 'GET':
        user = request.user  # Obtén al usuario actual que dio like
        article_response = UserResponse.objects.get(id=id)

        # Comprueba si el usuario ya ha dado like a esta respuesta
        if article_response.likes.filter(id=user.id).exists():
            # Si el usuario ya dio like, quítalo
            article_response.likes.remove(user)
        else:
            # Si el usuario no ha dado like, agrégalo
            article_response.likes.add(user)

        return redirect('listResponses', article_id=art_id)
    
def addDisLike(request, id, art_id):
    if request.method == 'GET':
        user = request.user 
        article_response = UserResponse.objects.get(id=id)

        # Comprueba si el usuario ya ha dado like a esta respuesta
        if article_response.dislikes.filter(id=user.id).exists():
            article_response.dislikes.remove(user)
        else:
            article_response.dislikes.add(user)

        return redirect('listResponses', article_id=art_id)



    
