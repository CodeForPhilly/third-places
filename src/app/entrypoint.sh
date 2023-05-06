#!/bin/sh

npm install
npm rebuild esbuild

exec "$@"