# opencart_selenium

To run OpenCart in Docker:

`$ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml`

Run container:
      
`docker-compose up -d`

To run test:

`pytest --base_url http://localhost:80 --browser chrome -vs`

To run test for admin login:

`pytest tests/admin/login_test.py --base_url https://127.0.0.1/admin --browser Chrome -vs`


Install packages:

`pip install -r requirements.txt`
