"""User Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class User(Model):
    """User Model."""

    __fillable__ = ["username", "password"]

    __auth__ = "username"
    
    @has_many("id","user_id")
    def locations(self):
      from app.Location import Location
      return Location
