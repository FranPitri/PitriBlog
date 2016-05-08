from django.contrib import admin
from main.models import Author,Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('content',)
    list_filter = ('author','date')
    list_display = ('title', 'author', 'date')

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('user',)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ('author',)
    list_display = ('author','post','date')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
