import os
from kubernetes import client, config
from openshift.dynamic import DynamicClient


class Client(object):
    def __init__(self):
    # to run inside the openshift cluster
        if "OPENSHIFT_BUILD_NAME" in os.environ:
            service_account_path = '/var/run/secrets/kubernetes.io/serviceaccount'

            with open(os.path.join(service_account_path, 'namespace')) as fp:
                self.namespace = fp.read().strip()
            config.load_incluster_config()

            configuration = client.Configuration()
            configuration.verify_ssl = False

            self.oapi_client = DynamicClient(
                client.ApiClient(configuration=configuration)
            )
    # to run in our local environment as well. 
        else:
            config.load_kube_config()
            configuration = client.Configuration()
            configuration.verify_ssl = False
            self.namespace = 'default'
            self.oapi_client = DynamicClient(
                client.ApiClient(configuration=configuration)
            )


    def get_pods(self):
        pods_api = self.oapi_client.resources.get(kind='Pod', api_version='v1')
        pod_list = pods_api.get(namespace=self.namespace)
        return self._get_running_pods(pod_list)

    def get_services(self):
        return []

    def get_self(self):
        return os.environ.get("HOSTNAME")

    def get_routes(self):
        routes_api = self.oapi_client.resources.get(
                                kind='Route',
                                api_version='route.openshift.io/v1')
        route_list = routes_api.get(namespace=self.namespace)

        return self._get_names(route_list)

    def _get_names(self, resources):
        return [resource.metadata.name
                for resource in resources.items]

    def _get_running_pods(self, pods):
        return [pod.metadata.name
                for pod in pods.items
                if pod.status.phase == "Running"]

    def _get_failed_pods(self, pods):
        return [pod.metadata.name
                for pod in pods.items
                if pod.status.phase == "Failed"]

    def _get_succeeded_pods(self, pods):
        return [pod.metadata.name
                for pod in pods.items
                if pod.status.phase == "Succeeded"]

