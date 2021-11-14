#!/bin/bash
set -o nounset -o pipefail -o errexit

# Load all variables from .env and export them all for Ansible to read
set -o allexport
source "$(dirname "$0")/.env"
set +o allexport

export ANSIBLE_SSH_ARGS="-F $HOME/.ssh/config"

# Run Ansible
exec ansible-playbook "$@"
