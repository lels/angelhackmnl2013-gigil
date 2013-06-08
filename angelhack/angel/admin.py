from django.contrib import admin
from angel.models import YesNo, \
                         Student, \
                         Gender, \
                         YearLevel, \
                         Story, \
                         Donator, \
                         Donation

admin.site.register(YesNo)
admin.site.register(Student)
admin.site.register(Gender)
admin.site.register(YearLevel)
admin.site.register(Story)
admin.site.register(Donator)
admin.site.register(Donation)
