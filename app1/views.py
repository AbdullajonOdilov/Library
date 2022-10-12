from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def sinashga(request):
    return  HttpResponse("Hello user!")

def bosh_sahifa(request):
    return render(request, 'asosiy.html')

def mashq(request):
    data = {
        'ism': 'Tim'
    }
    return render(request,'mashq.html',data)

def bitiruvchi_student(request):
    data = {
        'bitiruvchilar':Student.objects.filter(birituvchi = True)
    }
    return render(request, 'mashq/bitiruvchi.html', data)

def book(request,son):
    data = {
        'kitob':Kitob.objects.get(id = son)
    }
    return render(request,'mashq/kitobs.html',data)

def talaba(request,son):
    data = {
        "student":Student.objects.get(id = son)
    }
    return render(request,'mashq/student.html',data)




def info(request,num):
    data = {
        "recordlar":Record.objects.get(id = num)
    }
    return render(request,'mashq/records.html',data)

def b_s_r(request):
    data ={
        'bitiruchilar_r':Record.objects.filter(student__birituvchi = True)
    }
    return render(request,'mashq/bitiruvchilar.html',data)

def tiriklar(request):
    data = {
        "tiriklar":Muallif.objects.filter(tirik=True)
    }
    return render(request,'mashq/life.html',data)

def eng_katta(request):
    data = {
        'sahifas': Kitob.objects.order_by('-sahifa')[:3]
    }
    return render(request,'mashq/kitob3.html',data)

def olingan_sana(request):
    data = {
        'sana': Record.objects.order_by('-olingan_sana')[:3]
    }
    return render(request,'mashq/sana.html',data)

def t_m_k(request):
    data = {
        'kitoblar': Kitob.objects.filter(muallif__tirik = True)
    }
    return render(request,'mashq/t_m_kitob.html',data)

def badiiy(request):
    data = {
        'badiiys':Kitob.objects.filter(janr = 'badiiy')
    }
    return render(request,'mashq/badiiy.html',data)
def a_s(request):
    data ={
        'students':Student.objects.filter(ism__contains = 'a')
    }
    return render(request,'mashq/a.html',data)

def qari(request):
    data = {
        'kattalar':Muallif.objects.order_by('t_y')[:3]

    }
    return render(request,'mashq/katta.html',data)

def erkak(request):
    data ={
        'male':Student.objects.all()
    }
    return render(request, 'mashq/student.html',data)

def kam(request):
    data = {
        'kam_k': Muallif.objects.filter(kitob_soni__lt = 10)

    }
    return render(request,"mashq/onta.html",data)

def eng_kop(request):
    data = {
        'kop':Muallif.objects.order_by('-kitob_soni')[:3]
    }
    return render(request,'mashq/kopk.html',data)

def all_student(request):
    if request.method == 'POST':
        f = StudentForm(request.POST)
        if f.is_valid():

            Student.objects.create(
                ism = f.cleaned_data.get('i'),
                kitob_soni= f.cleaned_data.get('kitoblari_soni'),
                birituvchi = f.cleaned_data.get('bitiruvchi')
            )
        return redirect('/student/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()

    else:
        s = Student.objects.filter(ism__contains = soz)

    data = {
        'studentlar':s,
        'forma':StudentForm
    }
    return render(request,'students.html',data)

def student_ochir(request,son):

    Student.objects.get(id=son).delete()
    return redirect('/student/')

def all_techers(request):
    if request.method == 'POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/ustoz/')

    data = {
        "ustoz":Muallif.objects.all(),
        'forma':MuallifForm
    }
    return  render(request,'mashq/muallif.html',data)

def teacher(request,num):
    data = {
        "mualliflar":Muallif.objects.get(id = num)
    }
    return render(request,'mashq/mualliflar.html',data)

def kitobxon(request):
    if request.method == 'POST':
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()

        return redirect('/kitob/')
    data = {
        'mualliflar':Muallif.objects.all(),
        'book':Kitob.objects.all(),
        'forma':KitobForm
    }
    return render(request, 'mashq/kitob.html', data)

def kitob_ochir(request,son):
    Kitob.objects.get(id=son).delete()
    return redirect('/kitob/')

# editing
def student_edit(request,son):
    if request.method == 'POST':
        if request.POST.get('bitiradi') == 'on':
            natija = True
        else:
            natija = False

        Student.objects.filter(id=son).update(
            ism = request.POST.get('ismi'),

            kitob_soni= request.POST.get('k_soni'),
            birituvchi = natija
        )
        return redirect('/student/')

    data = {
        'student':Student.objects.get(id=son)
    }
    return render(request,'student-edit.html',data)

def m_edit(request,num):
    if request.method == "POST":
        if request.POST.get('tirikmi') == 'on':
            natija = True
        else:
            natija = False
        Muallif.objects.filter(id=num).update(
            ism=request.POST.get('ismi'),
            tirik=natija,
            kitob_soni=request.POST.get('k_soni'),
            t_y =request.POST.get('ty')
        )
        return redirect('/ustoz/')
    data = {
        'muallif':Muallif.objects.get(id=num)
    }
    return render(request,'muallif-edit.html',data)

def r_edit(request,num):
    if request.method == "POST":
        if request.POST.get('qaytardi') == 'on':
            r = True
        else:
            r = False

        Record.objects.filter(id=num).update(
            olingan_sana = request.POST.get('olsana'),
            qaytardi=r,
            qaytargan_sana=request.POST.get('qaysana')
        )
        return redirect('/record/')
    data = {
        'record':Record.objects.get(id=num)
    }
    return render(request,'r_edi.html',data)

def m_tasdiqlash(request,num):
    data = {
        'muallif':Muallif.objects.get(id = num)
    }
    return render(request,'m_ochir.html',data)

def k_tasdiqlash(request,num):
    data = {
        'kitob':Kitob.objects.get(id = num)
    }
    return render(request,'k_ochir.html',data)

def r_tasdiqlash(request,num):
    data = {
        'recocrd':Record.objects.get(id = num)
    }
    return render(request,'r_ochir.html',data)
def r_ochir(request,num):
    Record.objects.get(id=num).delete()
    return redirect('/record/')

def talaba_tasdiqlash(request,son):
    data = {
        'talaba': Student.objects.get(id = son)

    }
    return render(request,'student_ochir.html',data)

def kitoblar(request):
    if request.user.is_authenticated:
        data = {
            'kitoblar':Kitob.objects.all()
        }

        return render(request,'mashq/kitob.html',data)
    else:
        return redirect('/')

def recordlar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forma = RecordForm(request.POST)
            if forma.is_valid():
                forma.save()
        soz = request.GET.get('search')
        if soz is None:
            s = Record.objects.all()
        else:
            s = Record.objects.filter(student__ism__contains = soz)

        data = {
        'book':Kitob.objects.all(),
        'studentlar':Student.objects.all(),
        'records':s,
        'forma':RecordForm
        }
        return render(request,'mashq/record.html',data)
    else:
        return redirect('/')


def kitobxon(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forma = KitobForm(request.POST)
            if forma.is_valid():
                forma.save()

            return redirect('/kitob/')
        data = {
            'mualliflar': Muallif.objects.all(),
            'book': Kitob.objects.all(),
            'forma': KitobForm
        }
        return render(request, 'mashq/kitob.html', data)
    else:
        return redirect('/')

def loginView(request):
    if request.method =='POST':
        user = authenticate(username=request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/kitoblar/')

    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )

        return redirect('/')
    return render(request,'register.html')
