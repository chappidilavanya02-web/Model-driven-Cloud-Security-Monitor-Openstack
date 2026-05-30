from django.shortcuts import render
from .policy_engine import validate_policy
from .models import SecurityLog
from .openstack_service import get_users


def home(request):
    if not request.session.get(
            "username"
    ):
        from django.shortcuts import redirect

        return redirect("/")

    username = request.POST.get(
        'username',
        ''
    )

    role = request.POST.get(
        'role',
        ''
    )

    action = request.POST.get(
        'action',
        ''
    )

    result = ""
    color = "green"

    if username:

        allowed, result = validate_policy(
            username,
            role,
            action
        )

        if allowed:

            color = "green"

            SecurityLog.objects.create(

                username=username,

                role=role,

                action=action,

                status="ALLOWED"

            )

        else:

            color = "red"

            SecurityLog.objects.create(

                username=username,

                role=role,

                action=action,

                status="BLOCKED"

            )

    all_logs = SecurityLog.objects.all()

    logs = all_logs.order_by(
        '-timestamp'
    )[:10]
    suspicious_users = {}

    blocked_logs = SecurityLog.objects.filter(
        status="BLOCKED"
    )

    for log in blocked_logs:
        suspicious_users[log.username] = (

                suspicious_users.get(
                    log.username,
                    0
                ) + 1

        )

    blocked_count = all_logs.filter(
        status="BLOCKED"
    ).count()

    total_requests = all_logs.count()

    allowed_count = total_requests - blocked_count

    cloud_users = get_users()
    context = {
        "blocked_count": blocked_count,

        "allowed_count": allowed_count,

        "total_requests": total_requests,

        "username": username,

        "role": role,

        "action": action,

        "result": result,

        "color": color,

        "logs": logs,
        "suspicious_users": suspicious_users,
        "cloud_users": cloud_users,

    }

    return render(

        request,

        "home.html",

        context

    )