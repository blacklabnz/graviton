#!/bin/bash

az container create \
    --name aci-flaskapi \
    --resource-group rg-flaskapi-dev \
    --image python:3.6-alpine \
    --dns-name-label aci-flaskapi-$RANDOM \
    --query ipAddress.fqdn \
    --ports 80 \
    --gitrepo-url https://github.com/dg-hub/graviton.git \
    --gitrepo-mount-path /mnt/graviton \
    --command-line "/bin/bash -c '/mnt/graviton/run.sh'" \
    --restart-policy Never \
    --cpu 1 \
    --memory 1
