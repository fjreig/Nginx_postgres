# Almacenar logs de Nginx en PostgreSQL

## 0. Servicios

|  ID  | Contenedor |     Descripción       | Puerto |                Url                  |
|:----:|:----------:|:---------------------:|:------:|:-----------------------------------:|
|  1   |  API       |  API Monitorización   |   -    |  [api](http://localhost:8080/v1/docs#/)  |
|  2   |  API2      |  Servidor web         |   -    |  [api](http://localhost:8080/v2/docs#/)  |
|  3   |  Nginx     |  Dashboards gráficas  |  80    |               -                     |
|  4   |  Postgres  |  BBDD                 |  5432  |               -                     |

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
