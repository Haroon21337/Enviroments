from django.shortcuts import render, HttpResponse

# Create your views here.
from django.contrib import admin
from django.urls import path
import requests



# Create your views here.


def index(request):
    return render(request, 'index.html')

def store(request):
    if request.method=="POST":
        address = request.POST['address']
        print(address)
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
        }
      
        r = requests.post('https://api.gic.org/auth/Login',  data={'username': 'aortiz@safepointins.com', 'password': 'Tachoa@2600'}, headers=headers)
        data = r.json()
        authToken =data['token']
    
        #print(r.json())
        url="https://api.gic.org/property/GetPropertyInformation?wkt=POINT("+address+")&token="+authToken

        #url='https://api.gic.org/property/GetPropertyInformation?wkt=POINT(-82.7139639007722849 27.8590883896834072)&token='+authToken
        wk= requests.post(url)
        cnt=0
        wkdata=wk.json()
        wktPolygon = wkdata['structures'][0]['footPrint']['wkt']
        roofShape=wkdata['structures'][0]['roof_shape']['value']
        flatPercent=wkdata['structures'][0]['roof_shape']['flatPercent']
       

        OrthoURL = "https://api.gic.org/images/ExtractOrthoImages/?layer=bluesky-ultra&zoom=85&EPSG=4326&wkt=" + wktPolygon + "&token=" +authToken;
        #print(OrthoURL)
        return render(request, 'secondWindow.html',{'roofShape': roofShape,
        'flatPercent': flatPercent,
        
        'OrthoURL': OrthoURL})

    
def secondWindow(request):
    return render(request, 'secondWindow.html')


def thirdWindow(request):
    return render(request, 'thirdWindow.html')
