# Almacenar logs de Nginx en PostgreSQL



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
https://betterstack.com/community/guides/logging/rsyslog-explained/
https://www.shubhamdipt.com/blog/send-nginx-logs-to-sql-database/
