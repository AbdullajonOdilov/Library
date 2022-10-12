from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sinashga/', sinashga),

    path('mashq/', mashq),

    path('b/',bitiruvchi_student),

    path('kitob/',kitobxon),
    path('books/<int:son>/',book),

    path('record/',recordlar),



    path('b_r/',b_s_r),
    path('records/<int:num>/',info),
    path('r_edit/<int:num>/', r_edit),



    path('tirik/',tiriklar),
    path('sahifas/',eng_katta),
    path('sana/',olingan_sana),
    path('tmk/',t_m_k),
    path('badiy/',badiiy),
    path('astu/',a_s),
    path('katta/',qari),
    path('s_erkak/',erkak),
    path('kam/',kam),
    path('kop/',eng_kop),

    path('student/',all_student),
    path('talaba_ochir/<int:son>/',student_ochir),
    path('talaba/<int:son>/', talaba),
    path('talaba_edit/<int:son>/', student_edit),
    path('t_tas/<int:son>/', talaba_tasdiqlash),

    path('teacher/<int:num>/', teacher),
    path('m_edit/<int:num>/', m_edit),
    path('m_tas/<int:num>/', m_tasdiqlash),
    path('ustoz/', all_techers),

    path('kitob_ochir/<int:son>/',kitob_ochir),
    path('k_tas/<int:num>/', k_tasdiqlash),
    path('r_tas/<int:num>/', r_tasdiqlash),
    path('r_ochir/<int:num>/', r_ochir),
    path('kitoblar/',kitoblar),
    path('',loginView),
    path('logout/',logoutView),
    path('register/',signup),




]
