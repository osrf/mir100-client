#!/bin/sh

swagger-codegen-cli generate -l python -i mir100-openapi.yaml -o client -c swagger-config.json
