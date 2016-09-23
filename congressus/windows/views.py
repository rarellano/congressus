import datetime
from django.utils import timezone
from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.urlresolvers import reverse

from .models import TicketWindow
from .models import TicketWindowSale
from tickets.views import MultiPurchaseView
from tickets.views import get_ticket_or_404
from events.models import Event
from tickets.forms import MPRegisterForm
from tickets.utils import get_ticket_format

from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


class WindowLogin(TemplateView):
    template_name = 'windows/login.html'

    def get_context_data(self, *args, **kwargs):
        ev = self.kwargs.get('ev')
        w = self.kwargs.get('w')
        w = get_object_or_404(TicketWindow, event__slug=ev, slug=w)
        ctx = super(WindowLogin, self).get_context_data(*args, **kwargs)
        ctx['window'] = w
        return ctx

    def post(self, request, ev=None, w=None):
        w = get_object_or_404(TicketWindow, event__slug=ev, slug=w)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            have_access = user.groups.filter(name='window').count()
            if user.is_active and have_access:
                login(request, user)
                return redirect('window_multipurchase', ev=w.event.slug, w=w.slug)
            else:
                messages.error(request, _("This user can't access in this ticket window"))
        else:
            messages.error(request, _("Invalid username or password"))

        return render(request, self.template_name,
                      self.get_context_data(ev=ev, w=w.slug))
window_login = WindowLogin.as_view()


class WindowMultiPurchase(UserPassesTestMixin, MultiPurchaseView):
    template_name = 'windows/multipurchase.html'
    DEFAULT_PF = 'thermal'

    def get_window(self):
        ev = self.kwargs['ev']
        w = self.kwargs['w']
        w = get_object_or_404(TicketWindow, event__slug=ev, slug=w)
        return w

    def get_discounts(self):
        ev = self.kwargs['ev']
        ev = get_object_or_404(Event, slug=ev)
        return ev.discounts.all()

    def test_func(self):
        u = self.request.user
        have_access = u.groups.filter(name='window').count()
        return u.is_authenticated() and have_access

    def get_login_url(self):
        return reverse('window_login', kwargs=self.kwargs)

    def get_context_data(self, *args, **kwargs):
        ctx = super(WindowMultiPurchase, self).get_context_data(*args, **kwargs)
        w = self.get_window()
        ctx['window'] = w
        ctx['subsum'] = True
        ctx['print_formats'] = settings.PRINT_FORMATS
        ctx['default_pf'] = self.DEFAULT_PF
        ctx['discounts'] = self.get_discounts()
        return ctx

    def post(self, request, *args, **kwargs):
        w = self.get_window()

        ids = [(i[len('number_'):], request.POST[i]) for i in request.POST if i.startswith('number_')]
        seats = [(i[len('seats_'):], request.POST[i].split(',')) for i in request.POST if i.startswith('seats_')]
        print_format = request.POST.get('print-format', self.DEFAULT_PF)

        data = request.POST.copy()
        data['email'] = settings.FROM_EMAIL

        form = MPRegisterForm(data,
                              event=w.event, ids=ids, seats=seats,
                              client=request.session.get('client', ''))

        keys = list(form.fields.keys())
        for k in keys:
            # email is required
            if k == 'email':
                continue
            # removing not required fields
            form.fields.pop(k)

        if form.is_valid():
            mp = form.save(commit=False)
            mp.confirm()
            for tk in mp.tickets.all():
                tk.sold_in_window = True
                tk.price = tk.get_window_price()
                tk.save()

            price = float(data.get('price', 0))
            payed = data.get('payed', 0)
            if payed:
                payed = float(payed)
            else:
                payed = 0

            change = float(data.get('change', 0))
            payment = data.get('payment', 'cash')
            sale = TicketWindowSale(purchase=mp, window=w, user=request.user,
                                    price=price, payed=payed,
                                    change=change, payment=payment)
            sale.save()

            response = get_ticket_format(mp, pf=print_format)
            return response

        ctx = self.get_context_data()
        ctx['form'] = form

        return render(request, self.template_name, ctx)
# csrf_exempt because we use the same multipurchase form several times, we
# use target="_blank" in the form to return the PDF
window_multipurchase = csrf_exempt(WindowMultiPurchase.as_view())


class WindowLogout(View):
    def get(self, request, ev, w):
        auth_logout(request)
        return redirect('window_multipurchase', ev=ev, w=w)
window_logout = WindowLogout.as_view()


class WindowList(UserPassesTestMixin, TemplateView):
    template_name = 'windows/list.html'

    def test_func(self):
        u = self.request.user
        return u.is_authenticated() and u.is_superuser

    def get_context_data(self, *args, **kwargs):
        ev = self.kwargs.get('ev')
        ev = get_object_or_404(Event, slug=ev)
        ctx = super(WindowList, self).get_context_data(*args, **kwargs)
        ctx['windows'] = ev.windows.all()
        ctx['ev'] = ev

        ctx['date'] = timezone.now()

        d = self.request.GET.get('date', '')
        if d:
            date = datetime.datetime(*map(int, d.split('-')))
            ctx['date'] = date

        days = []
        d = timezone.now() - datetime.timedelta(10)
        d1 = timezone.now() + datetime.timedelta(10)
        while d < d1:
            days.append(d)
            d = d + datetime.timedelta(1)
        ctx['days'] = days
        ctx['today'] = timezone.now()
        ctx['menuitem'] = 'windows'

        return ctx
window_list = WindowList.as_view()
