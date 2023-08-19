from django.contrib import admin
from .models import Advers
# Register your models here.
class AdversAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image_of_adv", "price", "is_auction", "created_date", "updated_date"]
    actions = [
        'make_au_as_true',
        'make_au_as_false'
    ]
    list_filter = ["is_auction", "created_at"]
    fieldsets = (
        ('Main', {'fields':('title', 'description', 'user', 'image'), 'classes':['collapse']}),
        ('Money', {'fields':('price', 'is_auction'), 'classes':['collapse']})
    )
    @admin.action(description="+auction")
    def make_au_as_true(self, request, queryset):
        queryset.update(is_auction=True)
    @admin.action(description="-auction")
    def make_au_as_false(self, request, queryset):
        queryset.update(is_auction=False) 

admin.site.register(Advers, AdversAdmin)