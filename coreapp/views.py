from django.shortcuts import render, redirect
from .models import student


def form(request):
    if request.method == 'POST':
        student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            address=request.POST['address'],
            contact=request.POST['contact'],
            email=request.POST['email']
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
        student_obj.email = request.POST['email']
        student_obj.save()

        return redirect('home')
    return render(
        request,
        'coreapp/edit.html',
        {'data': student_obj}
    )


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