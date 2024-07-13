#!/usr/bin/env bash
set -e

host="$1"
shift
cmd="$@"

until nc -z "$host" 3306; do
  &2 echo "MYSQL is unavailble - sleeping"
  sleep 1
done

>&2 echo "MYSQL is up - executing command"
exec $cmd
