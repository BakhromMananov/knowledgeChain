from django.contrib import messages
from django.shortcuts import redirect

from space.models import Post

def login_required(login_url='/'):

    def func_process(func):

        def process(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'You should be authenticated to edit posts!')
                return redirect(login_url)
            return func(request, *args, **kwargs)
        return process
    return func_process