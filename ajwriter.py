import platform,socket,time,speedtest,sys
import requests,json

url = "http://192.168.1.201/admin/api.php?summaryRaw"
r = requests.get(url)
parsed_json = json.loads(r.text)
adsblocked = parsed_json['ads_blocked_today']

st = speedtest.Speedtest()
with open('inkytxt.txt', 'w+') as f:
    f.write(time.ctime()+"\n")
    f.write("ID: " + socket.gethostname() + ".connect\n")
    f.write("OS: " + platform.release() + " " + platform.version()+"\n")
    f.write("DL: " + str((st.download()/1024)/1024)[:5] + " MBps\n")
    f.write("AD: Blocked today " + str(adsblocked))
    f.close()
