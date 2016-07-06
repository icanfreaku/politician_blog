#!/bin/bash
# start production server

DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose-prod.yml}
docker-compose -f $DOCKER_CONFIG up -d
for i in {30..0}; do
        serverResponse=`wget --server-response --max-redirect=0 localhost:9200 2>&1`

        if [[ $serverResponse != *"Connection refused"* ]]
        then
                docker-compose -f $DOCKER_CONFIG run -d djangoprod python3 manage.py twitter_stream_collector
                docker-compose -f $DOCKER_CONFIG run -d djangoprod celery -A apps.sampleapp worker -B -l info
                break;
        else
                sleep 1
        fi
done
echo "started"