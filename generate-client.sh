#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

swagger-codegen-cli generate -l python -i mir100-openapi.yaml -o $DIR -c swagger-config.json
