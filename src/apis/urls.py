from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login/", views.login, ["POST"], "login url"),
    ("/register/", views.register, ["POST"], "register url"),
    ("/users/", views.users, ["GET"], "protected users list url"),
]

other_urls = []

all_urls = api_urls + other_urls
