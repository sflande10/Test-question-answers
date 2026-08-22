import requests

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    return response.json()

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/1"
    data = fetch_api_data(url)
    if data:
        print("Request successful!")
        print(f"Name: {data.get('name')}")
        print(f"Email: {data.get('email')}")
        print(f"City: {data.get('address', {}).get('city')}")
    else:
        print("Could not retrieve data.")