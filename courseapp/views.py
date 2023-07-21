from django.shortcuts import render,redirect
from courseapp.models import Course
from courseapp.models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')
def add_course(request):
    render(request,'course.html')
def add_coursedb(request):
    if request.method=='POST':
        course_name=request.POST.get('course_name')
        course_fee=request.POST.get('course_fee')
        course=Course(course_name=course_name,course_fee=course_fee)
        course.save()
        return redirect('/')
def add_student(request):
    course=Course.objects.all()
    return render(request,'student.html',{'course':course})
def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['student_name']
        print(student_name)
        student_address=request.POST['student_address']
        print(student_address)
        student_age=request.POST['student_age']
        print(student_age)
        joining_date=request.POST['joining_date']
        print(joining_date)
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=Student(student_name=student_name,student_address=student_address,student_age=student_age,joining_date=joining_date,course=course1)
        student.save()
        return redirect('add_student')

def show_student_details(request):
    student=Student.objects.all()
    return render(request,'showstudent.html',{'student':student})


def edit(request,pk):
    student=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'edit.html',{'student':student,'course':course})

def editdb(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['student_name']
        student.student_address=request.POST['student_address']
        student.student_age=request.POST['student_age']
        student.joining_date=request.POST['joining_date']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student.course=course1
        student.save()
        return redirect('show_student_details') 
    return render(request,'edit.html')   
    
 
def delete(request,pk):
    d=Student.objects.get(id=pk)
    d.delete()
    return redirect('show_student_details')
    