FROM  alpine:3.10.3

RUN mkdir /drf-test

WORKDIR /drf-test

ENV TZ=Asia/Shanghai

RUN  echo 'Asia/Shanghai' >/etc/timezone

COPY requirements.txt /drf-test/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk --no-cache update libpq \
    && apk --no-cache add tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo '$TZ' > /etc/timezone\
    && apk add --no-cache  python3 gcc musl-dev python3-dev postgresql-dev \
    && pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
