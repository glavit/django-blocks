# -*- coding: utf-8 -*
from django.contrib import admin
from blocks.models import Block
from blocks.models import URL


class BlockAdmin(admin.ModelAdmin):
	list_display = ['name', 'place', 'order', 'public']
	search_fields = ['name', 'place', 'order', 'public']
	list_filter = ['place', 'sites', 'urls', 'public']
	list_editable = ['public', 'order']

admin.site.register(Block, BlockAdmin)


class URLAdmin(admin.ModelAdmin):
	list_display = ['name', 'url', 'regex', 'created_at', 'updated_at']
	search_fields = ['name', 'url', 'regex', 'created_at', 'updated_at']
	list_filter = ['regex']
	list_editable = ['regex']

admin.site.register(URL, URLAdmin)