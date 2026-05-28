from django.shortcuts import render, redirect
from .models import student


def form(request):
    if request.method == 'POST' and request.FILES:
        student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            address=request.POST['address'],
            contact=request.POST['contact'],
            DOB = request.POST['DOB'],
            email=request.POST['email'],
            image=request.FILES['image'],
            video=request.FILES['video'],
            pdf=request.FILES['pdf']

        )
        return redirect('home')

    return render(request, 'coreapp/form.html')


def home(request):
    students = student.objects.filter(is_deleted=False)
    return render(request, 'coreapp/home.html', {'data': students})


def edit(request, id):
    student_obj = student.objects.get(id=id)

    if request.method == 'POST':
        student_obj.name = request.POST['name']
        student_obj.age = request.POST['age']
        student_obj.address = request.POST['address']
        student_obj.contact = request.POST['contact']
        student_obj.DOB = request.POST['DOB']
        student_obj.email = request.POST['email']

        if 'image' in request.FILES:
            student_obj.image = request.FILES['image']

        if 'video' in request.FILES:
            student_obj.video = request.FILES['video']

        if 'pdf' in request.FILES:
            student_obj.pdf = request.FILES['pdf']

        student_obj.save()

        return redirect('home')

    return render(request, 'coreapp/edit.html', {'data': student_obj})


def delete(request, id):
    student_obj = student.objects.get(id=id)

    student_obj.is_deleted = True
    student_obj.save()
    return redirect('home')


def recycle(request):
    recycle_data = student.objects.filter(is_deleted=True)
    return render(request, 'coreapp/recycle.html', {'data': recycle_data})


def restore(request, id):
    student_obj = student.objects.get(id=id)
    student_obj.is_deleted = False
    student_obj.save()

    return redirect('recycle')

def permanent_delete(request, id):
    student_obj = student.objects.get(id=id)
    student_obj.delete()  

    return redirect('recycle')