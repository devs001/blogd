from django.contrib.sitemaps import Sitemap
from .models import Artical_m

class Artical_sitemap(Sitemap):
    changefeq="weekly"
    priority=0.9
    def items(self):
        return Artical_m.posted.all()
    def lastmod(selfself,obj):
        return obj.update_date

