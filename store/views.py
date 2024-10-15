from django.shortcuts import render,redirect
from store.models import Item
from users.models import CharInfo
from member.models import Characters, Purchase
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

@login_required(login_url='/login')
def store_main(request):
    getUser = request.user
    userinfo = CharInfo.objects.get(user=getUser)
    
    item1 = Item.objects.get(itemID=1)
    item2 = Item.objects.get(itemID=2)
    item3 = Item.objects.get(itemID=3)
    item4 = Item.objects.get(itemID=4)
    item5 = Item.objects.get(itemID=5)
    item6 = Item.objects.get(itemID=6)
    
    item7 = Item.objects.get(itemID=7)
    item8 = Item.objects.get(itemID=8)
    item9 = Item.objects.get(itemID=9)
    item10 = Item.objects.get(itemID=10)
    item11 = Item.objects.get(itemID=11)
    item12 = Item.objects.get(itemID=12)
    
    page1_row1 = [item1,item2,item3]
    page1_row2 = [item4,item5,item6]
    page2_row1 = [item7,item8,item9]
    page2_row2 = [item10,item11,item12]
    
    
    
    if request.method == "POST":
        print("dsfsgwsegwgsdf")
        name = request.POST['itemName']
        itemPrice = request.POST['totalPrice']
        count = request.POST['quantity']
        
        # 갈레온 차감
        userinfo.galeon = int(userinfo.galeon) - int(itemPrice)
        userinfo.save()
        
        # 구매내역 저장
        char = Purchase(itemCount=count,
                        orderDate=datetime.today(),
                        itemInfo=Item.objects.get(itemName=name),
                        user=getUser)
        char.save()
    
    
    context = {'page1_row1':page1_row1,
               'page1_row2':page1_row2,
               'page2_row1':page2_row1,
               'page2_row2':page2_row2,
               'user':userinfo}

    return render(request, "store/store_main.html", context)

