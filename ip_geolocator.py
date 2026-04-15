import requests

def get_ip_info(ip=""):
    if ip == "":
        url = "https://ipinfo.io/json"
    else:
        url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        print(f"IP Address: {data.get('ip')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country')}")
        print(f"Location: {data.get('loc')}")
        print(f"ISP/Org: {data.get('org')}")
    except Exception as e:
        print("Error:", e)

ip_to_track = input("Enter IP Address: ")
get_ip_info(ip_to_track.strip())
