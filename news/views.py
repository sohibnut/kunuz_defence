from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Category, New, Social, Tag, AboutUs, Team
from .forms import CommentForm
# Create your views here.

class MainView(View):
    def get(self, request):
        latest_news = New.objects.all().order_by('-create_at')[:10]
        top_news = New.objects.all().order_by('-view_count')[:10]
        context = {
            'latest_news' : latest_news,
            'top_news' : top_news,
        }
        return render(request, template_name='index.html', context=context)


class CategoryFilterView(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        news = category.category_news.filter(type='news').order_by("-create_at")[:20]
        # news = New.objects.filter(category=id)
        context = {
            'news' : news,
            'category_name' : category.name,

        }
        return render(request, template_name='category_news.html', context=context)

class DetailNewView(View):
    def get(self, request, id):
        new = New.objects.get(id=id)
        new.view_count += 1
        new.save()
        category = new.category
        recommendation = category.category_news.filter(type='news').exclude(id=new.id).order_by('-view_count')[:5]
        last = category.category_news.filter(type='news').exclude(id=new.id).order_by('-create_at')[:5]
        context = {
            'recommendation' : recommendation,
            'last_news' : last,
            'new' : new
        }
        return render(request, template_name='detail_page.html', context=context)
    

class TagFilterView(View):
    def get(self, request, id):
        tag = Tag.objects.get(id=id)
        news = tag.tag_news.filter(type='news').order_by("-create_at")[:25]
        context = {
            'tag_name' : tag.name,
            'news' : news,
        }
        return render(request=request, context=context, template_name='tag_news.html')


class AdsView(View):
    def get(self, request):
        ads = New.objects.filter(type='ads').order_by('-create_at')
        context = {
            'ads' : ads,
        }
        return render(request=request, context=context, template_name='ads.html')
    
class AboutView(View):
    def get(self, request):
        about = AboutUs.objects.all().order_by('create_at').last()
        form = CommentForm()
        context = {
            'about' : about,
            'form' : form,
        }
        return render(request=request, context=context, template_name='about.html')

class TeamView(View):
    def get(self, request):
        persons = Team.objects.all()
        context = {
            'persons' : persons
        }
        return render(request, template_name='team.html', context=context)
    
class CommentView(View):
    def post(self, request):
        print('ishlayapti')
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='aboutus')