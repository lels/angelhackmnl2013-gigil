from django.http import HttpResponse
from django.shortcuts import render_to_response
from angel.models import Student

def index(request):
  return render_to_response('angel/index.html', {"list_students" : Student.objects.order_by('amount_needed')[0:3]})

def detail(request, student_id):
  return render_to_response('angel/profile.html', {})

def donate(request, student_id):
  return HttpResponse("You're donating on student %s." % student_id)
