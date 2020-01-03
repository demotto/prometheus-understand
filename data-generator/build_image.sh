#!/bin/bash -e
image_name="data-generator"
image_tag="latest"
full_image_name=172.17.198.145:5000/${image_name}:${image_tag}

cd "$(dirname "$0")"
docker build -t "${full_image_name}" .
docker push "$full_image_name"

