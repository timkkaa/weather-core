from django.views.generic import TemplateView

#API_KEY = 'acbb9cef0e941cd6c95e4dee15a0109a'
class WeatherInfoView(TemplateView):
    template_name = 'weather.html'


