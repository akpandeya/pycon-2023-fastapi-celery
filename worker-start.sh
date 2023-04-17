#! /usr/bin/env bash
set -e

celery -A src.worker.celery worker
