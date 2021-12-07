""" A LocationController Module """

from masonite.controllers import Controller
from app.Location import Location
from masonite.request import Request


class LocationController(Controller):
    """Class Docstring Description
    """
    
    def __init__(self, request:Request):
      self.request=request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", LocationController)
        """
        id= self.request.param("id")
        return Location.find(id)

        

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", LocationController)
        """
        return Location.all()

        

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", LocationController)
        """
        name = self.request.input("name")
        description=self.request.input("description")
        image=self.request.input("image")
        visited=self.request.input("visited")
        location = Location.create({"name":name,"description":description,"image":image,"visited":visited})
        
        return location

        

    def update(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", LocationController)
        """
        id=self.request.param("id")
        name = self.request.input("name")
        description=self.request.input("description")
        image=self.request.input("image")
        visited=self.request.input("visited")
        location = Location.where("id",id).update({"name":name,"description":description,"image":image,"visited":visited})
        return location
        
        

        

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", LocationController)
        """
        id = self.request.param("id")
        location= Location.where("id",id).get()
        Location.where("id",id).delete()
        return location

        