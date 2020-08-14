from django.contrib import admin

from .models import Category, Page

# Register your models here.

class PageInline(admin.TabularInline):
	model = Page
	extra = 10

class CategoryAdmin(admin.ModelAdmin):
	fieldsets=[
		('Name of category', {'fields': ['name'], 'classes':
			['collapse']}),
		('Number of likes',  {'fields': ['likes'],'classes': 
			['collapse']}),
		('Number of views',  {'fields': ['views'], 'classes':
			['collapse']}),
		]
	inlines = [PageInline]
	list_display = ('name', 'views', 'likes')
	list_filter = ['name']
	search_fields = ['name']
	

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
