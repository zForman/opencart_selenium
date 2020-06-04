# opencart_selenium

To run OpenCart in Docker:

`$ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml`

Run container:
      
`docker-compose up -d`

To run test:

`pytest --base_url http://localhost:8046 --browser chrome -vs`


Install packages:

`pip install -r requirements.txt`