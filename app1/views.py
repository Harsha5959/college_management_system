from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django import forms
from django.db.models import Count

from .models import Department, HOD, Professor, Student


# ===============================
# HARD-CODED ADMIN (TEMP)
# ===============================
ADMIN_USERNAME = "Harsha"
ADMIN_PASSWORD = "12345"


# ===============================
# BASIC VIEWS
# ===============================

@login_required
def home(request):
    dept = Department.objects.all()

    dept_names = list(dept.values_list('name', flat=True))
    dept_students = [Student.objects.filter(department=d).count() for d in dept]

    context = {
        "department_count": dept.count(),
        "hod_count": HOD.objects.count(),
        "professor_count": Professor.objects.count(),
        "student_count": Student.objects.count(),
        "dept_names": dept_names,
        "dept_students": dept_students,
    }
    return render(request, "frontend_app1/home.html", context)


@login_required
def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'professor_count': Professor.objects.count(),
        'hod_count': HOD.objects.count(),
        'department_count': Department.objects.count(),
    }
    return render(request, 'frontend_app1/dashboard.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        auth_login(request, user)
        return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})


# ===============================
# FORMS
# ===============================
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


# ===============================
# ADMIN CHECK
# ===============================
def is_admin_valid(request):
    return (
        request.POST.get('username') == ADMIN_USERNAME and
        request.POST.get('password') == ADMIN_PASSWORD
    )


# ===============================
# LIST VIEWS (Pagination)
# ===============================
@login_required
def department_list(request):
    qs = Department.objects.all().order_by('id')
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    data = paginator.get_page(page)

    return render(request, 'frontend_app1/department_list.html', {'data': data})


@login_required
def hod_list(request):
    qs = HOD.objects.all().order_by('id')
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    data = paginator.get_page(page)

    return render(request, 'frontend_app1/hod_list.html', {'data': data})


@login_required
def professor_list(request):
    qs = Professor.objects.all().order_by('id')
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    data = paginator.get_page(page)

    return render(request, 'frontend_app1/professor_list.html', {'data': data})


@login_required
def student_list(request):
    search = request.GET.get('search', '')
    dept = request.GET.get('department', '')

    qs = Student.objects.all().order_by('id')

    if search:
        qs = qs.filter(name__icontains=search)

    if dept:
        qs = qs.filter(department__name=dept)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    data = paginator.get_page(page)

    return render(request, 'frontend_app1/student_list.html', {
        'data': data,
        'departments': Department.objects.all(),
        'search': search,
        'department_selected': dept,
    })


# ===============================
# ADD (NO ADMIN CHECK)
# ===============================
@login_required
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('department_list')
    return render(request, 'frontend_app1/add_department.html', {'form': form})


@login_required
def add_hod(request):
    form = HODForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hod_list')
    return render(request, 'frontend_app1/add_hod.html', {'form': form})


@login_required
def add_professor(request):
    form = ProfessorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('professor_list')
    return render(request, 'frontend_app1/add_professor.html', {'form': form})


@login_required
def add_student(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'frontend_app1/add_student.html', {'form': form})


# ===============================
# EDIT (ADMIN CHECK REQUIRED)
# ===============================
@login_required
def edit_department(request, id):
    obj = get_object_or_404(Department, id=id)
    form = DepartmentForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('department_list')
    return render(request, 'frontend_app1/add_department.html', {'form': form, 'edit': True})


@login_required
def edit_hod(request, id):
    obj = get_object_or_404(HOD, id=id)
    form = HODForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hod_list')
    return render(request, 'frontend_app1/add_hod.html', {'form': form, 'edit': True})


@login_required
def edit_professor(request, id):
    obj = get_object_or_404(Professor, id=id)
    form = ProfessorForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('professor_list')
    return render(request, 'frontend_app1/add_professor.html', {'form': form, 'edit': True})


@login_required
def edit_student(request, id):
    obj = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'frontend_app1/add_student.html', {'form': form, 'edit': True})


# ===============================
# CONFIRM EDIT (Admin Auth)
# ===============================
@login_required
def confirm_edit_department(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        return redirect('edit_department', id=id)
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_edit_hod(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        return redirect('edit_hod', id=id)
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_edit_professor(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        return redirect('edit_professor', id=id)
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_edit_student(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        return redirect('edit_student', id=id)
    return render(request, 'frontend_app1/admin_confirm.html')


# ===============================
# DELETE (Admin Auth)
# ===============================
@login_required
def confirm_delete_department(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        Department.objects.filter(id=id).delete()
        return redirect('department_list')
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_delete_hod(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        HOD.objects.filter(id=id).delete()
        return redirect('hod_list')
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_delete_professor(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        Professor.objects.filter(id=id).delete()
        return redirect('professor_list')
    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_delete_student(request, id):
    if request.method == 'POST' and is_admin_valid(request):
        Student.objects.filter(id=id).delete()
        return redirect('student_list')
    return render(request, 'frontend_app1/admin_confirm.html')
