## Target: environment
#
# This initially-empty target provides an environment for docker-compose
# to start from the same base as the production builder environment. Common
# dependencies could be added here
#
FROM node:18-slim as environment


## Target: builder
#
# This target builds /src/dist with layers optimized for caching dependencies
#
FROM environment as builder
WORKDIR /src

COPY package*.json ./
RUN npm ci

COPY * ./
RUN npm run build


## Target: runtime
#
# This target provides an nginx web server wrapped around the static
# website build from the builder target
#
FROM nginx:alpine as runtime
COPY --from=builder /src/dist /usr/share/nginx/html
