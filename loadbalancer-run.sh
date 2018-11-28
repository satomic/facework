docker kill facebeauty-lb
docker rm facebeauty-lb
docker run -itd -p 5001:5000 --name facebeauty-lb satomic/facebeauty-lb
