FROM python:3.9-alpine

USER root

ARG project_dir=/app/
ADD . ${project_dir}
WORKDIR ${project_dir}

RUN set -x && \
    apk upgrade --no-cache && \
    # apk --update add --no-cache musl \
    #         linux-headers \
    #         gcc \
    #         g++ \
    #         make \
    #         gfortran \
    #         openblas-dev && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# EXPOSE 5000 8080

CMD ["python3", "main.py"]
