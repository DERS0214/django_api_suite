from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from datetime import datetime

class LandingAPI(APIView):
    name = "Landing API"

    collection_name = "reviews"  # Cambia este nombre según tu colección en Firebase

    def get(self, request):
        # Referencia a la colección
        ref = db.reference(f'{self.collection_name}')

        # get: Obtiene todos los elementos de la col ección
        data = ref.get()

        # Devuelve un arreglo JSON
        return Response(data, status=status.HTTP_200_OK)
    # Aquí puedes agregar los métodos para manejar las solicitudes GET, POST, etc.
    def post(self, request):
        # Extrae los datos del request
        message = request.data.get('message')
        name = request.data.get('name')
        rating = request.data.get('rating')
        timestamp = request.data.get('timestamp', datetime.utcnow().isoformat())

        if not all([message, name, rating]):
            return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        # Genera un nuevo ID para la review
        ref = db.reference(f'{self.collection_name}')
        new_id = ref.push().key

        review_data = {
            'message': message,
            'name': name,
            'rating': rating,
            'timestamp': timestamp
        }

        # Guarda la nueva review en la base de datos
        ref.child(new_id).set(review_data)

        return Response({'id': new_id, 'review': review_data}, status=status.HTTP_201_CREATED)
