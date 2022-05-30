FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:02ab-main

RUN apt-get update -y &&\
    apt-get install -y wget libncurses5

# We need perl v5.16.3 specifically.
RUN wget https://www.cpan.org/src/5.0/perl-5.16.3.tar.bz2 &&\
    tar -xjf perl-5.16.3.tar.bz2 &&\
    cd perl-5.16.3 &&\
    ./Configure -des -Dprefix=$HOME/localperl &&\
    make install &&\
    mv perl /usr/bin

RUN git clone https://github.com/WouterSteyaert/BATCH-GE /root/batch-ge

# Configure tool + prep reference genome.
WORKDIR /root/batch-ge
RUN perl Install.pl
RUN cd genomes &&\
    wget ftp://hgdownload.cse.ucsc.edu/goldenPath/danRer7/bigZips/danRer7.fa.gz
RUN perl PrepareGenome.pl --Genome=danRer7

# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
WORKDIR /root
COPY wf /root/wf
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN  sed -i 's/latch/wf/g' flytekit.config
RUN python3 -m pip install --upgrade latch
