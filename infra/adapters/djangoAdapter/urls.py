from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, PostViewSet

# Crie um router DRF para gerenciar as rotas automaticamente
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    # Inclua as rotas geradas pelo router
    path('api/', include(router.urls)),
    # Você pode adicionar outras rotas aqui, se necessário
]

# Adicione as rotas de autenticação, por exemplo, usando DRF
urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
