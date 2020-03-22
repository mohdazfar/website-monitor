# website-monitor

A simple website monitor that uses external configuration to check the status of websites. It monitors two things:

1. The status of the website i.e. 200 OR 404 etc
2. The response must have a string value that validates if the response is as expected

## Prerequisites

`docker` and `docker-compose` should be installed and configured.

## How it works

Assuming that `docker`  and `docker-compose` installed you just need to do:

```sh
$ docker-compose build
$ docker-compose up
```

Open the web browser and type `0.0.0.0:5000` and you'll see the logs started to appear. The web service will check the status every 30 seconds so you can refresh the page after 30 seconds to see new logs aprearing.

If you want to filter the logs based on date you can send a `GET` request like this `0.0.0.0:5000/filter?date=03-22-2020` and it will filter out the logs for specific day. 

Happy website monitoring!!!
