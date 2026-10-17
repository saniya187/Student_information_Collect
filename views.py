from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def home(request):
    return render(request,'index.html')

# Create: add new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form= StudentForm()
    
    return render(request,'student/student_form.html',{'form':form,'title':"Add Student"})
#Get:Display all student from database
def student_list(request):
    students=Student.objects.all().order_by("id")
    return render(request,'student/student_list.html',{'students':students})
    
