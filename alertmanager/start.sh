BASE_DIR=$(cd `dirname $0`/..; pwd)
CONFIG=${BASE_DIR}/config/alertmanager.yml
docker run -d -p 9093:9093 -v ${CONFIG}:/etc/alertmanager/config.yml --name alertmanager docker.io/prom/alertmanager:latest
