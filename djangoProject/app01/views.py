from django.shortcuts import render, redirect
from app01 import models
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Student, Upload, Scholarship





def index(request):
    if request.method == 'POST':
        form = models.Login(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main_menu')
    else:
        form = models.Login()
    return render(request, 'user_signin.html', {'form': form})





def main_menu(request):
    return render(request, "buttons.html")


def teacher_evaluation(request):
    return render(request, "teacher_evaluation.html")

def submitproject(request):
    if request.method == 'POST':
        num_forms = int(request.POST.get('num_forms'))
        for i in range(num_forms):
            name = request.POST.get(f'name_{i}')
            student_id = request.POST.get(f'student_id_{i}')
            college = request.POST.get(f'college_{i}')
            student = Student(name=name, student_id=student_id, college=college)
            student.save()
        return HttpResponseRedirect('/submitproject/')
    else:
        return render(request, "submitproject.html")


def scholarship(request):
    if request.method == 'POST':
        average_points = request.POST.get('average_points')
        last_term_point = request.POST.get('last_term_point')
        now_point = request.POST.get('now_point')
        same_major_rank = request.POST.get('same_major_rank')
        number_students_same_major = request.POST.get('number_students_same_major')
        poor_student = request.POST.get('1.id')
        team_leader = request.POST.get('2.id')
        prize = request.POST.get('3.id')
        scholarship = Scholarship(average_points=average_points, last_term_point=last_term_point,
                                  now_point=now_point, same_major_rank=same_major_rank,
                                  number_students_same_major=number_students_same_major, poor_student=poor_student,
                                  team_leader=team_leader, prize=prize)
        if average_points < 3.5:
            print("很遗憾，您申请奖学金失败")
        scholarship.save()
        return HttpResponseRedirect('/scholarship_review/')
    else:
        return render(request, "scholarship_review.html")
