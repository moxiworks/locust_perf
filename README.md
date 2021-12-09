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

## Distributed load generation
* A single process running Locust can simulate a reasonably high throughput. For a simple test plan it should be  
  able to make many hundreds of requests per second, thousands if you use FastHttpUser see  
  (https://docs.locust.io/en/stable/increase-performance.html#increase-performance).
* But if your test plan is complex or you want to run even more load, you’ll need to scale out to multiple processes,  
  maybe even multiple machines.
* To do this, you start one instance of Locust in master mode using the --master flag and multiple worker instances   
  using the --worker flag. If the workers are not on the same machine as the master you use --master-host to point   
  them to the IP/hostname of the machine running the master.
* The master instance runs Locust’s web interface, and tells the workers when to spawn/stop Users. The workers run   
  your Users and send back statistics to the master. The master instance doesn’t run any Users itself.
* Both the master and worker machines must have a copy of the locustfile when running Locust distributed.