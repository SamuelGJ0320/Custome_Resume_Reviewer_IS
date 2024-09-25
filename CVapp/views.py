from django.shortcuts import render

def custom_resume_view(request):
    return render(request, 'CVapp/custome_resume.html')