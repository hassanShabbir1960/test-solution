class HealthCheck:
    """
    A class for performing health checks on services using Elasticsearch data.

    Attributes:
        es (Elasticsearch): An instance of the Elasticsearch client.
        index (str): Name of the Elasticsearch index for storing service status data.
    """

    def __init__(self, es_config):
        """
        Initializes a HealthCheck instance with an Elasticsearch configuration.

        Args:
            es_config (ElasticSearchConfig): An instance of ElasticSearchConfig containing
                Elasticsearch connection details and index information.
        """
        self.es = es_config.es
        self.index = es_config.index

    def get_all_status(self):
        """
        Retrieves the status of all services from the Elasticsearch index.

        Returns:
            dict: A dictionary containing service names as keys and their respective
                statuses as values. For example: {"Service A": "OK", "Service B": "Error"}
        """
        body = {"size": 1000, "query": {"match_all": {}}}
        res = self.es.search(index=self.index, body=body)
        statuses = {}
        for hit in res['hits']['hits']:
            # Using 'application_name' and 'application_status' as keys
            statuses[hit['_source']['application_name']] = hit['_source']['application_status']
        return statuses


    def get_service_status(self, service_name):
        """
        Retrieves the status of a specific service from the Elasticsearch index.

        Args:
            service_name (str): The name of the service for which to retrieve the status.

        Returns:
            dict: A dictionary containing the service name as the key and its status as
                the value. For example: {"Service A": "OK"}.
                If the service is not found, returns {"Service Name": "Not Found"} with a
                status code of 404.
        """
        body = {"size": 1, "query": {"match": {"application_name": service_name}}}

        res = self.es.search(index=self.index, body=body)

        print(res)
        print("self.index",self.index,res['hits']['hits'][0]['_source'])
        

        if res['hits']['hits']:
            status = res['hits']['hits'][0]['_source']['application_status']
            return {service_name: status}
        return {service_name: "Not Found"}, 404
