
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3.9 python3-pip 
    #&& apt-get install -y python3-tk


COPY requirements.txt .


RUN pip3 install -r requirements.txt

COPY . .

# ENV MYSQL_HOST=localhost
# ENV MYSQL_USER=root
# ENV MYSQL_PASSWORD=root
# ENV MYSQL_DATABASE=techienaman
EXPOSE 8000

#CMD ["uvicorn", "demo:app", "--port", "8000", "--reload"]
CMD ["python3", "demo.py"]
