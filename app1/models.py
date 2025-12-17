from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class HOD(models.Model):
    department = models.OneToOneField(Department,on_delete=models.CASCADE,related_name='hod')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"HOD: {self.name} ({self.department.code})"


class Professor(models.Model):
    hod = models.ForeignKey(HOD,on_delete=models.CASCADE,related_name='professors')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Prof. {self.name} (HOD: {self.hod.name})"


class Student(models.Model):
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,related_name='students')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

