# Jelastic Jahia Environments

This repository hosts all packages, scripts & config files needed to create a Jahia environment on Jelastic.

## Infrasctructure overview

A Jahia environment contains:
- Two Haproxy nodes
- One or several Jahia Browsing nodes
- One Jahia Processing node
- Either one single MariaDB node or three MariaDB nodes clusterized with Galera

Requests on the domain name target Haproxy nodes (load balanced) which route them to Browsing node(s), where a session affinity is set in case there are multiple ones.

The processing node won't receive any request from client as browsing nodes are the only ones defined in Haproxy configuration.

In case of a Galera cluster, queries are all executed on the same MariaDB master node, which is replicated to the other ones.

## Docker images

Images used by Jahia environment nodes:

| Node type        | Docker image          |
| ---------------- | --------------------- |
| Haproxy          | jelastic/haproxy      |
| Jahia Browsing   | jahia/jahiastic-jahia |
| Jahia Processing | jahia/jahiastic-jahia |
| MariaDB          | jelastic/mariadb      |

## Packages

### Mixins

In order to limit JPS size and increase readability, actions can be defined in other JPS files and *imported* in another JPS with the **mixin** section.

Our different JPS use these defined mixins:
- common/common_actions.yml
  - Global actions, common to every nodes
- haproxy/haproxy_actions.yml
- jahia/jahia_actions.yml
- database/mariadb_actions.yml
- database/galera_actions.yml

### install.yml

The base JPS, called by Jahia Cloud to create an environment. It contains *only* nodes and events definition since actions are all defined in mixins JPS.

Takes as parameters:

- productVersion
  - Jahia version
- rootpwd
  - Jahia root password
- toolspwd
  - Jahia tools password
- browsingCount
  - Number of Jahia browsing nodes
- shortdomain
  - Environment shortdomain
- mode
  - Operating Mode, "production" or "development"
    - involves several things like the number of cloudlets, the number of MariaDB instances, the value of Jahia Xmx, etc.
- ddogApikey
  - Datadog API KEY

### update.yml

This package aims at updating events only, it is used when releasing a new Jahia Cloud version so we can make sure events are up-to-date and synchronized with environment modifications.

This script will allow to update the baseURL (containing branch name) with the last release tag so that the correct version of mixins is imported when triggering events.

### dx-upgrade.yml

This *upgrade* package aims at upgrading Jahia version by redeploying Jahia nodes with the target Jahia version tag, but since it takes the tag as a parameter, it is also used to do a rolling redeploy of Tomcat nodes.

Parameters are:
- name: targetVersion
  - Jahia Target Version. If nothing is specified, the current Jahia version of the target environment is selected
- name: packageType
- name: rollingUpgrade
  - Rolling upgrade, only available to redeploy Tomcat nodes only as the Jahia version upgrade currently needs all Tomcat nodes to be stopped

### onAfterClone.yml

As its name suggests, it is run from onAfterClone event, to do some actions that are not included in cloning function on the cloned environment.

### reset-polling.yml

Used by Jahia Cloud to reset polling when an action fails (especially during backup/restore). It generates a *finished* action on Jelastic Console so the frontend can be aware that there was an issue with previous JPS execution.

It takes as parameters:
- name: feature
  - Feature involved
- name: datetime
  - Date & Time

### utils/

In **utils** folder are stored packages that are called via Jelastic API from Jahia Cloud to do some specific actions related to environment management.

- *manage-auth-basic.yml*: add/update/remove auth basic on haproxy nodes
- *rewrite-rules.yml*: add/update/remove rewrite rules on haproxy nodes
- *set-jahia-root-password.yml*: update Jahia root password
- *set-jahia-tools-password.yml*: update Jahia tools password

## Monitoring

Each node is monitored on Datadog thanks to an agent directly installed on containers.

Datadog API key (pointing to a specific organization) is set as an envvar, and a periodic script update Datadog conf in case this envvar or any tag is changed so that the agent is still sending metrics to the right place.
