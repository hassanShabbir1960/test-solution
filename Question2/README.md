# Readme

This document provides a guide to testing the solution for checking the status of the application `rbcapp1` and listing down services that are not running, using an inventory file and Ansible playbook.

## Prerequisites

- Ansible installed on your local machine
- REST endpoint running, which was created in `TEST1` (Question1_part2)

## Inventory File

Create an inventory file named `inventory` with the following contents:

\```

[webserver]
localhost ansible_connection=local

[rabbitmq]
localhost ansible_connection=local

[postgresql]
localhost ansible_connection=local

\```

This inventory file specifies that the `webserver`, `rabbitmq`, and `postgresql` groups all run on `localhost` with a local connection type.

## Running the Playbook

You will need to execute the `assignment.yml` Ansible playbook to check the status of the `rbcapp1` application and to get a list of services that are down. 

Run the following commands:

1. To check the status of the `rbcapp1` application:

\```bash
ansible-playbook -i inventory assignment.yml -e "my_action=check-status" -K
\```

2. To check the disk:

\```bash
ansible-playbook -i inventory assignment.yml -e "my_action=check-disk" -K
\```

In both cases, you will be prompted to enter a password. Enter the password if running locally; otherwise, you will face a permission issue.


