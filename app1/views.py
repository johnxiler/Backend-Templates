from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import CourseEvaluation
from .forms import CourseEvaluationForm
from django.shortcuts import render
from .forms import SurveyRatingForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import SurveyRating


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

# Create your views here.


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('survey_rating_list')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


class SurveyRatingListView(ListView):
    model = SurveyRating
    template_name = 'survey_rating_list.html'
    context_object_name = 'survey_ratings'


class SurveyRatingCreateView(CreateView):
    model = SurveyRating
    fields = ['course_objectives', 'delivering_material', 'engaging_students', 'responding_questions', 'providing_feedback',
              'inclusive_environment', 'using_technology', 'promoting_critical_thinking', 'challenging_students', 'overall_satisfaction']
    template_name = 'survey_rating_form.html'
    success_url = reverse_lazy('survey_rating_list')


class SurveyRatingUpdateView(UpdateView):
    model = SurveyRating
    fields = ['course_objectives', 'delivering_material', 'engaging_students', 'responding_questions', 'providing_feedback',
              'inclusive_environment', 'using_technology', 'promoting_critical_thinking', 'challenging_students', 'overall_satisfaction']
    template_name = 'survey_rating_form.html'
    success_url = reverse_lazy('survey_rating_list')


class SurveyRatingDeleteView(DeleteView):
    model = SurveyRating
    template_name = 'survey_rating_confirm_delete.html'
    success_url = reverse_lazy('survey_rating_list')


def survey_rating(request):
    if request.method == 'POST':
        form = SurveyRatingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SurveyRatingForm()
    return render(request, 'survey_rating.html', {'form': form})


def evaluation(request):
    if request.method == 'POST':
        form = CourseEvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evaluation_list')
    else:
        form = CourseEvaluationForm()
    return render(request, 'evaluation.html', {'form': form})


def edit_evaluation(request, pk):
    template_name = 'evaluation.html'
    success_url = reverse_lazy('evaluation_list')
    evaluation = get_object_or_404(CourseEvaluation, pk=pk)
    if request.method == 'POST':
        form = CourseEvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('evaluation_list')
    else:
        form = CourseEvaluationForm(instance=evaluation)
    return render(request, template_name, {'form': form})


def delete_evaluation(request, pk):
    template_name = 'delete_evaluation.html'
    success_url = reverse_lazy('survey_rating_list')
    evaluation = get_object_or_404(CourseEvaluation, pk=pk)
    if request.method == 'POST':
        evaluation.delete()
        return redirect('evaluation_list')
    return render(request, template_name, {'evaluation_list': evaluation})


def evaluation_list(request):
    evaluations = CourseEvaluation.objects.all()
    return render(request, 'evaluation_list.html', {'evaluations': evaluations})
