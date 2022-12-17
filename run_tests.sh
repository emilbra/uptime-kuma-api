#!/bin/sh

for version in 1.18.5 1.17.1
do
  echo "Starting uptime kuma $version..."
  docker run -d -it --rm -p 3001:3001 --name uptimekuma "louislam/uptime-kuma:$version" > /dev/null

  while [[ "$(curl -s -L -o /dev/null -w ''%{http_code}'' 127.0.0.1:3001)" != "200" ]]
  do
    sleep 0.5
  done

  echo "Running tests..."
  python -m unittest discover -s tests

  echo "Stopping uptime kuma..."
  docker stop uptimekuma > /dev/null

  echo ''
done