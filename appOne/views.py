from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from appOne.models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodTypes, Goods, User, Order


def home(request):
    wheel = Wheel.objects.all()
    nav = Nav.objects.all()
    mustbuylist = Mustbuy.objects.all()
    shoplist = Shop.objects.all()
    shop1 = shoplist[0:1]
    shop2 = shoplist[1:3]
    shop3 = shoplist[3:7]
    shop4 = shoplist[7:11]

    mainshowlist = MainShow.objects.all()

    context = {'headername': '主页', 'pageTitle': '主页', 'wheelsList': wheel, "navlist": nav, 'mustbuylist': mustbuylist,
               'shop1list': shop1, 'shop2list': shop2,
               'shop3list': shop3, 'shop4list': shop4, 'mainshowlist': mainshowlist}
    return render(request, 'appOne/home.html', context)


def market(request):
    foottypeList = FoodTypes.objects.all()
    goodsList = Goods.objects.all()[0:16]
    context = {'goodsList': goodsList, 'foottypeList': foottypeList}

    return render(request, 'appOne/market.html', context)


def markethandle(request, foodtype, childcid, ordering):
    foottypeList = FoodTypes.objects.all()

    if ordering == '0':
        orderRule = 'id'
    elif ordering == '1':
        orderRule = 'price'
    elif ordering == '2':
        orderRule = 'productnum'
    elif ordering == '3':
        orderRule = '-price'
    else:
        orderRule = 'id'

    if childcid == '0':
        goodsList = Goods.objects.all().filter(categoryid=foodtype).order_by(orderRule)
    else:
        goodsList = Goods.objects.all().filter(categoryid=foodtype).filter(childcid=childcid).order_by(orderRule)

    foodtypeseleted = FoodTypes.objects.filter(typeid=foodtype).first()
    foodtypeseletedname = foodtypeseleted.childtypenames
    foodtypenamelist = foodtypeseletedname.split('#')
    category = []
    for i in foodtypenamelist:
        typechild = i.split(':')
        typechilddic = {'typechildname': typechild[0], 'typechildid': typechild[1]}
        category.append(typechilddic)

    context = {'childid': childcid, 'ordering': ordering, 'foodtype': foodtype,
               'category': category, 'foottypeList': foottypeList, 'goodsList': goodsList}
    return render(request, 'appOne/market.html', context)


def cart(request):
    username = request.COOKIES.get('user')
    user = User.objects.filter(name=username).first()
    order = Order.objects.filter(orderUser=user).last()
    try:
        if order.orderFlag == 'cart':
            orderGoodsList = str(order.orderInfo)
            orderGoodsList = orderGoodsList.strip('[').strip(']')
            orderGoodsList = orderGoodsList.split(',')
            orderProList = []
            orderProNumList = []
            orderGoodsPrice = []
            for i in range(len(orderGoodsList)):
                orderGoodsList[i] = str(orderGoodsList[i])
                orderGoodsList[i] = orderGoodsList[i].strip()
                orderGoodsList[i] = int(orderGoodsList[i])
                if i % 2 == 0:
                    if orderGoodsList[i+1] != ' 0':
                        goods = Goods.objects.filter(productid=orderGoodsList[i]).first()
                        orderGoodsPrice.append(float(goods.price))
                        orderProList.append(goods)
                else:
                    if orderGoodsList[i] != 0:
                        orderProNumList.append(orderGoodsList[i])
            priceSum = 0
            for i in range(len(orderGoodsPrice)):
                priceSum = priceSum + (orderGoodsPrice[i] * int(orderProNumList[i]))

            context = {'priceSum':priceSum,'orderProNumList':orderProNumList,'pageTitle': '小车', 'headername': '小车', 'orderProList': orderProList}
            return render(request, 'appOne/cart.html', context)
        else:
            return render(request, 'appOne/nullcart.html')
    except:
        return render(request,'appOne/nullcart.html')


def mine(request):
    username = request.COOKIES.get('user')
    context = {'pageTitle': '我的', 'headername': '我的', 'username': username}
    return render(request, 'appOne/mine.html', context)


def checkname(request):
    name = request.GET.get('username')
    if len(User.objects.filter(name=name)) == 0:
        status_dic = {'status': 'ok'}
    else:
        status_dic = {'status': 'no ok'}

    return JsonResponse(status_dic)


def adduser(request):
    user = User()
    name = request.GET.get('username')
    user.name = name
    passwordOne = request.GET.get('password')
    passwordTwo = request.GET.get('passwordtwo')
    if passwordOne == passwordTwo:
        user.password = passwordTwo
    else:
        return HttpResponse('你真是一个 小傻 两次输入密码不一样')
    user.email = request.GET.get('email')
    user.save()
    response = HttpResponseRedirect(reverse('axf:regeditsuccsess'))
    response.set_cookie('user', name, max_age=None)
    return response


def loadregedit(request):
    return render(request, 'appOne/mineregedit.html')


def loadlogin(request):
    return render(request, 'appOne/mineLogin.html')


def dologin(request):
    name = request.GET.get('username')
    user = User.objects.filter(name=name).first()
    checkpassword = request.GET.get('password')
    if user.password == checkpassword:
        response = HttpResponseRedirect(reverse('axf:mine'))
        response.set_cookie('user', name, max_age=None)
        return response
    else:
        return render(request, 'appOne/mineLogin.html')


