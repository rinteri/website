from django.contrib import admin
from .models import Advertisement

class AdvAdmin(admin.ModelAdmin):
    list_display =['id','title','description', 'price', 'created_date', 'update_date', 'auction', 'get_html_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true', 'make_image_as_false']
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Удалить изображение')
    def make_image_as_false(self, request, queryset):
        queryset.update(image=False)

admin.site.register(Advertisement, AdvAdmin)

