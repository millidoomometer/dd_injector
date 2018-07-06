dd_injector
inject desired custom metrics do datadog

examples included:
 * access_log_check (dd_injector.Stats)
check size and age of given access log

 * process_check (dd_injector.Service)
check if process is running, 1 or 0

 * s3_log_check (dd_injector.Stats)
this is a very custom check, we have fluentd copying certain logs to corresponding buffer files and want to monitor the sizes/ages, makes use of dd_injector.Stats

 * injection of metrics uses dd_injector.DD

Example configuration
```
[access_log]
location = /usr/local/squid/var/log/squid/access.log
[proc_check]
FluentD = /usr/sbin/td-agent
Lighttpd = /usr/sbin/lighttpd
Squid = /sbin/squid
[datadog]
app_key = yourdatadogappkeyhere
api_key = yourdatadogapikeyhere
[s3_log]
synflood = /var/log/td-agent/s3/synflood/
ban = /var/log/td-agent/s3/ban/
port = /var/log/td-agent/s3/port/
httpd_access = /var/log/td-agent/s3/httpd_access/
access = /var/log/td-agent/s3/access/
```

dependencies:
`sudo pip install -r pip_reqs.txt`

not daemonized yet, cron example:
`* * * * * /usr/bin/python /home/ec2-user/dd_injector.py`
