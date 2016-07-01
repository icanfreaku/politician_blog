#!/bin/bash
#initialize database if it hasn't been initialized yet

DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose.yml}
EK_CONTAINER=${EK_CONTAINER:-ek}

echo "initializing $EK_CONTAINER"
docker-compose -f $DOCKER_CONFIG up -d $EK_CONTAINER 

#EK_CONTAINER_ID=$(docker-compose -f $DOCKER_CONFIG ps -q $EK_CONTAINER)
#echo "initializing $EK_CONTAINER_ID"
#for i in {60..0}; do
#    echo "waiting for ek to finish initializing..."
#    if [ $(docker logs $EK_CONTAINER_ID 2>&1 | grep "Success. You can now start the ek server" | wc -l) == 1 ]; then
#        docker-compose -f $DOCKER_CONFIG stop $EK_CONTAINER
#        echo "ek initialized"
#        exit 0
#    else
#        sleep 1
#    fi
#done
#if [ "$i" = 0 ]; then
#    echo >&2 "ek init failed"
#    exit 0
#fi

