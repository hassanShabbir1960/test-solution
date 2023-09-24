class ServiceStatus:
    """
    A class for managing service status data in Elasticsearch.

    Attributes:
        es (Elasticsearch): An instance of the Elasticsearch client.
        index (str): Name of the Elasticsearch index for storing service status data.
    """

    def __init__(self, es_config):
        """
        Initializes a ServiceStatus instance with an Elasticsearch configuration.

        Args:
            es_config (ElasticSearchConfig): An instance of ElasticSearchConfig containing
                Elasticsearch connection details and index information.
        """
        self.es = es_config.es
        self.index = es_config.index

    def add_status(self, content):
        """
        Adds service status data to the Elasticsearch index.

        Args:
            content (dict): A dictionary containing the service status data to be added.

        Returns:
            tuple: A tuple containing a dictionary with the result and a HTTP status code.
                The result dictionary may include a "result" key with the Elasticsearch result
                and a status code of 201 if the operation is successful. If the content is
                invalid or missing, an error dictionary with a status code of 400 is returned.
        """
        if content:
            res = self.es.index(index=self.index, body=content)
            return {"result": res['result']}, 201
        return {"error": "Invalid payload"}, 400
