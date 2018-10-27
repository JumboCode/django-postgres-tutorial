from django.db import models

# Create your models here.

from django.db import models

#
# Create your models for the Tufts Bobsledding Society here.
#

# Things to Consider when making models:

#  Inherent data constrictions, validation:
# (eg. max_length=33 makes sure no sled with a name longer than 33 characters makes it into the database)

#  Flexibility:
#  Better to keep a running list of sleds then having to go through every SledMember to get a list of unique sleds.


# Data Representation/Abstraction of a Team in the database

class Sled(models.Model):
    name = models.CharField(max_length=33)
    victories = models.IntegerField(default=0)
    defeats = models.IntegerField(default=0)

    # Special method that lets django know how a object should be primarily identified for representation purposes
    def __str__(self):
        return self.name

# Data Representation/Abstraction of a  in the database


class TeamMember(models.Model):

    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=12)

    sled = models.ForeignKey("Sled", null=True, on_delete=models.SET_NULL)
    captain = models.BooleanField(default=False, null=False)

    def full_name(self):
        return self.first_name + " " + self.last_name


# Add a Representation for a Donor and a Donation Here...

