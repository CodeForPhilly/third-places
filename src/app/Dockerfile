FROM node:18-slim
ARG HOME=usr/local/src/
WORKDIR $HOME

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD . .
ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["npm", "run", "dev", "--host"]
EXPOSE 4321