from django.contrib import admin
from rate.models import *
# Register your models here.

class ProfessorAdmin(admin.ModelAdmin):
	fields = ["name","college"]
	search_fields = ['name']

class FactorRatingInline(admin.TabularInline):
    model = FactorRating
    extra = 7

class RatingAdmin(admin.ModelAdmin):
	fieldsets = [(None,{'fields': ['time','account','course','professor']})]
	list_display = ('time', 'account', 'course','professor')
	inlines = [FactorRatingInline]
	list_filter = ['time']

class AccountAdmin(admin.ModelAdmin):
	search_fields = ['name']
	fieldsets = [
		('Basic Information', {'fields':['name', 'email', 'isVerified']}),
	]

class ClassAdmin(admin.ModelAdmin):
	list_diplay = ('term','course','professor')

admin.site.register(Professor)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Course)
admin.site.register(Class,ClassAdmin)
admin.site.register(Factor)