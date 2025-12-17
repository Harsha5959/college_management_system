from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from app1.views import (
    home,
    department_list,
    hod_list,
    professor_list,
    student_list,
    user_logout,
    signup,
    confirm_delete_student,
    confirm_edit_student,
    edit_student,
    confirm_delete_department,
    confirm_edit_department,
    edit_department,
    confirm_delete_hod,
    confirm_edit_hod,
    edit_hod,
    confirm_delete_professor,
    confirm_edit_professor,
    edit_professor,
    add_department,
    add_hod,
    add_professor,
    add_student,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('department_list/', department_list, name='department_list'),
    path('hod_list/', hod_list, name='hod_list'),
    path('professor_list/', professor_list, name='professor_list'),
    path('student_list/', student_list, name='student_list'),

    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('logout/', user_logout, name='logout'),
    path('signup/', signup, name='signup'),

    # ---- STUDENT ----
    path('confirm-delete-student/<int:id>/', confirm_delete_student, name='confirm_delete_student'),
    path('confirm-edit-student/<int:id>/', confirm_edit_student, name='confirm_edit_student'),
    path('edit-student/<int:id>/', edit_student, name='edit_student'),

    # ---- DEPARTMENT ----
    path('confirm-delete-department/<int:id>/', confirm_delete_department, name='confirm_delete_department'),
    path('confirm-edit-department/<int:id>/', confirm_edit_department, name='confirm_edit_department'),
    path('edit-department/<int:id>/', edit_department, name='edit_department'),

    # ---- HOD ----
    path('confirm-delete-hod/<int:id>/', confirm_delete_hod, name='confirm_delete_hod'),
    path('confirm-edit-hod/<int:id>/', confirm_edit_hod, name='confirm_edit_hod'),
    path('edit-hod/<int:id>/', edit_hod, name='edit_hod'),

    # ---- PROFESSOR ----
    path('confirm-delete-professor/<int:id>/', confirm_delete_professor, name='confirm_delete_professor'),
    path('confirm-edit-professor/<int:id>/', confirm_edit_professor, name='confirm_edit_professor'),
    path('edit-professor/<int:id>/', edit_professor, name='edit_professor'),

    path('add-department/', add_department, name='add_department'),
    path('add-hod/', add_hod, name='add_hod'),
    path('add-professor/', add_professor, name='add_professor'),
    path('add-student/', add_student, name='add_student'),

]
