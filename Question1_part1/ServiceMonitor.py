#!/usr/bin/env python3

import os
import json
from datetime import datetime

SERVICES = ['httpd', 'rabbitMQ', 'postgreSQL']  # Correct the service names.
HOSTNAME = 'host1'
APPLICATION_NAME = 'rbcapp1'


class Service:
    """
    Represents a service whose status can be checked.

    Attributes:
        name (str): The name of the service.

    Methods:
        is_active: Checks if the service is active and returns a boolean value.
    """

    def __init__(self, name: str):
        """
        Initializes a new instance of the Service class.

        Args:
            name (str): The name of the service.

        Attributes:
            name (str): Stores the name of the service.
        """
        self.name = name

    def is_active(self) -> bool:
        """
        Checks if the service is active by using the 'systemctl is-active' command.

        Returns:
            bool: True if the service is active, False otherwise.
        """
        cmd = f'systemctl is-active {self.name}'
        result = os.popen(cmd).read().strip()
        return result == 'active'

class ApplicationStatusWriter:
    """
    Writes the status of an application to a JSON file based on its dependent services.

    Attributes:
        services (list): A list of Service objects representing the dependent services.

    Methods:
        write_status: Writes the status of the application to a JSON file.
    """

    def __init__(self, services: list):
        """
        Initializes a new instance of the ApplicationStatusWriter class.

        Args:
            services (list): A list of Service objects.
        
        Attributes:
            services (list): Stores the list of Service objects.
        """
        self.services = services

    def write_status(self):
        """
        Checks the status of each service in the services list. If any service is down, 
        sets the application status to 'DOWN'. Otherwise, sets it to 'UP'. Writes this 
        status along with application name and host name to a JSON file. The filename 
        contains the application name and a timestamp.

        Output JSON Example:
        {
            'application_name': 'rbcapp1',
            'application_status': 'UP',
            'host_name': 'host1'
        }
        """
        status = 'UP'
        for service in self.services:
            if not service.is_active():
                status = 'DOWN'
                break

        timestamp = int(datetime.timestamp(datetime.now()))
        filename = f'{APPLICATION_NAME}-status-{timestamp}.json'
        status_data = {
            'application_name': APPLICATION_NAME,
            'application_status': status,
            'host_name': HOSTNAME
        }
        with open(filename, 'w') as outfile:
            print(status_data)
            json.dump(status_data, outfile, indent=2)


def main():
    services = [Service(service_name) for service_name in SERVICES]
    writer = ApplicationStatusWriter(services)
    writer.write_status()


if __name__ == '__main__':
    main()
