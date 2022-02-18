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
        roofMaterial = wkdata['structures'][0]['roof_material']['class']
        roofCondition = wkdata['structures'][0]['roof_condition']['value']
        roofTopLocation = wkdata['structures'][0]['roof_top_location']['wkt']
        imageInfo = wkdata['structures'][0]['metadata']['gsd']
        layername = wkdata['structures'][0]['metadata']['layer_name']
        groundEvaluation = wkdata['structures'][0]['ground_elevation']['value']
        FootprintArea = wkdata['structures'][0]['footPrint']['area']
        SolarPanels = wkdata['structures'][0]['roof_solar']['value']
        TreeCoverPercent = wkdata['structures'][0]['tree_cover']['percent']
        RoofDiscolerated = wkdata['structures'][0]['roof_condition_report']['discolorated']['detected']
        feet30BuildingCoverage = wkdata['structures'][0]['defensible_space']['report']['DSB30']
        feet100BuildingCoverage = wkdata['structures'][0]['defensible_space']['report']['DSB100']
        DefensibleSpaceReport = wkdata['structures'][0]['defensible_space']['report']['DSB30']
        # Property Features
        Pool = wkdata['property_features']['pool']['score']
        PoolEnclosure = wkdata['property_features']['enclosure']['detected']
        DivingBoard = wkdata['property_features']['diving_board']['detected']
        WaterSlide = wkdata['property_features']['water_slide']['detected']
        Trampoline = wkdata['property_features']['trampoline']['detected']
        Deck = wkdata['property_features']['deck']['detected']
        Playground = wkdata['property_features']['playground']['detected']
        SportCourt = wkdata['property_features']['sport_court']['detected']

        OrthoURL = "https://api.gic.org/images/ExtractOrthoImages/?layer=bluesky-ultra&zoom=85&EPSG=4326&wkt=" + wktPolygon + "&token=" +authToken;
        #print(OrthoURL)
        return render(request, 'secondWindow.html',{'roofShape': roofShape,'roofCondition':roofCondition,  
        'flatPercent': flatPercent,'roofMaterial' : roofMaterial,'roofTopLocation':roofTopLocation,'groundEvaluation':groundEvaluation,
        'FootprintArea':FootprintArea,'SolarPanels':SolarPanels,'RoofDiscolerated':RoofDiscolerated,'TreeCoverPercent':TreeCoverPercent,
        'feet30BuildingCoverage':feet30BuildingCoverage,'feet100BuildingCoverage':feet100BuildingCoverage,'DefensibleSpaceReport':DefensibleSpaceReport,
        'imageInfo':imageInfo,'layername':layername,'Pool':Pool,'PoolEnclosure':PoolEnclosure,'DivingBoard':DivingBoard,'WaterSlide':WaterSlide,
        'Trampoline':Trampoline,'Deck':Deck,'Playground':Playground,'SportCourt':SportCourt,
        'OrthoURL': OrthoURL})

    
def secondWindow(request):
    return render(request, 'secondWindow.html')


def thirdWindow(request):
    return render(request, 'thirdWindow.html')
