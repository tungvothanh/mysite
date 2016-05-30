from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash

def index(request):
    return HttpResponse("Hello, world. You're at the top plz index.")

def simple_login(request):
    if request.POST:
        name = request.POST.get('username')
        password_sim = request.POST.get('password')

        user = authenticate(username=name,password=password_sim)

        if user is not None:
            if user.is_active:
                login(request,user)
                state = "you are logged in successfully"
                print(state)
            else:
                state = "your accout is not active"
        else:
            state = "your password / email is not correct"
        return render(request,'account/auth.html',{'state':state})
        # return redirect('http://127.0.0.1:8000/admin/')
    return render(request,'account/auth.html')
# coi nhu co ban la da login thanh cong
# dot doan nao thi search doan do thoi lo gi co chu
# it nhat thi cung khong phai ngay dem mo len freelancer lam gi cho met
# it nhat thi tu ta cung co the lam duoc
# nhiem vu tiep tuc la viet ham logout va changpassword
# i think it is not too difficult and you can done in today
# you are not smart but i belive you can do with you have learn
# try your best boy, belive yourself
# ham change password va reset password

def change_password(request):
    print("hell :) ")
    # o day n o dung thi vien a???
    # bo lao thiet
    # neu cai gi sai duoc thi sai thoi.
    # binh thuong thi minh phai lay duoc password va so sanh
    # in the case, if
    if request.POST:

        form =  PasswordChangeForm(user=request.user, data=request.POST)
        # current_password = request.POST.get('current_password')
        # new_password1 = request.POST.get('new_password1')
        # new_password2 = request.POST.get('new_password2')
        # if(new_password1!=new_password2):
        #     message = "the password is not match"
        #
        # if current_password !=
        # pass
    state = "ok, imagine that you have logged in"
    return render(request,'account/auth.html',{'state':state})
    # o day han tao form nhung thuc te eo can form lam gi


    # minh ko the tin duoc la bay gio minh da khac nhu the nao roi
    # khi moi thu deu co the hoc va code duoc het
    #

def logout(request):
    # okie, ham nay xu ly sau co ban cung ko co gi ghe gom tuy vao muc dicch su dung htoi.

    logout(request)
    print('hey da login roi do :D')
    return render(request,'account/auth.html',{})