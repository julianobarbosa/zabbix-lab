# Simple docker lab for Zabbix with PostgreSQL, Grafana and Zapix (API Testing)
## Versão em pt_BR: Olhe o arquivo README_pt.md

## Contents 
  - Zabbix:
    - Zabbix Server at: localhost:10051
    - Zabbix Agent at: localhost:10050
    - Zabbix Frontend at: http://localhost
  - Database:
    - Postgresql at: localhost:5432
    - PGAdmin at: http://localhost:5050
  - Support Tools:
    - Zapix at: http://localhost:8080
    - Grafana at: http://localhost:3000
    - Mailhog:
      - WEB Client: http://localhost:8025
      - SMTP Server: mailhog
      - SMTP Server Port: 1025
      - SMTP Helo: mailhog
      - SMTP Email: admin@mailhog
  (Default network ports can be changed in '.env' file)

## How to use:
  - [Install Prerequisites](./REQUIREMENTS.md)
    - Versão em pt_BR: Olhe o arquivo REQUIREMENTS_pt.md
  - Copy the project and zapix dependency to your station:
    ```sh
    $ git clone --recurse-submodules https://github.com/isaqueprofeta/zabbix-lab.git
    ```
  - **If necessary** edit the version options / ip / port variables:
    ```sh
    $ vim .env
    ```
    | Environment            | Padrão
    | -------------------    | -----------
    | IP_REDE                | 172.25.0.0/24
    | IP_ZBX_SERVER          | 172.25.0.10
    | IP_ZBX_FRONTEND        | 172.25.0.12
    | IP_ZBX_PGSQL           | 172.25.0.11
    | IP_ZBX_AGENT           | 172.25.0.13
    | IP_GRAFANA             | 172.25.0.14
    | IP_ZAPIX               | 172.25.0.15
    | IP_PGADMIN             | 172.25.0.16
    | IP_MAIL                | 172.25.0.17
    | PORT_ZBX_SERVER        | 10050
    | PORT_ZBX_FRONTEND      | 80
    | PORT_ZBX_FRONTEND_SSL  | 443
    | PORT_PGSQL             | 5432
    | PORT_ZBX_AGENT         | 10051
    | PORT_GRAFANA           | 3000
    | PORT_ZAPIX             | 8080
    | PORT_PGADMIN           | 5050
    | PORT_SMTP              | 1025
    | PORT_WEBMAIL           | 8025
    | ZABBIX_VERSION         | 4.0
    | POSTGRES_VERSION       | 11

  - Start the project with docker-compose
    ```sh
    $ docker-compose up -d
    ```
  - Note that docker not gonna let you use 'localhost' as configuring the Grafana datasources for Zabbix or PostgreSQL and also for PGAdmin to PostgreSQL. I'm using the hostname option for each container, and when configuring this features you can use the name that's specified there.

# About Zabbix

![Zabbix](https://assets.zabbix.com/img/logo/zabbix_logo_500x131.png)

Zabbix is ​​an open source distributed monitoring solution for large environments - The base repository for this project that contains all **Dockerfiles** of [Zabbix](https://zabbix.com/) for [Docker](https: //www.docker.com/) is [zabbix-docker](https://github.com/zabbix/zabbix-docker) with [automatic builds](https://registry.hub.docker.com/u/zabbix/) published to the [Docker Hub Registry](https://registry.hub.docker.com/).

# About Zapix

Online tool for testing and development using queries in Zabbix Web API - Original project at: [Github Zapix](https://github.com/monitoringartist/zapix) by [monitoringartist](https://monitoringartist.com/).

# About Grafana-XXL

![Grafana](https://raw.githubusercontent.com/grafana/grafana/master/docs/logo-horizontal.png)

Data Analysis and Reporting Tool - Container version with all plugins already installed on [Grafana-XXL](https://github.com/monitoringartist/grafana-xxl) by [monitoringartist](https://monitoringartist.com/).

# About Mailhog

![MailHog](https://raw.githubusercontent.com/mailhog/MailHog-UI/master/assets/images/hog.png)

Developer Email Testing Tool - [MailHog](https://github.com/mailhog/MailHog).
