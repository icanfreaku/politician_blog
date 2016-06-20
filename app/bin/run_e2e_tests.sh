#!/bin/bash
#this will start test server, start tests then stop test server

export DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose-e2e-test.yml}
PTOR_CONFIG=${PTOR_CONFIG:-e2e-tests/protractor.conf.js}
TEST_SERVER_URL=${TEST_SERVER_URL:-http://localhost:8001}

export DB_CONTAINER=dbe2e
export DBDATA_CONTAINER=dbdatae2e

if [ $(docker-compose -f $DOCKER_CONFIG ps | grep "djangoe2e" | grep "Up" | wc -l) != 0 ]; then
    echo "stopping running containers"
    docker-compose -f $DOCKER_CONFIG stop
fi

./bin/init_db.sh

if  ! [ -d e2e-tests/node_modules ]; then
    echo "installing e2e test deps"
    cd e2e-tests
    npm install 
    cd ..
fi

docker-compose build frontend
docker-compose run --rm frontend gulp build

#start testserver in background
echo "starting test server"
docker-compose -f $DOCKER_CONFIG build
docker-compose -f $DOCKER_CONFIG up -d

#wait until django starts
while true; do
    echo "waiting for django to start..."
    if  [ $(curl -s -o /dev/null -w "%{http_code}" $TEST_SERVER_URL) == 200 ]; then
        break
    else
        sleep 1
    fi
done

echo "starting e2e tests"
#run tests
./e2e-tests/node_modules/protractor/bin/protractor $PTOR_CONFIG

#kill django
echo "stopping test server"
docker-compose -f $DOCKER_CONFIG stop
