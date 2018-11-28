docker kill facebeauty
docker rm facebeauty
docker run -itd -p 5000:5000 --name facebeauty satomic/facebeauty