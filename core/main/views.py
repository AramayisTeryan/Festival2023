from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Header, Menu, Home, HomeVideo, About, Artist, ArtistFoto, ArtistFotoRight, Event, Plan, PriceList, Contact, Live, Footer,TicketHeader, TicketMenu, Ticket, TicketLive, TicketFoot

# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        header = Header.objects.all()
        menu = Menu.objects.all()
        home = Home.objects.all()
        homevideo = HomeVideo.objects.all()
        about = About.objects.all()
        artist  = Artist.objects.all()
        artistfoto = ArtistFoto.objects.all()
        artistfotoright = ArtistFotoRight.objects.all()
        event = Event.objects.all()
        plan = Plan.objects.all()
        pricelist = PriceList.objects.all()
        contact = Contact.objects.all()
        live = Live.objects.all()
        footer = Footer.objects.all()
        return render(request, self.template_name,  {'header':header, 'menu':menu, 'home':home, 'homevideo':homevideo, 'about':about, 'artist':artist, 'artistfoto':artistfoto, 'artistfotoright':artistfotoright, 'event':event, 'plan':plan, 'pricelist':pricelist, 'contact':contact, 'live':live, 'footer':footer})


class TicketListView(ListView):
    template_name = 'ticket.html'

    def get(self, request):
        ticketheader = TicketHeader.objects.all()
        ticketmenu = TicketMenu.objects.all()
        ticket = Ticket.objects.all()
        ticketlive = TicketLive.objects.all()
        ticketfoot = TicketFoot.objects.all()
        return render(request, self.template_name, {'ticketheader':ticketheader, 'ticketmenu':ticketmenu, 'ticket':ticket, 'ticketlive':ticketlive, 'ticketfoot':ticketfoot})

