from django.shortcuts import render
from modules.profile.models import User
from django.views import generic
from modules.profile.forms import SigninForm, LoginForm, UserUpdateForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.conf import settings



def user_settings(request):
    return render(request, '../templates/profile/user_settings.html')


class SigninView(generic.CreateView):
    model = User
    form_class = SigninForm
    template_name = 'profile/signin.html'
    success_url = "/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.


class LoginView(FormView):
    form_class = LoginForm
    model = User

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = 'profile/login.html'
    success_url = "/"

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


    # def my_view(self, request):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #
    #     if Profile is not None:
    #         login(request, user)
    #         return HttpResponseRedirect("/")

#class UserUpdateView(generic.UpdateView):
 #   model = Profile
  #  form_class = UserUpdateForm
   # template_name = 'profile/user_settings.html'
#
 #   def form_valid(self, form):
  #      instance = form.save(commit=False)
   #     instance.user = self.request.user
    #    instance.save()
     #   return super().form_valid(form)




