from django.core.management.base import BaseCommand, CommandError
from django.template import loader

from events.models import Event
from events.models import Session
from invs.models import Invitation
from invs.models import InvitationType
from invs.models import InvUsedInSession
from tickets.models import Ticket


class Command(BaseCommand):

    def handle(self, *args, **options):
        ev = Event.objects.filter(slug='sicab')
        template = loader.get_template('dashboard/access.html')

        res = {
            "labels": [],
            "datasets": []
        }

        # Create labels and dataset
        sessions = Session.objects.filter(space__event=ev).order_by('start')

        dlabels = []
        dused = []
        dtotal = []
        for session in sessions:
            tickets = Ticket.objects.filter(session=session, confirmed=True)
            used_tic = tickets.filter(used=True).count()

            invs_type = InvitationType.objects.filter(sessions__in=[session])
            invs = Invitation.objects.filter(type__in=invs_type)
            used_inv = InvUsedInSession.objects.filter(inv__in=invs, session=session).count()

            dlabels.append(session.space.slug + " " + session.slug + " tickets")
            dlabels.append(session.space.slug + " " + session.slug + " inv")
            dused.append(used_tic)
            dused.append(used_inv)
            dtotal.append(len(tickets) - used_tic)
            dtotal.append(len(invs) - used_inv)

        res['labels'] = dlabels

        dataset = {}
        dataset['hoverBackgroundColor'] = 'rgba(0,255,0,1)'
        dataset['backgroundColor'] = 'rgba(0,255,0,0.7)'
        dataset['data'] = dused
        dataset['label'] = 'usados'
        res['datasets'].append(dataset)

        dataset = {}
        dataset['hoverBackgroundColor'] = 'rgba(255,0,0,1)'
        dataset['backgroundColor'] = 'rgba(255,0,0,0.7)'
        dataset['data'] = dtotal
        dataset['label'] = 'pendientes'
        res['datasets'].append(dataset)
        return template.render({'data': res})
