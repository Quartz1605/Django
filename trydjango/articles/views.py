from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from .models import Article
from .forms import ArticleForm
# Create your views here.

def article_search_view(request):
  
  query_dict = request.GET
  
  query = query_dict.get("q")

  article_obj = None
  if query is not None:
    article_obj = Article.objects.get(id=query)




  

  context = {
    "object" : article_obj,
  }
  
  
  return render(request,"articles/search.html",context=context)










def article_detail_view(request,id=None):
  
  article_obj = None

  if id is not None:
   article_obj = Article.objects.get(id=id)
  
  
  context = {
    "object" : article_obj,
  }
  
  return render(request,"articles/detail.html",context=context)


#Don't forget to input LOGIN_URL going into settings.py(where ever you wanna take your user to)
## @login_required  
#def article_create_view(request):
  
  
  #form = ArticleForm()
  #context = {
    #"form" : form
  #}



  #if request.method == "POST":
    
    #form = ArticleForm(request.POST)

    #context['form'] = form
    
    #if form.is_valid():
      
      #title = form.cleaned_data.get("title")
      #content = form.cleaned_data.get("content")

      #article_object = Article.objects.create(title=title,content=content)
      
      ##context['created'] = True
    
  
  
  
  
  #return render(request,"articles/create.html",context=context)


## Newer version for optimization.
@login_required
def article_create_view(request):
  
  
  form = ArticleForm(request.POST or None)
  context = {
    "form" : form
  }
  print(form)



  
    
  if form.is_valid():
      
    #title = form.cleaned_data.get("title")
    #content = form.cleaned_data.get("content")

    article_object = form.save()
    context['object'] = article_object
    
    context['created'] = True
    
  
  
  
  
  return render(request,"articles/create.html",context=context)