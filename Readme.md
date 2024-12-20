# Almacenar logs de Nginx en PostgreSQL

https://betterstack.com/community/guides/logging/rsyslog-explained/
https://www.shubhamdipt.com/blog/send-nginx-logs-to-sql-database/


```
rsyslogd -f /etc/rsyslog.d/pgsql.conf -N1
```

```
systemctl restart rsyslog.service
```

```
tail -f /var/log/syslog
```
