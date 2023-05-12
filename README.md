# Third Places Project

## Overview

Third Places Project is a project that will seek to connect Philadelphians to comfortable public spaces, with the focus being on finding places spontaneously.

This project was started as part of Code for Philly's Launchpad 2023 event.

## Joining the regular meetings

We host weekly meetings both in person and remotely. This is largely where we make decisions and set up collaborative pairing sessions to get large chunks of work done.

The best way to find out about our meetings is joining the [#third-places-project](https://codeforphilly.slack.com/archives/C051CV94UV8) channel on the [Code for Philly](https://www.codeforphilly.org/) [Slack](https://www.codeforphilly.org/chat/).

## Contributing

Please read the [contributing guidelines](https://github.com/CodeForPhilly/third-places/blob/main/CONTRIBUTING.md) to find out how you can volunteer.

## Setup

### Requirements

You will need to have a working understanding of using a Unix-like system via a terminal or shell and the instructions below use Bash commands.

In order to run this app, you will need to have the following libraries installed on your machine:

Docker (Docker for Mac, or Docker for Windows) [Install here](https://docs.docker.com/get-docker/)

Note: These installations will not be required locally once we have the project containerized, the container will hand that.

### Create .env file

#### Why a .env?
We will be using a `.env` file to share environment variables with each of the Docker containers and separate our environment variables from our code.

#### Make the actual file

Duplicate the `.env.sample` file and rename it to `.env`

#### Note

The `.env` file is ignored by git and so any changes will have to be communicated to the team to make sure API keys etc. stay aligned from dev to dev.

### Start the servers

To run all servers (React, Django, & PostgreSQL):
```sh
# Build the containers from images
docker-compose build
# Run the servers
docker-compose up

# OR for a single command to do both
docker-compose up --build
```

### Port Numbers

Access the following ports from localhost to access their respective services

| Service | Port |
|---------|------|
| React   | 4321 |
| Django  | 8321 |

### Api Reference

- `/api/`: Hello world!
- `/users/`: `GET`, `POST` users
- `/users/{id}`: `GET`, `PUT` specific user details
