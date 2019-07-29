# Jahia Universal Package Release notes

## actual version: v1.5

### v1.5 (2019-07-24)
* [BUG]: `DX_VERSION` and `PACKAGE_TYPE` where not updated when upgrading an env
* [BUG]: fix `set_dd_tag.sh` removing Datadog agent's `logs_enabled`
* [BUG]: fix update env that do not reinstall datadog agent
* [IMPROVEMENT]: logs sent to Datadog
    * services name in logs sent to Datadog  where `service` is `shortdomain`
    * user `dd-agent` is now a `tomcat` group member
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
