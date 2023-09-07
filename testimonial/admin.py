from django.contrib import admin
from .models import Profession, Testimonial

# Register your models here.
class ProfessionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Profession, ProfessionAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('content', 'author')
    search_fields=('content', 'author__username','profesiones__name')
    list_filter=('author__username','profesiones__name')
admin.site.register(Testimonial, TestimonialAdmin)

