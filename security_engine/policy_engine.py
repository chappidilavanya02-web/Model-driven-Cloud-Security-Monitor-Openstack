restricted_actions = [
    "create_user",
    "delete_user",
    "assign_role"
]

def validate_policy(username, role, action):

    if role == "member" and action in restricted_actions:

        return False, "ACCESS DENIED: POLICY VIOLATION"

    return True, "ACCESS GRANTED"