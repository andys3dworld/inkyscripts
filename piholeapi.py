import requests,json

url = "http://192.168.1.201/admin/api.php?summaryRaw"
r = requests.get(url)
parsed_json = json.loads(r.text)
adsblocked = parsed_json['ads_blocked_today']
print(adsblocked)
