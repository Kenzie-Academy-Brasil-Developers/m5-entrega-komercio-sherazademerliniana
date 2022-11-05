from rest_framework import generics
from .models import Seller
from .serializers import SellerSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwner, IsAdmin

# Create your views here.


class SellerView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerDetailView(generics.ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get_queryset(self):
        max_users = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:max_users]


class SellerUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def patch(self, request, *args, **kwargs):
        key_is_active = request.data.get("is_active")
        key_is_superuser = request.data.get("is_superuser")
        if key_is_active:
            request.data.pop("is_active")
        elif key_is_superuser:
            request.data.pop("is_superuser")

        return self.partial_update(request, *args, **kwargs)


class AdminSellerUpdate(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
