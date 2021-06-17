from django.shortcuts import render
from .models import Image,ImageSuccess,Details
from random import randint
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    # total=len(Image.objects.all())
    total=Image.objects.all().count()
    # print(total)
    imgid=randint(11, 10+total)
    image=Image.objects.get(pk=imgid)

    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        amount=int(request.POST.get("amount"))*100
        client=razorpay.Client(auth=("rzp_test_FevfFiPQZ3dC0F","MSqH0ikpICP3jSoixBPDcYOr"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        detail=Details(name=name,amount=amount,email=email,payment_id=payment['id'])
        print(payment)
        detail.save()

        return render(request, 'index.html',{"image":image, "payment":payment})
    return render(request, 'index.html',{"image":image})

@csrf_exempt
def success(request):
    total=ImageSuccess.objects.all().count()
    icnid=randint(1, total)
    icon=ImageSuccess.objects.get(pk=icnid)

    if request.method=="POST":
        a=request.POST
        # print(a)
        order_id=""
        for key,val in a.items():
            if key=='razorpay_order_id':
                order_id=val
                break
        user=Details.objects.filter(payment_id=order_id).first()
        user.paid=True
        user.save()

        msg_plain=render_to_string('email.txt')
        msg_html=render_to_string('email.html')
        send_mail("Payment Successfull", msg_plain, settings.EMAIL_HOST_USER, [user.email],html_message=msg_html)

    return render(request,'success.html',{"icon":icon})
