# prometheus-grafana-monitoring
Repo to set up simple prometheus and grafana instances.


### Steps:

1. Clone the repo.
2. cd to repo.
3. run `docker-compose up -d`
4. Prometheus and Grafana instances are up and running.
5. Access the Prometheus instance at [http://localhost:9090](http://localhost:9090)
6. Access the Grafana instance at [http://localhost:3000](http://localhost:3000)
7. Enter the username as 'admin' and password as 'grafana' to login to grafana instance.
8. Prometheus is added a datasource and it's metrics are available in the grafana instance.
