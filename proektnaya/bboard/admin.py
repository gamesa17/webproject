from django.contrib import admin


from .models import BBoard
from .models import Rubric


class BBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubic')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(BBoard, BBoardAdmin)
admin.site.register(Rubric)