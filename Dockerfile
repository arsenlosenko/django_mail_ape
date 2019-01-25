FROM phusion/baseimage

EXPOSE 80

RUN mkdir app
WORKDIR /app

# copy all needed files
COPY api/ /app/api/
COPY mailape/ /app/mailape/
COPY mailinglist/ /app/mailinglist/
COPY static/ /app/static/
COPY templates/ /app/templates/
COPY user/ /app/user/
COPY scripts/ /app/scripts
COPY requirements.txt /app/requirements.txt
COPY manage.py  /app/manage.py

RUN mkdir /var/log/mailape/
RUN touch /var/log/mailape/mailape.log

# update packages, install python and pip
RUN apt-get update -y && \
    apt-get install -y \
    nginx postgresql-client redis-tools \
    python3 python3-pip

# setup venv, install dependencies
RUN pip3 install virtualenv
RUN virtualenv /app/venv

RUN bash /app/scripts/pip_install.sh /app
RUN bash /app/scripts/collect_static.sh /app
 
# configure nginx 
COPY nginx/mailape.conf /etc/nginx/sites-available/mailape.conf
RUN rm /etc/nginx/sites-enabled/*
RUN ln -s /etc/nginx/sites-available/mailape.conf /etc/nginx/sites-enabled/mailape.conf
 
COPY runit/nginx /etc/service/nginx
RUN chmod +x /etc/service/nginx/run

# add celery
COPY runit/celery /etc/service/celery
RUN chmod +x /etc/service/celery/run
 
# add gunicorn
COPY runit/gunicorn /etc/service/gunicorn
RUN chmod +x /etc/service/gunicorn/run

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* tmp/* /var/tmp/*
