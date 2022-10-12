from rest_framework import permissions
import ipdb; 

class UserPermission (permissions.BasePermission):
    def has_permissions(self, request, view):
        
        if request.user:
            return True;
        