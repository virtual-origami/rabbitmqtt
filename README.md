# rabbitmqtt
RabbitMQ + MQTT Pub/Sub Queue Stack

(Currently the MQTT Port 1883 is commented out in the `docker-compose` file

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
