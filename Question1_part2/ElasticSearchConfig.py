from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import os


class ElasticSearchConfig:
    """
    A configuration class for interacting with Elasticsearch.

    Attributes:
        es (Elasticsearch): An instance of the Elasticsearch class.
        index (str): Name of the index in Elasticsearch.
    """

    def __init__(self):
        """
        Initializes an ElasticSearchConfig instance by connecting to an Elasticsearch instance,
        setting the index attribute, and ensuring the index exists in the Elasticsearch instance.
        """

        # cloud_id = os.getenv('ES_CLOUD_ID')
        # username = os.getenv('ES_USERNAME')
        # password = os.getenv('ES_PASSWORD')

        self.es = Elasticsearch(
            cloud_id="test:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDA5ZGNiYThiZTVlNDQ5Mjk5NWZkOTAzZTUyYzYyOGRmJGZlYzNjZmE3YzQxYjQwMDg5Y2RkNDhjMmExODg1OGMw",
            http_auth=('elastic', '4kqzkmD1OVTABB4bKs9zEImy')  
        )
        self.index = "service_monitoring"
        self.ensure_index_existence()

    def ensure_index_existence(self):
        """
        Checks if the index specified by the `index` attribute exists.
        If the index does not exist, it is created.
        """
        try:
            self.es.indices.get(index=self.index)
        except NotFoundError:
            self.es.indices.create(index=self.index)
