from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, forms


class RegistrationView(CreateView):
    form_class = forms.SocFondUserForm
    template_name = 'fond/register.html'
    success_url = 'fond/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data['age']
        gender = form.cleaned_data['gender']
        stag = form.cleaned_data['stag']

        if age >= 60 and stag >= 40 :
            self.object.fond = 'пенсия по стажу для мужчин'
        elif age >= 55 and stag >= 35:
            self.object.fond = 'пенсия по стажу для женщин'
        elif age >= 63 and stag >= 25:
            self.object.fond = 'пенсия по старости для мужчин'
        elif age >= 58 and stag >= 20:
            self.object.fond = 'пенсия по старости для женщин'
        else:
            self.object.fond = 'Вам пенсия не назначена, так как у вас не хватает стаж'
        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'fond/login.html'

    def get_success_url(self):
        return reverse('fond:fond_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('fond:login')


class UserListView(ListView):
    template_name = 'fond/fond_list.html'
    model = models.SocFondUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fond'] = getattr(self.request, 'fond', 'недостаток одного или нескольких видов стажа')
        return context