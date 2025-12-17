from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Department, HOD, Professor, Student


# ============================
# TEMP ADMIN CREDENTIALS
# (TRIAL PROJECT ONLY)
# ============================
ADMIN_USERNAME = "Harsha"
ADMIN_PASSWORD = "12345"


# ============================
# BASIC VIEWS
# ============================

def home(request):
    return render(request, 'frontend_app1/home.html')


@login_required
def department_list(request):
    data = Department.objects.all()
    return render(request, 'frontend_app1/department_list.html', {'data': data})


@login_required
def hod_list(request):
    data = HOD.objects.all()
    return render(request, 'frontend_app1/hod_list.html', {'data': data})


@login_required
def professor_list(request):
    data = Professor.objects.all()
    return render(request, 'frontend_app1/professor_list.html', {'data': data})


@login_required
def student_list(request):
    data = Student.objects.all()
    return render(request, 'frontend_app1/student_list.html', {'data': data})


def user_logout(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


# ============================
# FORMS
# ============================

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class HODForm(forms.ModelForm):
    class Meta:
        model = HOD
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


# ============================
# ADMIN CHECK FUNCTION
# ============================

def is_admin_valid(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


# ============================
# ADD VIEWS
# ============================

@login_required
def add_department(request):
    if request.method == 'POST':
        if is_admin_valid(request):
            form = DepartmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('department_list')
        return render(request, 'frontend_app1/add_department.html', {
            'form': DepartmentForm(),
            'error': 'Invalid admin credentials'
        })

    return render(request, 'frontend_app1/add_department.html', {
        'form': DepartmentForm()
    })


@login_required
def add_hod(request):
    if request.method == 'POST':
        if is_admin_valid(request):
            form = HODForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('hod_list')
        return render(request, 'frontend_app1/add_hod.html', {
            'form': HODForm(),
            'error': 'Invalid admin credentials'
        })

    return render(request, 'frontend_app1/add_hod.html', {
        'form': HODForm()
    })


@login_required
def add_professor(request):
    if request.method == 'POST':
        if is_admin_valid(request):
            form = ProfessorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('professor_list')
        return render(request, 'frontend_app1/add_professor.html', {
            'form': ProfessorForm(),
            'error': 'Invalid admin credentials'
        })

    return render(request, 'frontend_app1/add_professor.html', {
        'form': ProfessorForm()
    })


@login_required
def add_student(request):
    if request.method == 'POST':
        if is_admin_valid(request):
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student_list')
        return render(request, 'frontend_app1/add_student.html', {
            'form': StudentForm(),
            'error': 'Invalid admin credentials'
        })

    return render(request, 'frontend_app1/add_student.html', {
        'form': StudentForm()
    })


# ============================
# EDIT VIEWS
# ============================

@login_required
def edit_department(request, id):
    obj = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=obj)

    return render(request, 'frontend_app1/edit_department.html', {'form': form})


@login_required
def edit_hod(request, id):
    obj = get_object_or_404(HOD, id=id)
    if request.method == 'POST':
        form = HODForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('hod_list')
    else:
        form = HODForm(instance=obj)

    return render(request, 'frontend_app1/edit_hod.html', {'form': form})


@login_required
def edit_professor(request, id):
    obj = get_object_or_404(Professor, id=id)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=obj)

    return render(request, 'frontend_app1/edit_professor.html', {'form': form})


@login_required
def edit_student(request, id):
    obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=obj)

    return render(request, 'frontend_app1/edit_student.html', {'form': form})


# ============================
# CONFIRM → EDIT / DELETE
# ============================

@login_required
def confirm_edit(request, redirect_url):
    if request.method == 'POST':
        if is_admin_valid(request):
            return redirect(redirect_url)
        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Invalid admin credentials'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_delete_department(request, id):
    if request.method == 'POST':
        if is_admin_valid(request):
            Department.objects.filter(id=id).delete()
            return redirect('department_list')
        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Invalid admin credentials'
        })
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_delete_hod(request, id):
    if request.method == 'POST':
        if is_admin_valid(request):
            HOD.objects.filter(id=id).delete()
            return redirect('hod_list')
        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Invalid admin credentials'
        })
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_delete_professor(request, id):
    if request.method == 'POST':
        if is_admin_valid(request):
            Professor.objects.filter(id=id).delete()
            return redirect('professor_list')
        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Invalid admin credentials'
        })
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_delete_student(request, id):
    if request.method == 'POST':
        if is_admin_valid(request):
            Student.objects.filter(id=id).delete()
            return redirect('student_list')
        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Invalid admin credentials'
        })
    return render(request, 'frontend_app1/admin_confirm.html')
