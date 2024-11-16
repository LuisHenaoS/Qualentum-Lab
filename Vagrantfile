module OS
  def OS.windows?
    (/cygwin|mswin|mingw|bccwin|wince|emx/ =~ RUBY_PLATFORM) != nil
  end
end

NODE_COUNT = 3
Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64" #"ubuntu/focal64"

  (1..NODE_COUNT).each do |node_id|
    config.vm.define "node#{node_id}.example.com" do |node|
      node.vm.hostname = "node#{node_id}.example.com"
      node.vm.network :private_network, ip: "192.168.100.#{node_id + 10}"
      # If NOT in Windows, it is this easy
      if node_id == NODE_COUNT && ! OS.windows?
        node.vm.provision "ansible" do |ansible|
          ansible.limit = "all"
          ansible.playbook = "playbook.yml"
          ansible.inventory_path = "inventory_vagrant.ini"
        end
      end
    end
  end

  if OS.windows? then
    config.vm.define "installer" do |node|
      node.vm.network :private_network, ip: "192.168.100.10"
      node.vm.provision "key_permission", type: "shell", privileged: true, inline: <<-SHELL
      mkdir -p /tmp/keys
      NODES=#{NODE_COUNT}
      for i in $(seq 1 ${NODES}) ; do
        cp /vagrant/.vagrant/machines/node$i.example.com/virtualbox/private_key /tmp/keys/key$i
      done
      chmod 600 /tmp/keys/*
      chown vagrant /tmp/keys/*
      SHELL

      node.vm.provision "ansible_local" do |ansible|
        ansible.limit = "all"
        ansible.playbook = "playbook.yml"
        ansible.inventory_path = "inventory.ini"
        ansible.verbose = false
        ansible.install = true
        # due to: https://docs.ansible.com/ansible/latest/reference_appendices/config.html#avoiding-security-risks-with-ansible-cfg-in-the-current-directory
        ansible.config_file = "ansible.cfg"
      end
    end
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
end
