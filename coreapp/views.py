from django.shortcuts import render, redirect
from .models import student
import nepali_datetime


# -----------------------------
# BS -> AD Converter
# -----------------------------
def bs_to_ad(bs_date):
    if not bs_date:
        return None
    try:
        y, m, d = map(int, bs_date.split('-'))
        return nepali_datetime.date(y, m, d).to_datetime_date()
    except:
        return None


# -----------------------------
# CREATE (FORM + POST same function)
# -----------------------------
def form(request):

    if request.method == 'POST':
        student.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            address=request.POST.get('address'),
            contact=request.POST.get('contact'),
            DOB=bs_to_ad(request.POST.get('bs_date')),
            email=request.POST.get('email'),
            image=request.FILES.get('image'),
            video=request.FILES.get('video'),
            pdf=request.FILES.get('pdf')
        )

        return redirect('home')

    # same function used for form display (GET implicit)
    return render(request, 'coreapp/form.html')


# -----------------------------
# READ
# -----------------------------
def home(request):
    data = student.objects.filter(is_deleted=False)
    return render(request, 'coreapp/home.html', {'data': data})


# -----------------------------
# UPDATE
# -----------------------------
def edit(request, id):

    student_obj = student.objects.get(id=id)

    if request.method == 'POST':

        student_obj.name = request.POST.get('name')
        student_obj.age = request.POST.get('age')
        student_obj.address = request.POST.get('address')
        student_obj.contact = request.POST.get('contact')
        student_obj.email = request.POST.get('email')

        student_obj.DOB = bs_to_ad(request.POST.get('bs_date'))

        if request.FILES.get('image'):
            student_obj.image = request.FILES.get('image')

        if request.FILES.get('video'):
            student_obj.video = request.FILES.get('video')

        if request.FILES.get('pdf'):
            student_obj.pdf = request.FILES.get('pdf')

        student_obj.save()

        return redirect('home')

    return render(request, 'coreapp/edit.html', {'data': student_obj})


# -----------------------------
# SOFT DELETE
# -----------------------------
def delete(request, id):

    obj = student.objects.get(id=id)
    obj.is_deleted = True
    obj.save()

    return redirect('home')


# -----------------------------
# RECYCLE BIN
# -----------------------------
def recycle(request):
    data = student.objects.filter(is_deleted=True)
    return render(request, 'coreapp/recycle.html', {'data': data})


# -----------------------------
# RESTORE
# -----------------------------
def restore(request, id):

    obj = student.objects.get(id=id)
    obj.is_deleted = False
    obj.save()

    return redirect('recycle')


# -----------------------------
# PERMANENT DELETE
# -----------------------------
def permanent_delete(request, id):

    obj = student.objects.get(id=id)
    obj.delete()

    return redirect('recycle')