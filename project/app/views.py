from django.shortcuts import render,HttpResponse
from .models import Student
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("you are in the app view")


def search_students(request):
    query = request.GET.get('term', '')  # Get the input from the search bar
    students = Student.objects.filter(name__istartswith=query)  # Filter by names starting with the input
    results = list(students.values('name'))  # Convert QuerySet to a list of dictionaries
    return JsonResponse(results, safe=False)  # Return the results as JSON




def search_page(request):
    return render(request, 'app/search.html')

