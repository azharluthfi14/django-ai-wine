from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
import numpy as np
import joblib
from .models import WineClassification


class LandingPageView(TemplateView):
    """
    Landing page class base view :
        - Check user is authenticated or not.
        - If user is authenticated redirect page to dashboard.
        - Else stay on landing page.
    """
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app:dashboard')
        return super(LandingPageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Scientics - Homepage'
        return context


class DashboardView(TemplateView):
    template_name = 'page/dashboard.html'
    """
    Dashboard page class based view:
        - Check user status authenticated or not.
        - User must login with their account.
        - If user admin display status user admin on dashboard page.
        - Else user member display status user member on dashboard page.
    """

    def get_context_data(self):
        role = self.request.user.is_staff
        status = "Admin" if role == 1 else "Member"
        context = {
            'status': status,
            'title': 'Scientics - Dashboard'
        }
        return context


class FormView(TemplateView):
    template_name = 'page/forms.html'
    """
    Form classification class based view:
        - Login required for this page.
    """

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['title'] = 'Scientics - Classification'
        return data


@login_required(login_url='app:signin')
def predict_submit(request):
    if request.POST.get('action') == 'POST':
        fixed_acidity = float(request.POST.get('fixed_acidity'))
        volatile_acidity = float(request.POST.get('volatile_acidity'))
        citric_acid = float(request.POST.get('citric_acid'))
        residual_sugar = float(request.POST.get('residual_sugar'))
        chlorides = float(request.POST.get('chlorides'))
        free_sulfur_dioxide = float(request.POST.get('free_sulfur_dioxide'))
        total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide'))
        density = float(request.POST.get('density'))
        pH = float(request.POST.get('pH'))
        sulphates = float(request.POST.get('sulphates'))
        alcohol = float(request.POST.get('alcohol'))

        model_learning = joblib.load(
            r'F:\Django_Project\django-wine\backend\app\model\model_wine.pkl')
        sample_data = [
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol
        ]

        manipulate_array = np.array(sample_data).reshape(1, -1)
        result = model_learning.predict(manipulate_array)
        temp = "Bad" if result == [0] else "Good"
        classification = f'%s quality' % temp
        WineClassification.objects.create(fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid,
                                          residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur_dioxide=free_sulfur_dioxide, total_sulfur_dioxide=total_sulfur_dioxide, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol, classification=classification)
        content = {
            'classification': classification,
            'fixed_acidity': fixed_acidity,
            'volatile_acidity': volatile_acidity,
            'citric_acid': citric_acid,
            'residual_sugar': residual_sugar,
            'chlorides': chlorides,
            'free_sulfur_dioxide': free_sulfur_dioxide,
            'total_sulfur_dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol
        }
        return JsonResponse(content, safe=False)


def data_wine(request):
    query = WineClassification.objects.filter().order_by('-date_created')
    return render(request, 'page/data.html', {'query': query})
