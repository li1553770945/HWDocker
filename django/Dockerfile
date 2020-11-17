FROM centos:7

RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup \
    && curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo  \
    && sed -i  's/$releasever/7/g' /etc/yum.repos.d/CentOS-Base.repo\
    && yum repolist \
    && yum -y install libXext libSM libXrender \
    && yum -y install git \
    && yum -y install python36 \
    && yum -y install gcc \
    && yum -y install python36-devel \
    && yum -y install mysql-devel \
    && pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && yum install kde-l10n-Chinese -y  \
    && yum install glibc-common -y  \
    && localedef -c -f UTF-8 -i zh_CN zh_CN.utf8

ENV LC_ALL zh_CN.UTF-8
COPY code/requirements.txt /requirements.txt
COPY sh /sh
RUN chmod 777 /sh/wait-for-it.sh \
    && chmod 777 /sh/web.sh \
    && pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=200 \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=200 \
    && rm requirements.txt 

EXPOSE 8000
