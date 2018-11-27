FROM satomic/python:flask
WORKDIR /usr/src/
CP backend /usr/src/
EXPOSE 5000
CMD ["python","./backend/ServiceFace"]