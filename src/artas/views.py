from django.shortcuts import render
import requests, json


def index(request):
    api_address = f'{request.scheme}://{request.META["HTTP_HOST"]}/api/beyr/'
    print(api_address)
    response = requests.get(api_address).text   #   .strip('][').split(', ')    # convert str_list to list
    
    response = json.loads(response)
    return render(request, 'artas/index.html', {'serueia': response[0]['39'], 'chelseru': response[1]['40']})


def new_order(request):
    return render(request, 'artas/order_new.html', {})
