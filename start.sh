#!/bin/sh
docker build -t backend ./backend
docker run -p 5000:5000 backend