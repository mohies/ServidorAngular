from django.urls import path
from . import api_views  # Asegúrate de importar las vistas correctas
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener el token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar el token
    
    
    
    path('login/', api_views.user_login, name='login'),
    path('logout/', api_views.user_logout, name='logout'),
    
    
    
    path('favorites/', api_views.list_favorites, name='list_favorites'),
    path('favorites/add/', api_views.add_favorite, name='add_favorite'),
    path('favorites/remove/<int:item_id>/', api_views.remove_favorite, name='remove_favorite'),
    
    

]
