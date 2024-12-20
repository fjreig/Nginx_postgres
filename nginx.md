https://betterstack.com/community/guides/logging/rsyslog-explained/
https://www.shubhamdipt.com/blog/send-nginx-logs-to-sql-database/



docker build -t frreimon/nginx:1.0 -f nginx/dockerfile .

```
CREATE TABLE accesslog (id serial NOT NULL PRIMARY KEY, log_line json NOT NULL, created_at TIMESTAMP NOT NULL);
```

```
apt update -y 
apt upgrade -y
apt install nano -y
apt install systemctl -y
apt install rsyslog-pgsql -y
```

```
nano /etc/rsyslog.d/51-mywebsite.conf
```

```
global(
  workDirectory="/var/spool/rsyslog"
)

module(load="imfile") # Load the imfile input module

input(type="imfile"
      File="/var/log/nginx/access.log"
      Tag="mywebsite:")

module(load="ompgsql")

template(name="pgsql-template" type="list" option.sql="on") {
  constant(value="INSERT INTO accesslog (log_line, created_at) values ('")
  property(name="msg")
  constant(value="','")
  property(name="timereported" dateformat="pgsql" date.inUTC="on")
  constant(value="')")
}

if( $syslogtag == 'mywebsite:')  then {
  action(type="ompgsql" server="postgres"
        user="postgres"
        pass="postgres"
        db="pam"
        template="pgsql-template"
        queue.type="linkedList")
}
```

```
rsyslogd -f /etc/rsyslog.d/pgsql.conf -N1
```

```
systemctl restart rsyslog.service
```

```
tail -f /var/log/syslog
```