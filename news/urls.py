from django.urls import path
from .views import (MainView, CategoryFilterView, DetailNewView, 
                    TagFilterView, AdsView, AboutView, TeamView,
                     CommentView )
urlpatterns = [
    path("", MainView.as_view(), name='index'),
    path("category/<int:id>", CategoryFilterView.as_view(), name='categoryfilter'),
    path("tag/<int:id>", TagFilterView.as_view(), name='tagfilter'),
    path("detail/<int:id>", DetailNewView.as_view(), name='detailpage'),
    path('reklama/', AdsView.as_view(), name='reklama'),
    path('aboutus/', AboutView.as_view(), name='aboutus'),
    path('team/', TeamView.as_view(), name='team'),
    path('comment/', CommentView.as_view(), name='comment')
]
