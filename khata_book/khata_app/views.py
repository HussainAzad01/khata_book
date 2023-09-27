from django.shortcuts import render, redirect
from .models import Khata_book, User
from datetime import date
from .helpers import grand_total, getClientList
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signupUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already Exists")
            return render(request, "khata_app/signup.html")

        if password == password_repeat and len(password) >= 5:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('/login')
        else:
            messages.info(request, "Password doesn't match or too short, Please try again!!")

    return render(request, "khata_app/signup.html")


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_user = authenticate(request, username=username, password=password)
        print(username)
        print(is_user)
        if is_user is not None:
            login(request, is_user)
            return redirect('/client-list')
        else:
            messages.info(request, "Wrong username or password, please try again!")

    return render(request, 'khata_app/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


@login_required
def add_client(request, client_name=None):
    if request.method == 'POST':
        customer_name = request.POST.get('clientName').capitalize()
        goods = request.POST.get('goods')
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        price_per_piece = request.POST.get('pricePerPiece')
        due_date = request.POST.get('due-date')
        total_amount = int(quantity) * int(price_per_piece)
        entry = Khata_book.objects.create(
            user=request.user,
            client_name=client_name if client_name == customer_name else customer_name,
            goods=goods,
            quantity=quantity,
            price=price_per_piece,
            size=size,
            total_amount=total_amount,
            created_on=date.today(),
            due_date=None if due_date == '' else due_date
        )
        return redirect('/client-list')

    params = {'client': client_name}
    return render(request, 'khata_app/client_add_view.html', params)


@login_required
def client_list(request):
    loggeduser = request.user
    params = {'data': getClientList(loggeduser, None)}
    return render(request, 'khata_app/client_list_view.html', params)


@login_required
def client_detail_view(request, client_name):
    data = Khata_book.objects.filter(user=request.user)
    # datas = Khata_book.objects.filter(client_name=client_name)
    datas = data.filter(client_name=client_name)
    if len(datas) == 0:
        return redirect('/client-list')
    amount = grand_total(datas)

    params = {"client_name": datas[0].client_name, 'data': datas, 'total_amount': amount}
    return render(request, 'khata_app/client_detail_view.html', params)


@login_required
def delete_goods(request, client_name, good_id):
    data_set = Khata_book.objects.filter(client_name=client_name)
    good = data_set.filter(id=good_id).first()
    url = f"/client-khata/{client_name}"
    good.delete()
    return redirect(url)


@login_required
def search(request):
    loggeduser = request.user
    if request.method == 'POST':
        query = request.POST.get('search-field')
        data = Khata_book.objects.filter(user=loggeduser)
        query_result = data.filter(client_name__contains=query.capitalize())

        if not query:
            return redirect('/client-list')
        if len(query_result) == 0:
            return render(request, 'khata_app/search.html')
        client = getClientList(loggeduser, query_result[0])
        params = {'data': client}
        return render(request, 'khata_app/search.html', params)
    else:
        return render(request, 'khata_app/search.html')
