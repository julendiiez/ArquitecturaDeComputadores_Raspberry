import requests

res = requests.get('http://192.168.0.31:5000/api/endpoint')
                    
print("H")
if res.ok:
    print(res.json())