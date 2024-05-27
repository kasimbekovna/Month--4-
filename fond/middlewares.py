from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class AgeSocFondMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            gender = request.POST.get('gender')
            stag = int(request.POST.get('stag'))
            instance = {}

            if age < 35:
                return HttpResponseBadRequest('Ваш возраст слишком мал для регистрации')

            elif gender == 'Male' and age <= 60:
                if stag >= 40:
                    instance['fond'] = 'пенсия по стажу для мужчин'
                else:
                    return HttpResponseBadRequest('Вам пенсия не назначено, так как у вас не хватает стажа')

            elif gender == 'Female' and age <= 55:
                if stag >= 35:
                    instance['fond'] = 'пенсия по стажу для женщин'
                else:
                    return HttpResponseBadRequest('Вам пенсия не назначено, так как у вас не хватает стажа')

            elif gender == 'Male' and age <= 63:
                if stag >= 25:
                    instance['fond'] = 'пенсия по старости для мужчин'
                else:
                    return HttpResponseBadRequest('Вам пенсия не назначено, так как у вас не хватает стажа')

            elif gender == 'Female' and age <= 58:
                if stag >= 20:
                    instance['fond'] = 'пенсия по старости для женщин'
                else:
                    return HttpResponseBadRequest('Вам пенсия не назначено, так как у вас не хватает стажа')

            else:
                return HttpResponseBadRequest('Вам пенсия не назначено, так как у вас не хватает стажа')
