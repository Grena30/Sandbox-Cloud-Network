# Sandbox Cloud Network Challenge

## Table of Contents

- [Project Documentation](./docs/Documentation.md)
- [Getting started](#getting-started)
- [Docker setup](#docker-setup)
- [API Documentation](#api-documentation)
- [Other](#other)

## Prerequisites

- [Docker](https://www.docker.com/)

## Getting Started

```bash
git clone https://github.com/Grena30/Sandbox-Cloud-Network
```

## Docker Setup

1. Build and run the project in the root directory

```bash
docker compose up --build
```
or
```bash
docker compose up --build -d
```
The `-d` flag allows you to start the application and its services without keeping the terminal open.

2. Check the logs of the containers to test if everything is working as expected

```bash
docker compose logs -f
```

3. Stop and remove the containers

```bash
docker compose down
```

4. If you want to remove the volumes as well, add the `--volumes` or `-v` flag.

```bash
docker compose down --volumes
```


## API Documentation

To test and send different API requests acess the following links:

**Compute-Intensive Pool**: [http://localhost:5000/docs](http://localhost:5000/docs)

**Request-Handling Pool**: [http://localhost:80/docs](http://localhost:80/docs)

## Other

### Consul

Consul is a service networking solution that helps manage secure network connectivity between services and across multi-cloud environments and runtimes. It also offers service discovery.

To view health-related checks and service connections access the link below.

**Consul UI**: [http://localhost:8500](http://localhost:8500)

### Grafana

Grafana is an open-source platform for monitoring and observability. It allows you to query, visualize, alert on and understand your metrics no matter where they are stored. Create, explore, and share dashboards. To view the platform access the link below. The default username is `admin` and password is `admin`.

**Grafana UI**: [http://localhost:3000](http://localhost:3000)

To create a dashboard go to the `Connection` tab then to the `Data sources` from which you choose `prometheus` and set the URL to `http://prometheus:9090`. Then go to `Dashboards` and choose to import a dashboard. Set the ID of the dashboard to `1860` which is related to Node Exporter. This  collects data about to server resources such as RAM, disk space, and CPU utilization. Lastly, choose the prometheus data source and import.  


### RabbitMQ Management

The RabbitMQ management provides an HTTP-based API for management and monitoring of RabbitMQ nodes and clusters, along with a browser-based UI. To view the platform access the link below. The default username is `admin` and password is `pass`.

**RabbitMQ UI**: [http://localhost:15672](http://localhost:15672)

To view different metrics about a specific queue go to the `Queue and Streams` tab and choose a desired one. 


## License

Shield: [![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg