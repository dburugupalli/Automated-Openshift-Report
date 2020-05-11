# Automated-Openshift-Report


Automated-Openshift-Report is python flask web application to get all the OpenShift resource metrics.

## Requirements

Should have python virtual environment [setup](https://www.tutorialspoint.com/python-virtual-environment)

##### Local Environment 

Should have Minishift cluster up and running


Should be able to access OpenShift cluster using openshift-client 
```
example: oc get pods
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
```

## 
## Environment Variables



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
