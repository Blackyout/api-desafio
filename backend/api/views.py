from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Person, Product
from .serializers import PersonSerializer, ProductSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    
    # Filtros exactos para email y last_name
    filterset_fields = ['email', 'last_name']
    
    # Ordenamiento
    ordering_fields = ['created_at']
    ordering = ['-created_at']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtros avanzados
    filterset_fields = {
        'sku': ['exact'],
        'price': ['gte', 'lte'], # price__gte (min) y price__lte (max)
    }
    
    # Búsqueda por texto (query param: ?search=nombre)
    search_fields = ['name']
    
    # Ordenamiento
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']