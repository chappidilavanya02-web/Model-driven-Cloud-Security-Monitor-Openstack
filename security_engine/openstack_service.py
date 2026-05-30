import requests


def get_users():

    try:

        print("CALLING API...")

        response = requests.get(
            "http://172.18.130.132:5000/users",
            timeout=5
        )

        print(
            "STATUS:",
            response.status_code
        )

        print(
            "DATA:",
            response.text
        )

        return response.json()

    except Exception as e:

        print(
            "ERROR:",
            e
        )

        return []