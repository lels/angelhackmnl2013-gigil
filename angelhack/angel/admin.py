from django.contrib import admin
from django import forms
from angel.models import YesNo, \
                         Student, \
                         Gender, \
                         NeedItem, \
                         YearLevel, \
                         Story, \
                         Donator, \
                         Donation

class StoryTextForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea);
    
    class Meta:
        model = Student

class Story_Admin(admin.ModelAdmin):
    form = StoryTextForm

admin.site.register(YesNo)
admin.site.register(Student)
admin.site.register(Gender)
admin.site.register(NeedItem)
admin.site.register(YearLevel)
admin.site.register(Story,Story_Admin)
admin.site.register(Donator)
admin.site.register(Donation)
