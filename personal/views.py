from django.shortcuts import render
from personal.models import Question
# Create your views here.

def home_screen_view(request):
	context = {}
	# context['some_string'] = "this is some string that I am passing to the view"
	# context['some_number'] = 231


	# context= { 'some_string': "this is some string that I am passing to the view"}

	# list_of_values=[]
	# list_of_values.append("First entry")
	# list_of_values.append("Second entry")
	# list_of_values.append("Third entry")
	# list_of_values.append("Fourth entry")
	# context['list_of_values'] = list_of_values;

	questions = Question.objects.all()
	context['questions'] = questions
	return render(request, "personal/home.html", context)