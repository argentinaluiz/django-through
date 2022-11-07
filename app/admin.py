from django.contrib import admin
from app.models import Course, Enrollment
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    fields= ['name']

    # link

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)