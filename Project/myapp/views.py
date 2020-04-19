from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Address
from myapp.forms import AddressForm
import requests

def Home(request):
# from requests import get
# ip = get('https://api.ipify.org').text #the above concept is meant to be used to know the ip address of the specific user
# print('My public IP address is:', ip)

    if request.method=="POST":
        form=AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=AddressForm()
    url = "https://api.ipfind.com?ip={}&auth=388a1108-c672-4acf-a898-eb810389b32b"
    address=Address.objects.all()
    captured_data=[]
    for address in address:
        response=requests.get(url.format(address)).json()
        print(response)

        address_data={
        "address":response["ip_address"],
        "country":response['country'],
        "country_code":response['country_code'],
        "continent":response['continent'],
        "city":response['city'],
        "longitude":response['longitude'],
        "latitude":response['latitude'],
        "currency":response['currency'],
        "official_language":response['languages'][0],
        "national_language":response['languages'][1]

        }
        captured_data.append(address_data)
    print(captured_data)
    context={
    'address':captured_data,
    'form':form
    }
    return render(request,'myapp/home.html',context)
