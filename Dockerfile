FROM ubuntu:trusty

MAINTAINER Agustin Larreinegabe <alarreine@gmail.com>

RUN apt-get update && apt-get install -y build-essential software-properties-common

RUN add-apt-repository -y ppa:grand-edgemaster/texlive-backports && apt-get update

RUN apt-get install -y --no-install-recommends latexmk texlive-fonts-extra \
    texlive-fonts-recommended texlive-latex-base texlive-latex-extra \
    texlive-latex-recommended texlive-luatex texlive-xetex latex-xcolor texlive-pictures pgf \
    texlive-lang-french fonts-font-awesome fonts-lmodern

RUN useradd myuser \
	&& mkdir /home/myuser \
	&& chown myuser:myuser /home/myuser \
	&& mkdir /data \
	&& chown myuser:myuser /data

USER myuser
WORKDIR /data

CMD ["/bin/bash"]