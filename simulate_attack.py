import time
import requests

URL = "http://127.0.0.1:8000/api/cinder/create-volume"


def send_request(username, volume_name, size):
    payload = {"user": username, "volume_name": volume_name, "size": size}
    try:
        response = requests.post(URL, json=payload)
        print(f"User: {username:15} | Status Code: {response.status_code} | Response: {response.json().get('status')}")
    except Exception as e:
        print(f"Error connecting to server: {e}")


if __name__ == "__main__":
    print("🚀 Starting Cloud API Security Simulation...\n")

    # 1. Simulate a legitimate user request (Allowed by OCL)
    print("--- Simulating Normal Behavior ---")
    send_request("student_user", "prod-db-volume", 20)
    time.sleep(1)

    # 2. Simulate a malicious user exploiting resource exhaustion limits (Blocked by OCL)
    print("\n--- Simulating Malicious Resource Exhaustion Attack ---")
    for i in range(1, 8):
        send_request("malicious_user", f"attack-vol-{i}", 100)
        time.sleep(0.2)  # High frequency burst attack

    print("\n✅ Simulation Complete. Logs successfully captured!")