from django.contrib import admin
from angel.models import YesNo, \
                         Student, \
                         Gender, \
                         YearLevel, \
                         SuccessStory, \
                         Donator, \
                         Donation

admin.site.register(YesNo)
admin.site.register(Student)
admin.site.register(Gender)
admin.site.register(YearLevel)
admin.site.register(SuccessStory)
admin.site.register(Donator)
admin.site.register(Donation)
