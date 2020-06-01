# opencart_selenium

To run OpenCart in Docker:

`$ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml`

Change opencart to ports:
      
      ports:
      - '8046:80'
      - '8047:443'
      
`docker-compose up -d`

To run test:

`pytest tests/test_opencart_page.py --base_url http://localhost:8046 --browser Chrome -vs`


Install packages:

`pip install -r requirements.txt`