from django.contrib import admin
from ssms.models import Grub,Grub_Coord,Grub_Student,Veg,NonVeg,Both,Student,Wear,Event,Wear_Student,Event_Student,DateMailStatus
admin.site.register(Grub)
admin.site.register(Grub_Coord)

admin.site.register(Veg)
admin.site.register(NonVeg)
admin.site.register(Both)

admin.site.register(Wear)
admin.site.register(DateMailStatus)
admin.site.register(Event)

class GrubStudentAdmin(admin.ModelAdmin):
    search_fields = ('student_id',)
admin.site.register(Grub_Student,GrubStudentAdmin)
admin.site.register(Wear_Student,GrubStudentAdmin)
admin.site.register(Event_Student,GrubStudentAdmin)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('bits_id',)
admin.site.register(Student,StudentAdmin)
