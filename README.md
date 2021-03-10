# rabbitmqtt
RabbitMQ + MQTT Pub/Sub Queue Stack

## Usage

1. Create a network for the stack called `iotstack`:

        docker network create iotstack

2. Change the Default Username / Password / Node Namein the `prototype.env` file if needed

3. Change the `hostname` for the RabbitMQ service in the `docker-compose.yml` file if needed

4. Bring the Stack Up using:

        docker-compose up -d

5. You can change the password for Redis in the `redis/redis.conf` file

### Log Tracing

    docker-compose logs -f

## Consumers

The `consumers` directory has script that will connect to the RabbitMQ Broker via AMQP and list to MQTT Published Payload

### Usage

    cd consumers/
    # Enable Virtual Environment
    python -m venv venv
    . venv/bin/activate
    # Upgrade pip
    pip install -U pip
    # Install Packages
    pip install -r requirements.txt

Each Code has some CLI arguments in them. Use

    python3 <file_name>.py --help


    

## TODO

__Consumers__:
- [ x ] Give a simple `pika` based Consumer Example
- [  ] Use `redis` package along with `pika`
- [  ] Use `celery` to use RabbitMQ and Redis

__Documentation__:

- [ ] Add docs for setting up a distinct use in RabbitMQ via Management UI