def checkloginname(request):
    name = request.GET.get('username')
    if len(User.objects.filter(name=name)) == 0:
        status_dic = {'status': '用户名不存在'}
    else:
        status_dic = {'status': 'ok'}

    return JsonResponse(status_dic)


def minelogout(request):
    response = HttpResponseRedirect(reverse('axf:loadlogin'))
    response.delete_cookie('user')

    return response


def regeditsuccsess(request):
    return render(request, 'appOne/regeditSuccess.html')


def checkpwdagain(request):
    pwd = request.GET.get('pwd')
    pwdagain = request.GET.get('pwdagain')
    if pwd == pwdagain:
        status_dic = {'status': 'ok'}
    else:
        status_dic = {'status': '两次密码输入不一样'}

    return JsonResponse(status_dic)


def carthandele(request, flag):
    username = request.COOKIES.get('user')

    if username == None:
        return JsonResponse({'status': 'usernone'})
    else:
        if flag == '0':
            user = User.objects.filter(name=username).first()
            productid = request.GET.get('productid')
            order = Order.objects.filter(orderUser=user).filter(orderFlag='cart')
            if order.count() == 0:
                order = Order()
                order.orderUser = user
                orderGoodsList = [int(productid), 1]
                order.orderInfo = orderGoodsList
                order.save()
            else:
                order = Order.objects.filter(orderUser=user).last()
                orderGoodsList = order.orderInfo
                orderGoodsList = str(orderGoodsList).strip('[').strip(']')
                orderGoodsList = orderGoodsList.split(',')
                try:
                    orderGoodsListNew = []
                    for i in orderGoodsList:
                        i = i.strip()
                        orderGoodsListNew.append(i)
                    index = orderGoodsListNew.index(productid)
                    orderGoodsListNew[index + 1] = int(orderGoodsListNew[index + 1]) + 1
                    orderGoodsListPlus = []
                    for i in orderGoodsListNew:
                        i = str(i)
                        i = i.strip('\\').strip("\'").strip("\"")
                        i = i.strip()
                        i = int(i)
                        orderGoodsListPlus.append(i)
                    order.orderInfo = orderGoodsListPlus
                    order.save()
                except:
                    orderGoodsList.append(productid)
                    orderGoodsList.append('1')
                    orderGoodsListPlus = []
                    for i in orderGoodsList:
                        i = str(i)
                        i = i.strip('\\').strip("\'").strip("\"")
                        i = i.strip()
                        i = int(i)
                        orderGoodsListPlus.append(i)
                    order.orderInfo = orderGoodsListPlus
                    order.save()
            return JsonResponse({'status': 'ok'})

        else:
            user = User.objects.filter(name=username).first()
            productid = request.GET.get('productid')
            order = Order.objects.filter(orderUser=user).first()
            orderGoodsList = order.orderInfo
            orderGoodsList = str(orderGoodsList).strip('[').strip(']')
            orderGoodsList = orderGoodsList.split(',')

            orderGoodsListNew = []
            for i in orderGoodsList:
                i = i.strip()
                orderGoodsListNew.append(i)
            index = orderGoodsListNew.index(productid)
            orderGoodsListNew[index + 1] = int(orderGoodsListNew[index + 1]) - 1
            orderGoodsListPlus = []
            for i in orderGoodsListNew:
                i = str(i)
                i = i.strip('\\').strip("\'").strip("\"")
                i = i.strip()
                i = int(i)
                orderGoodsListPlus.append(i)
            order.orderInfo = orderGoodsListPlus
            order.save()
            return JsonResponse({'status': 'ok'})


def payment(request):
    return render(request,'appOne/payment.html')

def chageorderflag(request):
    username = request.COOKIES.get('user')
    user = User.objects.filter(name=username).first()
    order = Order.objects.filter(orderUser=user).last()
    order.orderFlag = 'order'
    order.save()

    return None


def orderlist(request):
    username = request.COOKIES.get('user')
    user = User.objects.filter(name=username).first()
    order = Order.objects.filter(orderUser=user).first()
    try:
        if order.orderFlag == 'order':
            orderGoodsList = str(order.orderInfo)
            orderGoodsList = orderGoodsList.strip('[').strip(']')
            orderGoodsList = orderGoodsList.split(',')
            orderProList = []
            orderProNumList = []
            orderGoodsPrice = []
            for i in range(len(orderGoodsList)):
                orderGoodsList[i] = str(orderGoodsList[i])
                orderGoodsList[i] = orderGoodsList[i].strip()
                orderGoodsList[i] = int(orderGoodsList[i])
                if i % 2 == 0:
                    if orderGoodsList[i + 1] != ' 0':
                        goods = Goods.objects.filter(productid=orderGoodsList[i]).first()
                        orderGoodsPrice.append(float(goods.price))
                        orderProList.append(goods)
                else:
                    if orderGoodsList[i] != 0:
                        orderProNumList.append(orderGoodsList[i])
            priceSum = 0
            for i in range(len(orderGoodsPrice)):
                priceSum = priceSum + (orderGoodsPrice[i] * int(orderProNumList[i]))

            context = {'priceSum': priceSum, 'orderProNumList': orderProNumList,
                       'orderProList': orderProList}
            return render(request, 'appOne/order.html', context)
    except:
        return render(request, 'appOne/nullcart.html')



