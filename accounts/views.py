from django.shortcuts import render, redirect


def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        if username:

            request.session[
                "username"
            ] = username

            return redirect(
                "/dashboard/"
            )

    return render(
        request,
        "login.html"
    )
