BASE_DIR=$(cd `dirname $0`/..; pwd)
CONFIG=${BASE_DIR}/config/alert.yml

cmd="docker run -d -p 9093:9093 -v ${CONFIG}:/etc/alertmanager/alertmanager.yml --name alertmanager docker.io/prom/alertmanager:latest"
echo $cmd
$cmd
