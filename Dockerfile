FROM ubuntu:trusty
MAINTAINER Robert Glas "robert.glas.muenchen@gmail.com"

# python and relevant tools
RUN sudo apt-get update && apt-get install -y \ 
    curl \
    build-essential \
    python3 \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    libssl-dev \
    zlib1g-dev \
    libyaml-dev \
    libffi-dev \
    firefox \
    xvfb \ 
    python3-pip

# General dev tools
RUN apt-get install -y git

# Latest versions of python tools via pip
RUN pip3 install --upgrade pip \
                          virtualenv \
                          requests
                          
RUN pip3 install selenium \
                         behave \ 
                          xvfbwrapper
