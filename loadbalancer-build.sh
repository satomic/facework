docker build -f ./loadbalancer/Dockerfile -t satomic/facebeauty-lb .
docker tag satomic/facebeauty-lb satomic/facebeauty-lb:v0.0.1
docker push satomic/facebeauty-lb:v0.0.1
