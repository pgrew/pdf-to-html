# Dockerfile to build a pdf2htmlEx image
FROM debian:latest

# update debian source list
RUN echo "deb http://ftp.de.debian.org/debian sid main" >> /etc/apt/sources.list && \
	apt-get -qqy update && \
	apt-get -qqy install pdf2htmlex && \
	rm -rf /var/lib/apt/lists/*

RUN apt-get -qqy update
RUN apt-get -qqy install python
RUN apt-get -qqy install python-pip

ARG SCRIPT=pdf2html.py
ARG PDF_DIR=/pdf
RUN mkdir $PDF_DIR
ADD $SCRIPT $PDF_DIR
RUN chmod +x $PDF_DIR/$SCRIPT

# input pdf to convert
ARG INPUT_PDF

ADD $INPUT_PDF /pdf
WORKDIR $PDF_DIR

CMD [$SCRIPT, $INPUT_PDF]
