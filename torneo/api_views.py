from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .forms import *
from django.db.models import Q, Prefetch
from django.contrib.auth.models import Group
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "message": "Login exitoso", "username": user.username})
        else:
            return JsonResponse({"success": False, "message": "Credenciales incorrectas"}, status=401)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout exitoso'}, status=200)




from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_favorite(request):
    user = request.user
    data = request.data.copy()
    data['user'] = user.id
    serializer = FavoriteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def remove_favorite(request, item_id):
    try:
        favorite = Favorite.objects.get(user=request.user, item_id=item_id)
        favorite.delete()
        return Response({"message": "Eliminado de favoritos"}, status=status.HTTP_204_NO_CONTENT)
    except Favorite.DoesNotExist:
        return Response({"error": "Favorito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

