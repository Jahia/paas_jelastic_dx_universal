# Jahia Universal Package Release notes

## actual version: v1.9

### v1.9 (2019-09-18)
* [IMPROVEMENT]: PAAS-381 add package to update jahia tools password
* [IMPROVEMENT]: PAAS-379 add package to update jahia root password
* [IMPROVEMENT]: PAAS-309 changes to adapt to haproxy environement
    * scaling of tomcat nodes now involve haproxies conf update
    * deletion of a Jahia environment involve deletion of the corresponding haproxy environment
    * tomcat logs now show the real IP address of the client
* [IMPROVEMENT]: PAAS-150 passwords are not deisplayed anymore in catalina.out
* [IMPROVEMENT]: PAAS-284 use new images for browsing and processing nodes
    * remove some actions from the package (datadog installation, maven,)

### v1.8.1 (2019-09-04)
* [BUG]: Cannot have working DX if not >v7.3.1.0
    * because of a java argument for Garbage Collector logging wich is unknown for jdk 8

### v1.8 (2019-09-03)
* [BUG]: weird probleme with `mysql_cluster` package
    * install mariadb 10.4.6 in dev cluster and 10.3.16 in prod
    * now we not using this package anymore and directly create the node with v10.4.6
    * we will return to it when mariadb clustering will be ok
* [BUG]: maven url is 404
    * new version (3.6.1) of Maven was release today
    * change to used url to the archived one from the Maven website

### v1.7 (2019-08-22)
* [IMPROVEMENT]: password in logs are now masked before being set to datadog
* [IMPROVEMENT]: now sqldb nodes get a jahia_cfg_operatingMode envvar too
* [BUG]: I'm ashamed about a lot of things from previous version
    * change PhpMyAdmin disabling method
        * v1.6 is completly broken because of it, sorry for that
        * now using `PHPMYADMIN_ENABLED` and `ADMINPANEL_ENABLED` envvars to `false`
    * MariaDB fork was shitty
        * wrong repo name `pass` instead of `paas`
        * `baseURL`'s package still rely to originated Jelastic's repo

### v1.6 (2019-08-02)
* [CHANGE][BUG][IMPROVEMENT]: about MariaDB
    * now using a fork version of Jelastic's `mysql_cluster` package
        * it can be found here: https://www.github.com/Jahia/pass_jelastic_mysql_cluster
    * MariaDB is now v10.4 which have some importants authentification changes
        * now local user `root` and `mysql` can connect to the server using a socket and without password
        * now the mysql user used by Jahia is just a regular user granted with all permission on jahia's database only (and not the mariadb's root anymore)
    * disable httpd to avoid phpMyAdmin access
* [IMPROVEMENT]: Garbage Collector Logs are now enabled for Jahia

### v1.5 (2019-07-24)
* [BUG]: `DX_VERSION` and `PACKAGE_TYPE` where not updated when upgrading an env
* [BUG]: fix `set_dd_tag.sh` removing Datadog agent's `logs_enabled`
* [BUG]: fix update env that do not reinstall datadog agent
* [IMPROVEMENT]: logs sent to Datadog
    * services name in logs sent to Datadog  where `service` is `shortdomain`
    * user `dd-agent` is now a `tomcat` group member
    * now send access_logs too
    * now send karaf logs too
* [IMPROVEMENT][BUG]: MariaDB
    * adding slow queries log in /var/log/mysql/slow-queries.log
        * a slow query is more than 5.0s
    * now functionnal log rotation
    * Datadog agent now use tag `role:Database` for mariadb nodes
* [BUG]: better selection of tools password


### v1.4 (2019-07-05)
* [NEW]: Add license if set
    * we can now fill a optional `license` setting with the base64 encoded license file
    * if not set, the 30 days demo license remain

### v1.3 (2019-07-02)
* [BUG][[PAAS-233](https://jira.jahia.org/browse/PAAS-233)] Add new parameters to `_JAVA_OPTIONS` to avoid some issues
    * `-XX:SurvivorRatio=8 `
    * `-Xmn1G`
