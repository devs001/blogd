from django.urls import path
from . import views
from  .views import artical_in
from django.conf.urls.static import static
from django.conf import settings
from .feeds import LastestArticalFeed
print("gfguyggyuguyg")
urlpatterns = [
    path('', views.first , name='first'),
    path('heade', views.heade, name='heade'),
    path('create_head', views.create_head, name='create_head'),
    path('show_headin',views.show_heading, name='show_headin'),
    path('show_contents/<int:head_id>',
         views.show_contents,name='show_contents'),
    path('create_contents/<int:head_id>',
         views.create_contents,name='create_contents'),
    path('create_artical',views.create_artical,name='create_artical'),
    path('show_articals', views.show_articals, name='show_articals'),
    path('dashbroad', views.Dashbroad, name='dashbroad'),
    path('show_drafts', views.show_drafts, name='show_drafts'),
    path('delete_artical/<str:slug>',
         views.delete_artical, name='delete_artical'),
    path('edits_artical/<str:slug>',views.edits_artical,name='edits_artical'),
    path('artical_m/liked',views.liked,name='artical_m/liked'),
    path('artical_m/<str:slug>/',views.artical_in,name='artical_m'),
    path('commentsform/<int:id>',
         views.comments_V,name='commentsform'),
    path('commentsshow/<int:id>',
         views.CommentsList.as_view(),name='commentssho'),
    path('tags/<str:slug>',
         views.tags.as_view(),name='tags'),
    path('email_share/<int:id>', views.Email_Share_V, name='email_share'),
    path('categoryadd',views.Category_add.as_view(),name='categoryadd'),
    path('serach',views.Search.as_view(),name='serach'),
                  path('feed/', LastestArticalFeed, name='post_feed')
              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

