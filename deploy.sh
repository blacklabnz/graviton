#!/bin/bash
SNOWFLAKE_PASSWORD=""
CONTAINER_NAME=aci-graviton-$RANDOM
az container create \
    --name $CONTAINER_NAME \
    --resource-group rg-flaskapi-dev \
    --image python:3.6 \
    --vnet aci-vnet \
    --vnet-address-prefix 10.0.0.0/24 \
    --subnet aci-subnet \
    --subnet-address-prefix 10.0.0.0/24
#    --dns-name-label $CONTAINER_NAME \
    --environment-variables SNOWFLAKE_PASSWORD=$SNOWFLAKE_PASSWORD \
    --query ipAddress.fqdn \
    --ports 80 \
    --gitrepo-url https://github.com/dg-hub/graviton.git \
    --gitrepo-mount-path /mnt/graviton \
    --command-line "/bin/sh -c '/mnt/graviton/run.sh'" \
    --restart-policy Never \
    --cpu 1 \
    --memory 1
