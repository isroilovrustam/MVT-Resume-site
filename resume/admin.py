from django.contrib import admin
from .models import About, Blog, Category, Tag, Comment, Collection, Contact, Newslatter

# Register your models here.

admin.site.register(About)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Collection)
admin.site.register(Newslatter)
