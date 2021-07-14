# APIs Load Testing using Locust IO: https://locust.io/
Locust is Open-source Python-based load testing. Locust provides a small HTTP API and a Web UI to control the 
execution of the tests and browsing through the results. One can use the API, for example, to automatically 
trigger stress tests as a part of build process.

## Update load testing criteria
* Open 'load_branding_test.sh' in project root directory
* Set or update the data
* Run: $ sh load_branding_test.sh
* Start web interface by clicking on generated server url such as: http://0.0.0.0:8089

## Locust Web Interface
* The fields on interface should already be populated by data you supplied in the shell script.