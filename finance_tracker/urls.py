from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from finances.views import ExpenseViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
