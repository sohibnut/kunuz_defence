from .models import Category, Social

def contextBase(request):
    categories = Category.objects.all()
    socials = Social.objects.all()
    context = {
        'categories' : categories,
        'socials' : socials,
    }
    return context