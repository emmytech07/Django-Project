from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InvestorCustomRegistrationSerializer, InventorCustomRegistrationSerializer, UserSerializer
from rest_framework import generics,status,permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsInventor, IsInvestor



"""
@api_view(['GET'])
def allroutes(request):
    all_urls = {
        'investorSignUp': '/investorsignup/',
        'inventorsignup': '/inventorsignup/',
    
    }

    return Response(all_urls)
"""

class Inventorsignup(generics.GenericAPIView):
    serializer_class = InventorCustomRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
            
        })



class Investorsignup(generics.GenericAPIView):
    serializer_class = InvestorCustomRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
            
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']

        token, created= Token.objects.get_or_create(user=user)

        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_inventor':user.is_inventor
        })


class LogOutView(APIView):
    def post(self, request, *args, **kwargs):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class InvestorOnly(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsInvestor]

    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user


class InventorOnly(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsInventor]

    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user