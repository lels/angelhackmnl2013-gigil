from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from angel.models import Student

def index(request):
  return render_to_response('angel/index.html', {"list_students" : Student.objects.order_by('amount_needed')[0:3]})

def detail(request, student_id):
  return render_to_response('angel/profile.html', {"student" : \
      Student.objects.filter(pk=student_id)[0]})

def donate(request, student_id):
  return HttpResponse("You're donating on student %s." % student_id)
  
def search(request):
  search = request.REQUEST['search']
  return render_to_response('angel/search.html', {"list_students": Student.objects.filter(Q(first_name__icontains=search)|Q(middle_name__icontains=search)|Q(last_name__icontains=search)).order_by('amount_needed')})
