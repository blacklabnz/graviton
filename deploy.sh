#!/bin/bash
CONTAINER_NAME=aci-graviton-$RANDOM
az container create \
    --name $CONTAINER_NAME \
    --resource-group rg-flaskapi-dev \
    --image python:3.6 \
    --dns-name-label $CONTAINER_NAME \
    --query ipAddress.fqdn \
    --ports 80 \
    --gitrepo-url https://github.com/dg-hub/graviton.git \
    --gitrepo-mount-path /mnt/graviton \
    --command-line "/bin/sh -c '/mnt/graviton/run.sh'" \
    --restart-policy Never \
    --cpu 1 \
    --memory 1
