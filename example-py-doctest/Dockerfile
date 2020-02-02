
FROM ubuntu:latest

RUN apt-get update 

RUN apt-get install -y git

WORKDIR /doubt/somesh

RUN git clone https://github.com/AndyLPK247/python-testing-101.git

RUN apt-get install -y python3  && \      
    apt-get install -y  python  && \       
    apt-get install  -y python-minimal

RUN apt-get install -y python-pip

RUN pip install --upgrade pip

RUN pip install xmlrunner

WORKDIR /doubt/somesh/python-testing-101/example-py-doctest

COPY  test.py /doubt/somesh/python-testing-101/example-py-doctest

#RUN chmod 777 "test.py"

CMD ["python", "test.py"]





