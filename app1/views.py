from django.shortcuts import render
from app1.models import Department, HOD, Professor, Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django import forms




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
    logout(request)          # this clears the session
    return redirect('home')  # go back to home page


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()            # create the user
            auth_login(request, user)     # log the user in immediately
            return redirect('home')       # go to home page
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def confirm_delete_student(request, id):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        admin_user = authenticate(request, username=username, password=password)

        if admin_user and admin_user.is_superuser:
            student = get_object_or_404(Student, id=id)
            student.delete()
            return redirect('student_list')

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials are allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_edit_student(request, id):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            return redirect('edit_student', id=id)

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials are allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'frontend_app1/edit_student.html', {'form': form})


@login_required
def confirm_delete_department(request, id):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            Department.objects.filter(id=id).delete()
            return redirect('department_list')

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_edit_department(request, id):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            return redirect('edit_department', id=id)

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


@login_required
def edit_department(request, id):
    dept = get_object_or_404(Department, id=id)

    form = DepartmentForm(request.POST or None, instance=dept)
    if form.is_valid():
        form.save()
        return redirect('department_list')

    return render(request, 'frontend_app1/edit_department.html', {'form': form})


@login_required
def confirm_delete_hod(request, id):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            HOD.objects.filter(id=id).delete()
            return redirect('hod_list')

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_edit_hod(request, id):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            return redirect('edit_hod', id=id)

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


class HODForm(forms.ModelForm):
    class Meta:
        model = HOD
        fields = '__all__'


@login_required
def edit_hod(request, id):
    hod = get_object_or_404(HOD, id=id)

    form = HODForm(request.POST or None, instance=hod)
    if form.is_valid():
        form.save()
        return redirect('hod_list')

    return render(request, 'frontend_app1/edit_hod.html', {'form': form})



@login_required
def confirm_delete_professor(request, id):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            Professor.objects.filter(id=id).delete()
            return redirect('professor_list')

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


@login_required
def confirm_edit_professor(request, id):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            return redirect('edit_professor', id=id)

        return render(request, 'frontend_app1/admin_confirm.html', {
            'error': 'Only ADMIN credentials allowed'
        })

    return render(request, 'frontend_app1/admin_confirm.html')


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


@login_required
def edit_professor(request, id):
    prof = get_object_or_404(Professor, id=id)

    form = ProfessorForm(request.POST or None, instance=prof)
    if form.is_valid():
        form.save()
        return redirect('professor_list')

    return render(request, 'frontend_app1/edit_professor.html', {'form': form})


@login_required
def add_department(request):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            form = DepartmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('department_list')

        return render(request, 'frontend_app1/add_department.html', {
            'error': 'Only ADMIN can add department'
        })

    form = DepartmentForm()
    return render(request, 'frontend_app1/add_department.html', {'form': form})


@login_required
def add_hod(request):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            form = HODForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('hod_list')

        return render(request, 'frontend_app1/add_hod.html', {
            'error': 'Only ADMIN can add HOD'
        })

    form = HODForm()
    return render(request, 'frontend_app1/add_hod.html', {'form': form})


@login_required
def add_professor(request):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            form = ProfessorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('professor_list')

        return render(request, 'frontend_app1/add_professor.html', {
            'error': 'Only ADMIN can add Professor'
        })

    form = ProfessorForm()
    return render(request, 'frontend_app1/add_professor.html', {'form': form})



@login_required
def add_student(request):
    if request.method == 'POST':
        admin_user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if admin_user and admin_user.is_superuser:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student_list')

        return render(request, 'frontend_app1/add_student.html', {
            'error': 'Only ADMIN can add Student'
        })

    form = StudentForm()
    return render(request, 'frontend_app1/add_student.html', {'form': form})
