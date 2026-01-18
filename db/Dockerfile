FROM redis:8.4.0

WORKDIR /home/db

COPY redis.conf /usr/local/etc/redis/redis.conf
COPY run.sh .
RUN chmod +x run.sh

CMD ["./run.sh"]
