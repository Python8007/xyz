from django.contrib import admin
from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','ephno','eadd']

    def get_ordering(self, request):
        return [('eno')]
admin.site.register(Employee,EmployeeAdmin)