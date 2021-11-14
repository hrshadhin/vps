# Base

A set of tasks that need to be run after VM first start. Like system updates, user add, securing the VM.

## Requirements

To run this role you have to install **`python3`**

## Role Variables

These are the variables needed for this role

```yaml
sysadmin_email:
add_swap:
swap_space:
time_zone:
add_secondary_user:
secondary_user_username:
secondary_user_password:
ssh_port:
ssh_pub_key_path:
install_fail2ban:
install_ufw:
ufw_rules: []
```

## Example Playbook

```yaml
- name: Provision XYZ
.....
  become: yes
  roles:
    - role: base
      add_swap: true,
      swap_space: 512M


# OR
- name: Provision XYZ
.....
  become: yes
  roles:
    - role: base
      sysadmin_email: devops@hrshadhin.me
      add_swap: false
      time_zone: Asia/Dhaka
      add_secondary_user: true
      secondary_user_username: devops
      secondary_user_password: Super7secre8
      ssh_port: 456
      ssh_pub_key_path: ssh_pub_key_file_for_seconadary_user
      install_fail2ban: True
      install_ufw: True
      ufw_rules: []
```

## License

GPL-3.0-or-later

## Author Information

H.R. Shadhin <devops@hrshadhin.me>
