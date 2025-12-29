"""Test API endpoint using requests library (like frontend fetch)"""
import requests
import json

# Test the API endpoint like the frontend would
url = "http://localhost:8000/api/chat"
headers = {
    "Content-Type": "application/json",
    "Origin": "http://localhost:3001"  # Add origin header like browser would
}
payload = {
    "question": "What is humanoid robotics?"
}

print(f"Testing API endpoint: {url}")
print(f"Payload: {json.dumps(payload, indent=2)}")
print("\nSending request...")

try:
    response = requests.post(url, json=payload, headers=headers, timeout=30)

    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"\nResponse Body:")
    print(json.dumps(response.json(), indent=2))

    if response.status_code == 200:
        print("\n✅ SUCCESS! API is working!")
        data = response.json()
        print(f"\nAnswer preview: {data['answer'][:200]}...")
    else:
        print(f"\n❌ FAILED with status {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"\n❌ Request failed: {e}")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
