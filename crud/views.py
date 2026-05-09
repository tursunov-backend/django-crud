import json

from django.views import View
from django.http import HttpRequest, JsonResponse

from .models import Item


# FCB & CBV

class ItemsView(View):
    
    def get(request: HttpRequest) -> JsonResponse:
        items = [item.to_dict() for item in Item.objects.all()]

        data = {
            'itemas': items
        }
        return JsonResponse(data, safe=False)
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body)

        item = Item(name=data['name'], description=data.get('description', ''), amount=data['amount'])
        item.save()

        return JsonResponse({'message': 'ok'}, status=201)
    

class ItemView(View):
    pass



def items_view(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        items = [item.to_dict() for item in Item.objects.all()]

        data = {
            'itemas': items
        }
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)

        item = Item(name=data['name'], description=data.get('description', ''), amount=data['amount'])
        item.save()

        return JsonResponse({'message': 'ok'}, status=201)


# client > browser > Gunicorn > Middleware > Url Dispatcher > View
# client < browser < Gunicorn < Middleware < View

def item_one_view(request: HttpRequest, id: int) -> JsonResponse:
    if request.method == 'GET':
        # try:
        #     item = Item.objects.get(id=id)
        #     return JsonResponse(item.to_dict())
        # except Item.DoesNotExist:
        #     return JsonResponse({'error': 'not found.'})

        item = Item.objects.filter(id=id).first()
        if item:
            return JsonResponse(item.to_dict())
        else:
            return JsonResponse({'error': 'not found.'})
    elif request.method == 'DELETE':
        try:
            item = Item.objects.get(id=id)
            item.delete()
            return JsonResponse({'message': 'ok'})
        except Item.DoesNotExist:
            return JsonResponse({'error': 'not found.'})
    elif request.method == 'PUT':
        try:
            item = Item.objects.get(id=id)

            data = json.loads(request.body)
            
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            item.amount = data.get('amount', item.amount)

            item.save()
            
            return JsonResponse({'message': 'ok'})
        except Item.DoesNotExist:
            return JsonResponse({'error': 'not found.'})
    else:
        return JsonResponse({'message': 'not allowed'})

