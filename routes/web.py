"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
      Get("/","LocationController@index").name("index"),
      Get("/@id", "LocationController@show").name("show"),
      Post("/", "LocationController@create").name("create"),
      Put("/@id", "LocationController@update").name("update"),
      Delete("/@id", "LocationController@destroy").name("destroy"),
    ],prefix="/locations", name="locations")
]
