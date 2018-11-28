FROM satomic/python:flask
WORKDIR /usr/src/
COPY backend .
COPY MicroService MicroService
COPY PythonSDK PythonSDK
EXPOSE 5000
CMD ["python","./ServiceFace.py"]
