from flask import Flask, render_template, jsonify
import requests

app=Flask(__name__)

services={
    'server_pi':'http://10.0.0.201/admin/login', 
    'server_hp':'https://10.0.0.202:8006/',
    'vm_ubuntu':'http://10.0.0.203'
}

def health_checker(service):
    ip=services.get(service)
    try:
        response=requests.get(ip, verify=False, timeout=5) 
        status=response.status_code
        print('Service: '+ service +' Status: '+ str(status))
        if status==200:
            print(service+' UP')
            return 'UP'
        else:
            print(service+' DOWN')
            return f'DOWN ({status})'
    except requests.exceptions.RequestException:
        return 'Offline'
    
@app.route('/')
def dashboard():
    #status_pi=health_checker('server_pi')
    #status_hp=health_checker('server_hp')
    #status_ubuntu=health_checker('vm_ubuntu')

    return render_template("index.html")

@app.route('/status')
    #the API
def status():
    #created dictionary called "statuses", looping through services, copying key and values over to statuses   
    statuses={}
    for name in services:
        print('Checking status of '+name)
        statuses[name]=health_checker(name)
    return jsonify(statuses)


if __name__=='__main__':
    #can be accessed from server it's running from, port 5000
    app.run(debug=True, host='0.0.0.0', port=5000) 

























































