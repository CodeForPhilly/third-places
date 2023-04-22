FROM node:18-slim
WORKDIR usr/local/src/app
COPY . .
RUN npm install
CMD ["npm", "run", "dev", "--host"]
EXPOSE 4321