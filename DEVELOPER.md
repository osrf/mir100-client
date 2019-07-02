# Generating MiR100 Client REST API

**NOTE:** The generated code is committed into the repo, so there is no need to perform any generation if you are just using it. The instructions below is only if you need to re-generate the client for development purposes.

### Requirements

* Swagger codegen
	* https://github.com/swagger-api/swagger-codegen
* pdftotext
	* `apt install poppler-utls`

### Generating client code

* Extract text from MiR100 REST API pdf
	* `./pdftotext.sh`
* Generate openapi yaml
	* `python3 mir-openapi-generator.py > mir100-openapi.yaml`
* Generate client
	* `./generate-client.sh`
