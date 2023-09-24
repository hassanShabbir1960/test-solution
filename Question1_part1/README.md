# README

## Introduction

This README provides a guide for setting up and monitoring three dummy services: 'httpd', 'rabbitMQ', and 'postgreSQL'. The provided bash and Python scripts create, start, and monitor these services, checking their statuses and writing the statuses to a JSON file.

## Prerequisites

Ensure that your user has sufficient permissions to run scripts, manage services, and create files in system directories.

## Instructions

1. **Setting up the Services:**

    - First, change the permissions of the `runServices.sh` script to make it executable with the following command:
      ```bash
      chmod +x runServices.sh
      ```
    - Now, run the script:
      ```bash
      ./runServices.sh
      ```
    This script sets up three dummy services: 'httpd', 'rabbitMQ', and 'postgreSQL' and lets them run for 1 minute. 

2. **Monitoring the Services:**

    - While the `runServices.sh` script is running, open another terminal.
    - Run the `ServiceMonitor.py` script with the following command:
      ```bash
      python ServiceMonitor.py
      ```
    This Python script checks the status of the three dummy services. If all services are running, it will create a JSON file with a status of 'UP'. If any of the services are not running, the JSON file will have a status of 'DOWN'. The JSON file will be named with the application name and a timestamp (e.g., `rbcapp1-status-1632969334.json`).

## Files

- `runServices.sh`: This is a bash script that sets up and runs three dummy services for 1 minute.
- `ServiceMonitor.py`: This Python script monitors the status of the three services and writes their statuses to a JSON file.

## JSON Output Example

The JSON output file will look something like this:

```json
{
  "application_name": "rbcapp1",
  "application_status": "UP",
  "host_name": "host1"
}
