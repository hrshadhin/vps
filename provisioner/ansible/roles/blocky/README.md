# Blocky

Blocky DNS-proxy and adBlocker setup

## Requirements

To run this role you have to install **`python3`**

## Role Variables

Available variables are listed in default values (see `defaults/main.yml`)

## Dependencies

None.

## Example Playbook

    - hosts: servers
      roles:
       - { role: blocky }

## License

GPL-3.0-or-later

## Author Information

This role was created in 2021 by [H.R. Shadhin](https://hrshadhin.me)

## To-do

- custom mapping
- own blocking list
- add auth for DoH
