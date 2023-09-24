# My Simple Python REST Webservice

This is a simple Python REST webservice to add and check the health status of various services. The web service uses Elasticsearch for storing the service data.

## Installation

1. **Install the requirements**

    Before you can run the webservice, you need to install the necessary packages. Run the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary packages listed in the `requirements.txt` file.

## Elasticsearch Configuration

This project uses the Elasticsearch free trial cloud version, so you don't have to set up Elasticsearch locally.
> :warning: **Note that the Elasticsearch credentials are written in the file for simplicity. Typically, these should be set as environment variables, but for the ease of understanding and usage, they are included in the code directly.**


## API Endpoints

1. **Insert Payload into Elasticsearch**
   - **Endpoint:** `/add`
   - **Method:** `POST`
   - **Description:** Accepts a JSON file and writes it to Elasticsearch.

2. **Return All Application Status**
   - **Endpoint:** `/healthcheck`
   - **Method:** `GET`
   - **Description:** Returns the status (“UP” or “DOWN”) of all applications.

3. **Return Specific Application Status**
   - **Endpoint:** `/healthcheck/<string:service_name>`
   - **Method:** `GET`
   - **Description:** Returns the status (“UP” or “DOWN”) of a specific application by service name.

## Testing the API

Use Postman to test the API endpoints. Import the `Ivedha-API.postman_collection.json` file into Postman, which includes pre-configured requests for the API endpoints.

## Usage

Run the file `main.py` (or whatever you have named your Python file) to start the Flask webserver:

```bash
python main.py
