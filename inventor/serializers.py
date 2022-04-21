from rest_framework import serializers
#from rest_auth.registration.serializers import RegisterSerializer
from .models import investor, inventor, User



class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['username','first_name', 'last_name', 'email_address', 'phone','country', 'is_inventor']


class InvestorCustomRegistrationSerializer(serializers.ModelSerializer):

        password2 = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        #password = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        class Meta:
                model = User
                fields = ['username','first_name', 'last_name', 'email_address','password', 'password2', 'phone', 'country']
                extra_kwargs = {'password': {'write_only': True}}
                

        def save(self, **kwargs):
            user = User(
                username =self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email_address=self.validated_data['email_address'],
                phone=self.validated_data['phone'],
                country=self.validated_data['country'],
            )

            password=self.validated_data['password'],
            password2=self.validated_data['password2'],
            if password!=password2:
                raise serializers.ValidationError({"error":"password does not match"})


            user.set_password(self.validated_data['password'],)
            user.is_investor=True
            user.save()
            investor.objects.create(user=user)
            return user



class InventorCustomRegistrationSerializer(serializers.ModelSerializer):
    
        password2 = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        #password = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        class Meta:
                model = User
                fields = ['username','first_name', 'last_name', 'email_address','password', 'password2', 'phone', 'country']
                extra_kwargs = {'password': {'write_only': True}}
                

        def save(self, **kwargs):
            user = User(
                username =self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email_address=self.validated_data['email_address'],
                phone=self.validated_data['phone'],
                country=self.validated_data['country'],
            )

            password=self.validated_data['password'],
            password2=self.validated_data['password2'],
            if password!=password2:
                raise serializers.ValidationError({"error":"password does not match"})


            user.set_password(self.validated_data['password'],)
            user.is_inventor=True
            user.save()
            inventor.objects.create(user=user)
            return user

          