from django.db import models

# Create your models here.

class Header(models.Model):
    name = models.CharField('Header name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'



class Menu(models.Model):
    name = models.CharField('Menu name', max_length=50)
    name1 = models.CharField('Menu name1', max_length=50)
    name2 = models.CharField('Menu name2', max_length=50)
    name3 = models.CharField('Menu name3', max_length=50)
    name4 = models.CharField('Menu name4', max_length=50)
    name5 = models.CharField('Menu name5', max_length=50)
    name6 = models.CharField('Menu name6', max_length=50)
    name7 = models.CharField('Menu name7', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'



class Home(models.Model):
    name = models.CharField('Home name', max_length=50)
    name1 = models.CharField('Home name1', max_length=50)
    name2 = models.CharField('Home name2', max_length=50)
    name3 = models.CharField('Home name3', max_length=50)
    name4 = models.CharField('Home name4', max_length=50)
    about = models.TextField('Home about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'



class HomeVideo(models.Model):
    video = models.FileField('HomeVideo video', upload_to='media')

    def __str_(self):
        return str(self.video)

    class Meta:
        verbose_name = 'HomeVideo'
        verbose_name_plural = 'HomeVideos'



class About(models.Model):
    name = models.CharField('About name', max_length=50)
    name1 = models.CharField('About name1', max_length=50)
    name2 = models.CharField('About name2', max_length=50)
    name3 = models.CharField('About name3', max_length=50)
    about = models.TextField('About about')
    about1 = models.TextField('About about1')
    about2 = models.TextField('About about2')
    about3 = models.TextField('About about3')
    img = models.ImageField('About image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'



class Artist(models.Model):
    name = models.CharField('Artist name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'



class ArtistFoto(models.Model):
    name = models.CharField('ArtistFoto name', max_length=50)
    name1 = models.CharField('ArtistFoto name1', max_length=50)
    name2 = models.CharField('ArtistFoto name2', max_length=50)
    name3 = models.CharField('ArtistFoto name3', max_length=50)
    about = models.TextField('ArtistFoto about')
    about1 = models.TextField('ArtistFoto about1')
    about2 = models.TextField('ArtistFoto about2')
    about3 = models.TextField('ArtistFoto about3')
    img = models.ImageField('ArtistFoto image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ArtistFoto'
        verbose_name_plural = 'ArtistFotos'



class ArtistFotoRight(models.Model):
    name = models.CharField('ArtistFotoRight name', max_length=50)
    name1 = models.CharField('ArtistFotoRight name1', max_length=50)
    name2 = models.CharField('ArtistFotoRight name2', max_length=50)
    name3 = models.CharField('ArtistFotoRight name3', max_length=50)
    about = models.TextField('ArtistFotoRight about')
    about1 = models.TextField('ArtistFotoRight about1')
    about2 = models.TextField('ArtistFotoRight about2')
    about3 = models.TextField('ArtistFotoRight about3')
    img = models.ImageField('ArtistFotoRight image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ArtistFotoRight'
        verbose_name_plural = 'ArtistFotoRights'



class Event(models.Model):
    name = models.CharField('Event name', max_length=50)
    name1 = models.CharField('Event name1', max_length=50, null=True)
    name2 = models.CharField('Event name2', max_length=50, null=True)
    name3 = models.CharField('Event name3', max_length=50, null=True)
    name4 = models.CharField('Event name4', max_length=50, null=True)
    name5 = models.CharField('Event name5', max_length=50, null=True)
    about = models.TextField('Event about', null=True)
    about1 = models.TextField('Event about1', null=True)
    about2 = models.TextField('Event about2', null=True)
    about3 = models.TextField('Event about3', null=True)
    about4 = models.TextField('Event about4', null=True)
    about5 = models.TextField('Event about5', null=True)
    about6 = models.TextField('Event about6', null=True)
    about7 = models.TextField('Event about7', null=True)
    about8 = models.TextField('Event about8', null=True)
    about9 = models.TextField('Event about9', null=True)
    about10 = models.TextField('Event about10', null=True)
    about11 = models.TextField('Event about11', null=True)
    about12 = models.TextField('Event about12', null=True)
    about13 = models.TextField('Event about13', null=True)
    about14 = models.TextField('Event about14', null=True)
    about15 = models.TextField('Event about15', null=True)
    about16 = models.TextField('Event about16', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'



class Plan(models.Model):
    name = models.CharField('Plan name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'



class PriceList(models.Model):
    name = models.CharField('PriceList name', max_length=50)
    name1 = models.CharField('PriceList name1', max_length=50)
    # name2 = models.CharField('PriceList name2', max_length=50, blank=True)
    name3 = models.CharField('PriceList name3', max_length=50, blank=True)
    name4 = models.CharField('PriceList name4', max_length=50)
    about = models.TextField('PriceList about')
    about1 = models.TextField('PriceList about1')
    about2 = models.TextField('PriceList about2')
    about3 = models.TextField('PriceList about3')
    about4 = models.TextField('PriceList about4')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PriceList'
        verbose_name_plural = 'PriceLists'



class Contact(models.Model):
    name = models.CharField('Contact name', max_length=50)
    name1 = models.CharField('Contact name1', max_length=50)
    name2 = models.CharField('Contact name2', max_length=50)
    name3 = models.CharField('Contact name3', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'



class Live(models.Model):
    name = models.CharField('Live name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Live'
        verbose_name_plural = 'Lives'



class Footer(models.Model):
    name = models.CharField('Footer name', max_length=50)
    name1 = models.CharField('Footer name1', max_length=50)
    name2 = models.CharField('Footer name2', max_length=50)
    name3 = models.CharField('Footer name3', max_length=50)
    about = models.TextField('Footer about')
    about1 = models.TextField('Footer about1')
    about2 = models.TextField('Footer about2')
    about3 = models.TextField('Footer about3')
    about4 = models.TextField('Footer about4')
    about5 = models.TextField('Footer about5')
    about6 = models.TextField('Footer about6')
    about7 = models.TextField('Footer about7')
    about8 = models.TextField('Footer about8')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'



class TicketHeader(models.Model):
    name = models.CharField('TicketHeader name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TicketHeader'
        verbose_name_plural = 'TicketHeaders'



class TicketMenu(models.Model):
    name = models.CharField('TicketMenu name', max_length=50)
    name1 = models.CharField('TicketMenu name1', max_length=50)
    name2 = models.CharField('TicketMenu name2', max_length=50)
    name3 = models.CharField('TicketMenu name3', max_length=50)
    name4 = models.CharField('TicketMenu name4', max_length=50)
    name5 = models.CharField('TicketMenu name5', max_length=50)
    name6 = models.CharField('TicketMenu name6', max_length=50)
    name7 = models.CharField('TicketMenu name7', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TicketMenu'
        verbose_name_plural = 'TicketMenues'



class Ticket(models.Model):
    name = models.CharField('Ticket name', max_length=50)
    name1 = models.CharField('Ticket name1', max_length=50)
    name2 = models.CharField('Ticket name2', max_length=50)
    about = models.TextField('Ticket about')
    about1 = models.TextField('Ticket about1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'



class TicketLive(models.Model):
    name = models.CharField('TicketLive name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TicketLive'
        verbose_name_plural = 'TicketLives'



class TicketFoot(models.Model):
    name = models.CharField('TicketFoot name', max_length=50)
    name1 = models.CharField('TicketFoot name1', max_length=50)
    name2 = models.CharField('TicketFoot name2', max_length=50)
    name3 = models.CharField('TicketFoot name3', max_length=50)
    about = models.TextField('TicketFoot about')
    about1 = models.TextField('TicketFoot about1')
    about2 = models.TextField('TicketFoot about2')
    about3 = models.TextField('TicketFoot about3')
    about4 = models.TextField('TicketFoot about4')
    about5 = models.TextField('TicketFoot about5')
    about6 = models.TextField('TicketFoot about6')
    about7 = models.TextField('TicketFoot about7')
    about8 = models.TextField('TicketFoot about8')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TicketFoot'
        verbose_name_plural = 'TicketFoots'








