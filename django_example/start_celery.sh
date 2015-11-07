#!/bin/bash

celery --app=celery_in_django worker --concurrency=`nproc` --loglevel=info &
