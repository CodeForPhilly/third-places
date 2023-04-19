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

### Start the servers
To run both servers:
```sh
# Set up react dependencies
# From third-places/src/app/
cd src/app/
npm install
npm run dev
cd ../

# In new tab
# From thirdplaces/src/django/
cd django/
python3 manage.py runserver
```

### Port Numbers

Access the following ports from localhost to access their respective services

| Service | Port |
|---------|------|
| React   | 4321 |
| Django  | 8000 |

### Api Reference

`/api/`: Hello world!
