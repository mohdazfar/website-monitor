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

Happy website monitoring!!!
