from django.shortcuts import render
from django.http import JsonResponse
import json
import os

def map_view(request):
    return render(request, 'navigation/map.html')



def streetlight_data(request):
    file_path = os.path.join('data', '전국보안등정보표준데이터.json')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'File not found'}, status=404)
