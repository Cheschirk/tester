from django.shortcuts import render
from modules.profile.models import User
from django.views import generic
from modules.profile.forms import SigninForm, LoginForm#, UserUpdateForm
from django.views.generic.edit import FormView, BaseUpdateView
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

        # # user.password = make_password(form.cleaned_data['password'])
        # # instance.set_password(form.cleaned_data['password'])
        # instance.user = self.request.user
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

# class UserUpdateView(BaseUpdateView):
#     model = User
#     form_class = UserUpdateForm
#     template_name = 'profile/user_settings.html'

    # def get(self):
    #     return self.queryset.object
    # def get(self, request, *args, **kwargs):
    #     return self.request.object()

    # def get_object(self, queryset=None):
    #     return self.request.object()
    #
    # def get_object(self, queryset=None):
    #     """
    #     Для неавторизованного пользователя возвращает 404 ошибку
    #     Конечно мы можем как и в предыдущем примере использовать декоратор login_required
    #     """
    #     object = super(UserUpdateView, self).get_object()
    #     return object

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.save()
    #     return super().form_valid(form)







