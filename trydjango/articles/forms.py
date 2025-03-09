from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ['title','content']

  def clean(self):
    
    data = self.cleaned_data
    title = data.get("title")
    qs = Article.objects.filter(title__icontains=title)

    if qs.exists():
      self.add_error("title",f"{title} is already in use. Try another name.")

    return data





class ArticleFormOld(forms.Form):
  title = forms.CharField()
  content = forms.CharField()

  # Name can't change of these functions, clean_"" jisse bhi clean karna hai wo.
  #def clean_title(self):   
    #cleaned_data = self.cleaned_data
    #title = cleaned_data.get("title")

    #if title.lower().strip() == "the office":
      #raise forms.ValidationError('This title is taken.')

    #return title
  
  def clean(self):
    cleaned_data = self.cleaned_data
    title = cleaned_data.get("title")
    content = cleaned_data.get("content")

    if title.lower().strip() == "the office":
      self.add_error('title','Bro,This title is taken')
      #raise forms.ValidationError('This title is taken.')

    if "office" in content:
      self.add_error("content","office can't be in content.")

    return cleaned_data