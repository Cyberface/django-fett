from __future__ import unicode_literals

from django.db import models

# Each class here is basically a database table. Each variable is a table column,
# and then a datatype and maybe some further attributes if you like, like max_length
# and so on. If you wish to reference these objects and get something back besides
# that it is a Post or Category object, then you need to define the __str__ method.
# If you are using Python 2.7, shame on you!... but you need to do __unicode__ instead of __str__.
# This models.py file is straight forward, especially once you know all of the
# possible datatypes and such. Check out the Django Docs for the Model Fields, you have a lot of options.

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
    # def __unicode__(self):
        return self.title
