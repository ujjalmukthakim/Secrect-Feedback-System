from rest_framework import serializers
from .models import CoustomUser,Comment
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, attrs):
        user=authenticate(
            username=attrs["username"],
            password=attrs["password"]
        )
        if not user:
            raise serializers.ValidationError("Invalid User")
        
        attrs["user"]=user
        return attrs
    # class Meta :
    #     model =CoustomUser
    #     fields=['username','password']


        




class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta :
        model = CoustomUser
        fields=['username','password']
    def create(self, validated_data):
        user=CoustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']

        )
        return user
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields=['context']