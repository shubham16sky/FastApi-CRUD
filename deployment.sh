#!/bin/bash

image=`docker images | grep "airmeet-app"`
if [ ! -z "$image" ]
then
	docker-compose down && docker rmi airmeet-app && docker-compose up -d
else
	docker-compose up -d 
fi




