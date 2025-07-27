from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import uuid

# Simulación de base de datos local en memoria
data_list = []

# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False}) # Ejemplo de item inactivo

class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):
        # Filtra la lista para incluir solo los elementos donde 'is_active' es True
        active_items = [item for item in data_list if item.get('is_active', False)]
        return Response(active_items, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data

        # Validación mínima
        if 'name' not in data or 'email' not in data:
            return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        data['id'] = str(uuid.uuid4())
        data['is_active'] = True
        data_list.append(data)

        return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)

class DemoRestApiItem(APIView):
    
    def put(self, request, item_id):
        data = request.data

        # Buscar el elemento por ID (usando el parámetro de la URL)
        for index, item in enumerate(data_list):
            if item['id'] == item_id:
                # Reemplazar completamente los datos, excepto el identificador
                data['id'] = item_id  # Mantener el ID original
                data['is_active'] = item['is_active']  # Mantener el estado activo
                data_list[index] = data
                return Response({'message': 'Dato actualizado exitosamente.', 'data': data}, status=status.HTTP_200_OK)

        return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, item_id):
        data = request.data

        # Buscar el elemento por ID (usando el parámetro de la URL)
        for index, item in enumerate(data_list):
            if item['id'] == item_id:
                # Actualizar parcialmente los campos
                for key, value in data.items():
                    if key != 'id':  # No permitir la modificación del ID
                        item[key] = value
                return Response({'message': 'Dato actualizado parcialmente.', 'data': item}, status=status.HTTP_200_OK)

        return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, item_id):
        # Buscar el elemento por ID (usando el parámetro de la URL)
        for index, item in enumerate(data_list):
            if item['id'] == item_id:
                # Eliminar lógicamente el elemento
                item['is_active'] = False  # Cambiar el estado a inactivo
                return Response({'message': 'Elemento eliminado lógicamente.', 'data': item}, status=status.HTTP_200_OK)

        return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)