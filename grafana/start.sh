BASE_DIR=$(cd `dirname $0`/..; pwd)
docker run -d -p 9090:9090 -v ${CONFIG}:/etc/prometheus/prometheus.yml prom/prometheus:latest
