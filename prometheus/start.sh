BASE_DIR=$(cd `dirname $0`/..; pwd)
CONFIG=${BASE_DIR}/config/prometheus.yml
docker run -d -p 9090:9090 -v ${CONFIG}:/etc/prometheus/prometheus.yml prom/prometheus:latest
