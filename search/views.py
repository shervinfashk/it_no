from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):

    context  = {
        "posts": Post.objects.all(),
    }

    return render(request,'search/home.html',context)

def sok(request):
    
    pris = request.GET.get('Pris')
    
    minBredde = request.GET.get('minBredde')
    maksBredde = request.GET.get('maksBredde')
    
    minLengde = request.GET.get('minLengde')
    maksLengde = request.GET.get('maksLengde')
    
    solgt = request.GET.get('Solgt')
    if (solgt == None):
        solgt = 1
    
    context  = {
        "posts": Post.objects.all().filter(PRICE__lte=pris).filter().filter(WIDTH__range=(minBredde, maksBredde)).filter(LENGTH__range=(minLengde, maksLengde)).filter(QTY__range=(solgt, 1)).values(),
        "verdier": {"pris":pris, "minBredde":minBredde, "maksBredde":maksBredde, "minLengde":minLengde, "maksLengde":maksLengde}
    }
      
    return render(request,'search/sok.html',context)
