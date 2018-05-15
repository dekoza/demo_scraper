#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A sunscraper.taskapp beat -l INFO
