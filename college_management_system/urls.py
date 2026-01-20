from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app1 import views

urlpatterns = [

    # ADMIN + DASHBOARD
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),

    # AUTHENTICATION
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    # LISTS (Tables + Search + Filters)
    path('departments/', views.department_list, name='department_list'),
    path('hods/', views.hod_list, name='hod_list'),
    path('professors/', views.professor_list, name='professor_list'),
    path('students/', views.student_list, name='student_list'),

    # ADD
    path('add-department/', views.add_department, name='add_department'),
    path('add-hod/', views.add_hod, name='add_hod'),
    path('add-professor/', views.add_professor, name='add_professor'),
    path('add-student/', views.add_student, name='add_student'),

    # CONFIRM EDIT (Authorization Screens)
    path('confirm-edit-department/<int:id>/', views.confirm_edit_department, name='confirm_edit_department'),
    path('confirm-edit-hod/<int:id>/', views.confirm_edit_hod, name='confirm_edit_hod'),
    path('confirm-edit-professor/<int:id>/', views.confirm_edit_professor, name='confirm_edit_professor'),
    path('confirm-edit-student/<int:id>/', views.confirm_edit_student, name='confirm_edit_student'),

    # EDIT (Forms)
    path('edit-department/<int:id>/', views.edit_department, name='edit_department'),
    path('edit-hod/<int:id>/', views.edit_hod, name='edit_hod'),
    path('edit-professor/<int:id>/', views.edit_professor, name='edit_professor'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),

    # DELETE (Confirmation)
    path('delete-department/<int:id>/', views.confirm_delete_department, name='delete_department'),
    path('delete-hod/<int:id>/', views.confirm_delete_hod, name='delete_hod'),
    path('delete-professor/<int:id>/', views.confirm_delete_professor, name='delete_professor'),
    path('delete-student/<int:id>/', views.confirm_delete_student, name='delete_student'),
]
