#!/bin/bash

# Dummy service names
SERVICES=('httpd' 'rabbitMQ' 'postgreSQL')

# Create, start, and enable dummy services
setup_service() {
    service=$1
    echo "Setting up $service"
    echo -e "#!/bin/bash\nwhile true; do sleep infinity; done" | sudo tee /usr/local/bin/${service}-dummy.sh > /dev/null
    sudo chmod +x /usr/local/bin/${service}-dummy.sh
    echo -e "[Unit]\nDescription=Dummy $service Service\n\n[Service]\nExecStart=/usr/local/bin/${service}-dummy.sh\n\n[Install]\nWantedBy=multi-user.target" | sudo tee /etc/systemd/system/${service}.service > /dev/null
    sudo systemctl daemon-reload
    sudo systemctl start $service
    sudo systemctl enable $service
}

# Stop, disable, and remove dummy services
cleanup_service() {
    service=$1
    echo "Cleaning up $service"
    sudo systemctl stop $service
    sudo systemctl disable $service
    sudo rm /etc/systemd/system/${service}.service
    sudo rm /usr/local/bin/${service}-dummy.sh
    sudo systemctl daemon-reload
}

# Setup dummy services
for service in "${SERVICES[@]}"; do
    setup_service $service
done

# Let them run for 1 minute
echo "Letting services run for 1 minute..."
sleep 60

# Cleanup dummy services
for service in "${SERVICES[@]}"; do
    cleanup_service $service
done
