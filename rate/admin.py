from django.contrib import admin
from rate.models import *
# Register your models here.

class ProfessorAdmin(admin.ModelAdmin):
	fields = ["name","college"]
	search_fields = ['name']

admin.site.register(Professor)

class FactorRatingInline(admin.StackedInline):
    model = FactorRating
    extra = 7

class RatingAdmin(admin.ModelAdmin):
	fieldsets = [(None,{'fields': ['time','account','course','professor']})]
	list_display = ('time', 'account', 'course','professor')
	inlines = [FactorRatingInline]
	list_filter = ['time']

admin.site.register(Rating, RatingAdmin)

class AccountAdmin(admin.ModelAdmin):
	search_fields = ['name']
	fieldsets = [
		('Basic Information', {'fields':['name', 'email', 'isVerified']}),
	]

admin.site.register(Account,AccountAdmin)

class ClassAdmin(admin.ModelAdmin):
	list_diplay = ('term','course','professor')

admin.site.register(Class,ClassAdmin)

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Factor)