#Here are functions for displaying templates and forms on the site

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from hotel.forms import PersonForm, RoomForm, RoomFormCreate
from hotel.models import Person, Hotel

from django.contrib.auth import views as auth_views, logout
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from .forms import CustomLoginForm


def is_admin(user):
    return user.is_active and user.is_staff and user.is_superuser


def main_menu(request: HttpRequest):
    free_rooms = len([i for i in Hotel.objects.all() if not i.room.all()])
    not_free_rooms = len([i for i in Hotel.objects.all() if i.room.all()])
    context = {
        'persons': Person.objects.all(),
        'hotels': Hotel.objects.all(),
        'free_rooms': free_rooms,
        'not_free_rooms': not_free_rooms,
    }
    return render(request, 'hotel/main_menu.html', context=context)


class LogoutAndRedirectView(View):
    def get(self, request):
        return self.logout_and_redirect(request)

    def post(self, request):
        return self.logout_and_redirect(request)

    def logout_and_redirect(self, request):
        next_page = request.GET.get('next', resolve_url('hotel:main_menu'))
        logout(request)
        return redirect(next_page)


class LoginView(auth_views.LoginView):
    form_class = CustomLoginForm
    template_name = 'hotel/login.html'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class create_new_person(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": PersonForm(),
            "groups": Person.objects.prefetch_related('permissions').all()
        }
        return render(request, 'hotel/person_create.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('hotel:person_list')


class PersonListView(ListView):
    template_name = 'hotel/person_view.html'
    queryset = Person.objects.all
    context_object_name = "persons"


class PersonDetailsView(DetailView):
    template_name = 'hotel/person_detail.html'
    model = Person
    context_object_name = 'person'


@method_decorator(user_passes_test(is_admin), name='dispatch')
class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy("hotel:person_list")


@method_decorator(user_passes_test(is_admin), name='dispatch')
class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            'hotel:person_detail',
            kwargs={'pk': self.object.pk}
        )


@user_passes_test(is_admin)
def HotelList(request):
    if request.method == 'POST':
        form = RoomFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel:hotel_list')
    else:
        form = RoomFormCreate()

    return render(request, 'hotel/hotel_create.html', {'form': form})


class HotelListView(ListView):
    template_name = 'hotel/hotel_view.html'
    queryset = Hotel.objects.all
    context_object_name = "rooms"


@user_passes_test(is_admin)
def HotelUpdate(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel:hotel_detail', pk=pk)
    else:
        form = RoomForm(instance=hotel)
    context = {'form': form, 'hotel': hotel}
    return render(request, 'hotel/hotel_update_form.html', context=context)



class HotelDetailsView(DetailView):
    template_name = 'hotel/hotel_detail.html'
    model = Hotel
    context_object_name = 'room'

