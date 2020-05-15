from flask import Flask
from flask import request
from Openshift import openshift_info
from flask.json import jsonify
import signal
import os
import sys

app = Flask(__name__)

openshift_object = openshift_info.Client()


@app.route('/health')
def health():
    return "OK"


@app.route('/pods')
def main():
    pods = openshift_object.get_pods()
    me = openshift_object.get_self()
    routes = openshift_object.get_routes()
    services = openshift_object.get_services()

    return jsonify({
            "pods": pods,
            "me": me,
            "routes": routes,
            "services": services})


@app.route('/pull_data/pods/<status>/<time>')
def pull_from_object_store(time, status):
    """
    flask endpoint to pull the data from object store
    """
    filename = 'pods_' + status+'_'  + time + '.csv'
    filepath = '/tmp/SSMT/OpenShift/' + filename 
    os.makedirs('/tmp/SSMT/OpenShift', exist_ok=True)
    if(helper.file_exists(filepath)):
        return helper.convert_csv_to_json(filepath)  
    else:
        interface_pull.interface_pull(filename)
        return helper.convert_csv_to_json(filepath)
  
def signal_term_handler(signal, frame):
    app.logger.warn('got SIGTERM')
    sys.exit(0)

 
if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_term_handler)

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
