import requests
from django.http import JsonResponse
from django.views import View
from requests.auth import HTTPBasicAuth

class ObtenerDatosApi(View):
    def get(self, request):
        survey_id = 2062  # El valor del survey_id
        access_key = '5kj1fbBG1M8%3D'
        
        # URL con survey_id y access_key incluidos
        url_api_externa = f'https://api-public.myhotel.io/followup/v2/surveys/2062/areas?access_key=5kj1fbBG1M8%3D&start_date=2024-06-01&end_date=2024-06-30'

        headers = {
            'x-api-key': 'TcAQ3AWjXK7LVhqEdAdkz9sD44zrOGH68k3RZABV',
        }

        # Configuración de la autenticación básica
        auth = HTTPBasicAuth('socialmediazuana@gmail.com', 'Zuana.2024*')

        # Realizamos la solicitud GET
        response = requests.get(url_api_externa, headers=headers, auth=auth)

        # Imprimir detalles de la solicitud y respuesta para depuración
      

        # Manejar la respuesta
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({
                "timestamp": response.headers.get("Date"),
                "code": response.status_code,
                "message": response.json().get("message", "Error"),
                "details": response.json().get("details", "")
            }, status=response.status_code)







