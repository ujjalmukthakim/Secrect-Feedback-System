from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer,CommentSerializer,LoginSerializer
from .models import CoustomUser,Reaction,Link,Comment
from rest_framework.response import Response
from rest_framework import status
import hashlib
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

def get_ip_hash(request):
    ip = request.META.get('REMOTE_ADDR')
    return hashlib.sha256(ip.encode()).hexdigest()


# class LoginViewSet(APIView):
    def post(self,request):
        ip_hash=get_ip_hash(request)
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(
            username=username,
            password=password,
            
        )

        if user.ip_hash!=ip_hash:
            return Response(
                {
                    "message":"wrong IP"
                }
            )


        if user is not None:
            return Response(
                {
                    "message":"login..."
                }
            )
        return Response(
            {
                "message":"fake info"
            }
        )
        
class LoginViewSet(APIView):
    def post(self,request):
      serializer=LoginSerializer(data=request.data)
      ip_hash=get_ip_hash(request)
      print(ip_hash)
      if serializer.is_valid():
          username=serializer.validated_data['username']
          password=serializer.validated_data['password']

          user = serializer.validated_data["user"]
          if user is not None:
              if user.ip_hash !=ip_hash:
                  return Response(
                      {
                          "message":"wrong Ip"
                      }
                  )
          refresh=RefreshToken.for_user(user)
          return Response(
                  {
                      "access":str(refresh.access_token),
                      "refresh":str(refresh)
                  }
              )
      return Response(
          serializer.errors

          )
           
          
   




class RegisterViewSet(APIView):

    def post(self, request):

        ip_hash = get_ip_hash(request)

        if CoustomUser.objects.filter(ip_hash=ip_hash).exists():
            return Response(
                {
                    "message": "Already registered from this IP"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.ip_hash = get_ip_hash(request)
            user.save()

            return Response(
                {
                    "message": "User created successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ReactViewSet(APIView):

    def post(self,request,link_id):
        ip_hash=get_ip_hash(request)
        try:
          link=Link.objects.get(id=link_id)

        except Link.DoesNotExist:
            return Response(
                {
                    "message":"Link is invalid"
                }
            )
        if Reaction.objects.filter(link=link,ip_hash=ip_hash).exists():
            return Response(
                {
                    "message":"already exits.."
                }
            )
        
        Reaction.objects.create(
            ip_hash=ip_hash,
            link=link
        )
        return Response(
            {
                "message":"Done"
            }
        )

class CommentViewSet(APIView):
    def post(self,request,link_id):
        ip_hash=get_ip_hash(request)
        try:
            link=Link.objects.get(id=link_id)
        except Link.DoesNotExist:
            return Response(
                {
                    "message":'link is invalid'
                }
            )
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip_hash=ip_hash,link=link)
            return Response(
                {
                    "message":"Created Successfully"
                }
            )
        return Response(
            serializer.errors,
            status=400
        )
