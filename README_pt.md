# Laboratório simples em docker para o Zabbix com PostgreSQL, Grafana e Zapix(Testes em API)

## Conteúdo 
  - Zabbix:
    - Zabbix Server em: localhost:10051
    - Zabbix Agent em: localhost:10050
    - Zabbix Frontend em: http://localhost
  - Banco de dados:
    - Postgresql em : localhost:5432
    - PGAdmin em : http://localhost:5050
  - Ferramentas de apoio:
    - Zapix em: http://localhost:8080
    - Grafana em: http://localhost:3000
    - Mailhog:
      - WEB Client: http://localhost:8025
      - SMTP Servidor: mailhog
      - SMTP Server Port: 1025
      - SMTP Helo: mailhog
      - SMTP Email: admin@mailhog
  (As portas de rede padrão podem ser alteradas no arquivo '.env')

## Como usar:
  - [Instalar os pré-requisitos](./REQUIREMENTS.md)
  - Copiar o projeto e a dependência do zapix para sua estação:
    ```sh
    $ git clone --recurse-submodules https://git.serpro/monitoracao/zabbix-lab.git
    ```
  - **Se necessário** editar as variaveis de opções de versão/ip/porta:
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

  - Iniciar o proejeto com o docker-compose
    ```sh
    $ docker-compose up -d
    ```

# Sobre o Zabbix

![Zabbix](https://assets.zabbix.com/img/logo/zabbix_logo_500x131.png)

O Zabbix é uma solução de monitoramento distribuído de código aberto para grandes ambientes - O repositório base desse projeto que contem todos os **Dockerfiles** do [Zabbix](https://zabbix.com/) para [Docker](https://www.docker.com/) é o [zabbix-docker](https://github.com/zabbix/zabbix-docker) com [builds automáticas](https://registry.hub.docker.com/u/zabbix/) publicadas no [Docker Hub Registry](https://registry.hub.docker.com/).

# Sobre o Zapix

Ferramenta Online para testes e desenvolvimento usando pesquisas dentro da API Web do Zabbix - Projeto original em: [Github Zapix](https://github.com/monitoringartist/zapix) por [monitoringartist](https://monitoringartist.com/).

# Sobre o Grafana-XXL

![Grafana](https://raw.githubusercontent.com/grafana/grafana/master/docs/logo-horizontal.png)

Ferramenta para relatórios e análise de dados - Versão em container com todos os plugins já instalados em [Grafana-XXL](https://github.com/monitoringartist/grafana-xxl) por [monitoringartist](https://monitoringartist.com/).

# Sobre o Mailhog

![MailHog](https://raw.githubusercontent.com/mailhog/MailHog-UI/master/assets/images/hog.png)

Ferramenta para teste de envio de emails para desenvolvedores - [MailHog](https://github.com/mailhog/MailHog).
