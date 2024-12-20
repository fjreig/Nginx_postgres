# Almacenar logs de Nginx en PostgreSQL

## 0. Servicios

|  ID  | Contenedor |     Descripción       | Puerto |                Url                  |
|:----:|:----------:|:---------------------:|:------:|:-----------------------------------:|
|  1   |  API       |  API Ejemplo 1        |   -    |  [api](http://localhost:8080/v1/docs#/)  |
|  2   |  API2      |  API Ejemplo 2        |   -    |  [api](http://localhost:8080/v2/docs#/)  |
|  3   |  Nginx     |  Dashboards gráficas  |  8080  |               -                     |
|  4   |  Postgres  |  BBDD                 |  5432  |               -                     |


## 1. Arrancar rsyslogd desde el contenedor nginx

Una vez arrancado el nginx, proceder de la siguiente manera, para ejecutar el rsyslogd
```
rsyslogd -f /etc/rsyslog.d/pgsql.conf -N1
systemctl restart rsyslog.service
```

Postreiormente se puede comprobar si se esta todo con el siguiente comando
```
tail -f /var/log/syslog
```


## Info
* https://betterstack.com/community/guides/logging/rsyslog-explained/
* https://www.shubhamdipt.com/blog/send-nginx-logs-to-sql-database/
