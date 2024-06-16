from django.shortcuts import render
import requests

def index(request):
        # URL de la API externa
    api_url = ' https://apis.datos.gob.ar/georef/api/provincias'
    
    # Realizar la solicitud GET a la API
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        data = response.json()
        provincias = data.get('provincias', [])
        provincias.sort(key=lambda x: x['id'])
    else:
        provincias = []
    
    # Pasar los datos al contexto
    context = {'provincias': provincias}
    
    return render(request, 'mi_app/index.html', context)
