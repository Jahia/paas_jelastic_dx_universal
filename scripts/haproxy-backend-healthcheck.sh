#!/usr/bin/env bash

source /.jelenv

res=$(curl -s $3:$4/modules/healthcheck?token=$jahia_cfg_healthcheck_token |jq .status -r)
if [ "$res" = "GREEN" ] || [ "$res" = "YELLOW" ]; then
  exit 0
fi
exit 1
