# Monitoring

Setup monitoring stack using, prometheus, alert_manager, node_exporter & grafana

## Requirements

To run this role you have to install **`python3`**

## Role Variables

Available variables are listed in default values (see `defaults/main.yml`)

## Dependencies

None.

## Example Playbook

    - hosts: servers
      vars:
        monitoring_components:
          - prometheus
          - node_exporter
          - alert_manager
          - grafana
      roles:
       - { role: monitoring }

## License

GPL-3.0-or-later

## Author Information

This role was created in 2021 by [H.R. Shadhin](https://hrshadhin.me)
