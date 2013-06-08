from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
  return render_to_response('angel/index.html', {})

def detail(request, student_id):
  return render_to_response('angel/profile.html', {})

def donate(request, student_id):
  return HttpResponse("You're donating on student %s." % student_id)
