# Simple docker lab for Zabbix with PostgreSQL, Grafana and Zapix (API Testing)

Versão em pt_BR: Olhe o arquivo README_pt.md

## Contents

- Zabbix:
  - Zabbix Server at: zabbix-server:10051
  - Zabbix Agent at: zabbix-agent:10050
  - Zabbix Frontend at: http://zabbix-frontend:8080
- Database:
  - Postgresql at: postgresql:5432
  - PGAdmin at: http://pgadmin:5050
- Support Tools:
  - Zapix at: http://zapix
  - Grafana at: http://grafana:3000
  - Mailhog:
    - WEB Client: http://mailhog:8025
    - SMTP Server: mailhog
    - SMTP Server Port: 1025
    - SMTP Helo: mailhog
    - SMTP Email: admin@mailhog

## How to use:

- [Install Prerequisites](./REQUIREMENTS.md)
  - Versão em pt_BR: Olhe o arquivo REQUIREMENTS_pt.md
- Copy the project and zapix dependency to your station:
  ```sh
  $ git clone --recurse-submodules https://github.com/isaqueprofeta/zabbix-lab.git
  ```
- In the scenario of forgetting the "--recurse-submodules" parameter, activate the zappix using the lines bellow:
  ```sh
  $ git submodule init
  $ git submodule update
  ```
- **If necessary** edit the version options:
  ```sh
  $ vim .env
  ```
  | Environment      | Default    |
  | ---------------- | ---------- |
  | ZABBIX_VERSION   | 5.0-latest |
  | POSTGRES_VERSION | 11         |
- Start the docker hoster for easy access using local DNS:
  ```sh
  $ docker run -d \
      --restart=always
      -v /var/run/docker.sock:/tmp/docker.sock \
      -v /etc/hosts:/tmp/hosts \
      dvdarias/docker-hoster
  ```
- Start the project with docker-compose
  ```sh
  $ docker-compose up -d
  ```
- **Note** that docker **will not use 'localhost'** so, do not configure the Grafana datasources for Zabbix or PostgreSQL and also for PGAdmin to PostgreSQL and Mailhog. To do this configuration, look at hostname option for each container, inside docker-compose.yml file.

# About Zabbix

![Zabbix](https://assets.zabbix.com/img/logo/zabbix_logo_500x131.png)

Zabbix is ​​an open source distributed monitoring solution for large environments - The base repository for this project that contains all **Dockerfiles** of [Zabbix](https://zabbix.com/) for [Docker](https: //www.docker.com/) is [zabbix-docker](https://github.com/zabbix/zabbix-docker) with [automatic builds](https://registry.hub.docker.com/u/zabbix/) published to the [Docker Hub Registry](https://registry.hub.docker.com/).

# About Zapix

Online tool for testing and development using queries in Zabbix Web API - Original project at: [Github Zapix](https://github.com/monitoringartist/zapix) by [monitoringartist](https://monitoringartist.com/).

# About Grafana

![Grafana](https://raw.githubusercontent.com/grafana/grafana/master/docs/logo-horizontal.png)

[Grafana](https://grafana.com) is a Data Analysis and Reporting Tool - Container already configured with zabbix plugin installed

# About Mailhog

![MailHog](https://raw.githubusercontent.com/mailhog/MailHog-UI/master/assets/images/hog.png)

Developer Email Testing Tool - [MailHog](https://github.com/mailhog/MailHog).
