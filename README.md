# SSMT 

OpenShift on OpenStack Metering 

SSMT is python flask web application to get all the OpenShift resource metrics, push it onto the OpenStack Object Store. 


## Requirements

Should have python virtual environment [setup](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Installing Virtualenv

```bash
# MacOs and Linux
python3 -m pip install --user virtualenv
```

### Creating a Virtual Environment 

```bash
# MacOs and Linux
python3 -m venv env
```

### Activating Virtual Environment

```bash
source env/bin/activate
```

You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

```bash
On macOS and Linux:
which python
.../env/bin/python
```

##### Local Environment 

Should have Minishift cluster up and running


Should be able to access OpenShift cluster using openshift-client

```
example: oc get pods --all-namespaces (should not throw error) 
```

##### OpenShift Cluster

Should have OpenShift Account

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python dependencies.

```bash
pip3 install flask 
pip3 install kubernetes
pip3 install openshift
pip3 install crontabs
pip3 install boto
```

## 
## Environment Variables

```
# To configure object store
export access_key = <access_key>
export secret_key = <secret_key>
export end_point = <authentication endpoint> 
# To configure flask web application 
export host = <hostname> # if not provided, sets the default value
export port = <desired port to run the application> # if not provided, sets the default value
```

## 
## Usage

```python
python3 app.py # will start the flask web application 
python3 crontab.py # will query for the data at periodic intervals
```
Flask Web Application Overview

Try to access the web application URL using the following commands

Local Development

```bash
http://0.0.0.0:9000/push_to_object_store
# Purpose : Retrieve OpenShift Cluster resource metics and push it to OpenStack Object Store 
# Returns : A list of CSV files pushed to the OpenStack Object Store
http://0.0.0.0:8000/get_cumulative_information
# Purpose: Retrieve Cumulative infomation like OpenShift Nodes, Pods, PVC's, Projects etc.
# Returns: JSON Response with names of all Nodes, Pods, PVC's, PV's, Projects in an OpenShift cluster
http://0.0.0.0:8000/pull_data/pods/<status>/<time>
#Purpose: Pull the data from openstack object store when status and time is provided. 
#Returns: JSON Response with the contents of the Pods running and Failed.
#<status> represents the data runnning, failed. <time> represents the time 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
