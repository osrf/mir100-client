#!/bin/sh

pdftotext -f 4 -l 254 -raw -bbox mir_mir100_rest_api_270.pdf mir_mir100_rest_api_270-paths.xml
pdftotext -f 255 -raw -bbox mir_mir100_rest_api_270.pdf mir_mir100_rest_api_270-schemas.xml
