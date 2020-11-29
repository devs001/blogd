from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Artical_m

class LastestArticalFeed(Feed):
    title="articals"
    link = reverse_lazy("show_articals")
    description_template = "new articals"

    def items(self):
        return Artical_m.posted.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
         return truncatewords(item.body, 30)