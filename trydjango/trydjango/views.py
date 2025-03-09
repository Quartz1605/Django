"""
To render html webpages

"""

HTML_STRING = """ <h1>Hello World</h1> """



from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string

def home(request,*args,**kwargs):
  """
  Take in a request
  Return HTML as a response(We pick to return the response)

  
  """
  
  
  article_obj = Article.objects.get(id=1)
  
  ##this actually returns a queryset
  articles_list = Article.objects.all()


  my_list = articles_list
  

  context = {
    "title" : article_obj.title,
    "id" : article_obj.id,
    "content" : article_obj.content,
    "my_list" : my_list,
  }

  ##Django template basics
  ##first way of doing this is:
  
  ## Html_string = "<h1>Title is {title} and its content is {content}.</h1>".format(**context)

  ##Second way is render_to_string
  Html_string = render_to_string("home-view.html",context=context)

  return HttpResponse(Html_string)

