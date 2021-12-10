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
    ],prefix="/locations", name="locations"),
    
    RouteGroup([
      Post("/login","AuthController@login").name("login"),
      Post("/signup","AuthController@signup").name("signup"),
      Post("logout","AuthController@logout").name("logout"),
      Get("/all","AuthController@users").name("all"),
      
    ],prefix="/auth", name="auth"),
    Post("/login","AuthController@login").name("login"),
    
    RouteGroup([
      Post("/","LocationController@create_post").name("create"),
      Get("/","LocationController@all_posts").name("all"),
      Get("/@id","LocationController@show_post").name("show"),
      Put("/@id", "LocationController@update_post").name("update"),
      Delete("/@id", "LocationController@destroy").name("destroy"),
      Get("/allposts","LocationController@all_posts").name("allposts")
    ],prefix="/posts",name="posts",middleware=["auth"])
    
  ]
