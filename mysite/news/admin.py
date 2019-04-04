from django.contrib import admin

from .models import Reporter, Article

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 3
    
class ReporterAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    list_filter = ['full_name']
    search_fields = ['full_name']
    
admin.site.register(Reporter, ReporterAdmin)
