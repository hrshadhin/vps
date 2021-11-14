# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
IMAGE_NAME = "ubuntu/focal64"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # basic config
  config.vm.box = IMAGE_NAME
  config.vm.box_check_update = false
  config.vm.synced_folder ".", "/vagrant", disabled: true
  # advance configs, needed after base role setup is done.
  # so, on first run comment out below 4 lines
  config.ssh.host = "192.168.60.60"
  config.ssh.insert_key = false
  config.ssh.port = ENV["SSH_PORT"] || "22"
  config.ssh.private_key_path = "~/.ssh/id_rsa_local"

  config.vm.define "testVM" do |testVM|
    testVM.vm.provider "virtualbox" do |vb|
      vb.name = "testVM"
      vb.cpus = 1
      vb.memory = "1024"
      vb.check_guest_additions = false
    end
    testVM.vm.network "private_network", ip: "192.168.60.60", name: "vboxnet1"
  end
end
