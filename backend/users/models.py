from uuid import uuid4
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from events.models import Event
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
  DEPARTMENTS = (
    ("COMP", "Computer"),
    ("IT", "IT"),
    ("EXTC", "EXTC"),
    ("MECH", "Mechanical"),
    ("ELEC", "Electrical"),
    ("OTHER", "Other")
  )
  roll_no = models.IntegerField(_("Roll Number"),unique=True, blank=False)
  email = models.EmailField(_('email address'),unique=True, max_length=254)
  name = models.CharField(_('Name'), max_length=256,blank=True, null=True)
  avatar = models.CharField(_("Avatar Image"), max_length=256, blank=True ,null=True)
  department = models.CharField(_('Department'),max_length=10,blank=True, null=True, choices=DEPARTMENTS)
  semester = models.SmallIntegerField(_("Semester"),blank=True, null=True)
  phone_no = models.CharField(_("Phone Number"),blank=True,  max_length=10)
  is_phone_no_verified = models.BooleanField(_("Is Phone Number Verified"), default=False)
  
  money_owed = models.DecimalField(_("Money Owed"),decimal_places=2,max_digits=10, default=0.00)
  has_filled_profile = models.BooleanField(_("Has Filled Profile"), default=False)
  criteria = models.TextField(_("Criteria JSON"), default='{"1": false, "2": false, "3": false}')
  cart = models.TextField(_("Cart JSON"), default="[]")

  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'roll_no'
  REQUIRED_FIELDS = ['email',]

  objects = UserManager()

  def __str__(self) -> str:
      return f"{self.roll_no}#{self.email}"


class Team(models.Model):
  team_code = models.CharField(_("Team Code"), default=uuid4,max_length=36, unique=True)
  team_name = models.CharField(_("Team Name"), max_length=256,blank=False)
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants")
  members = models.ManyToManyField(User, related_name='teams')
  transaction_id = models.CharField(_("Transactions Id"), max_length=36, blank=True, null=True)
  is_paid = models.BooleanField(_("Is Paid"), default=False)
  is_verified = models.BooleanField(_("Is Verified"), default=False)


  def __str__(self) -> str:
    return f"{self.team_name}#{self.team_code}"


# ADD POST_SAVE after getting verified and increment event seats
@receiver(post_save, sender=Team)
def update_seats(sender, instance, created, **kwargs):
  print("post save bruh")
  if not created:
    if instance.is_paid and instance.is_verified:
      event = instance.event
      print(event.seats)
      event.seats += 1
      print(event.seats)
      event.save()