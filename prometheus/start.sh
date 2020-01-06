BASE_DIR=$(cd `dirname $0`/..; pwd)
CONFIG=${BASE_DIR}/config/prometheus.yml
ALERT_RULES=${BASE_DIR}/config/alertmanager_rules.yml

cmd="docker run -d -p 9090:9090 -v ${CONFIG}:/etc/prometheus/prometheus.yml -v ${ALERT_RULES}:/etc/prometheus/alertmanager_rules.yml prom/prometheus:latest"
echo $cmd
$cmd
