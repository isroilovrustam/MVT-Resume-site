from django.contrib import admin
from .models import About, Blog, Category, Tag, Comment, Collection, Contact, Newslatter


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category', 'create_date')
    search_fields = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone')
    list_filter = ('create_date',)


admin.site.register(About)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)

admin.site.register(Collection)
admin.site.register(Newslatter)
