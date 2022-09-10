from django.shortcuts import render
from django.core.exceptions import PermissionDenied



def is_session_active(function):

    def wrap(request, *args, **kwargs):
        try:
            userId = request.session["id"]
            if userId:
                return function(request, *args, **kwargs)
            else:
                return render(request, "login.html", {"msg": "session timeout,Please login again"})
        except Exception:
            return render(request, "login.html", {"msg": "session timeout,Please login again"})


    return wrap