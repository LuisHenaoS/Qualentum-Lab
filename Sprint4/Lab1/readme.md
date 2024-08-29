
# Network Configuration with Vagrant and VirtualBox

## Description

This project sets up a network environment using Vagrant and VirtualBox to create three virtual machines: `bastion`, `web1`, and `web2`. The goal is to establish a private network where `web1` and `web2` can communicate exclusively through the `bastion` machine, which acts as a bridge or bastion host.

## Tools Used

- **Vagrant**: Tool for managing reproducible development environments through virtualization.
- **VirtualBox**: Virtualization software used to run virtual machines.
- **Bash**: Used to write provisioning scripts that configure network routes and firewall rules.
- **`iptables`**: Tool for controlling network traffic on Linux.
- **`tcpdump`**: Tool for capturing and analyzing network packets.

## Project Architecture

- **Bastion** (`bastion`): The central machine that connects the networks of `web1` and `web2`. It has two network interfaces to communicate with each subnet (`192.168.19.0/24` and `192.168.20.0/24`).
- **Web1** (`web1`): Machine in the `192.168.19.0/24` and `172.16.1.0/24` subnets.
- **Web2** (`web2`): Machine in the `192.168.20.0/24` and `172.16.2.0/24` subnets.

## Environment Setup

### Vagrantfile

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.ssh.insert_key = false # Avoids the need for SSH keys to simplify access

  # Bastion
  config.vm.define "bastion" do |bastion|
    bastion.vm.hostname = "bastion.local"
    bastion.vm.network "private_network", ip: "192.168.19.100"
    bastion.vm.network "private_network", ip: "192.168.20.100"

    # Provisioning script
    bastion.vm.provision "shell", inline: <<-SHELL
      sudo sysctl -w net.ipv4.ip_forward=1 # Enable IP forwarding
      sudo apt-get install -y tcpdump   # tcpdump
      sudo iptables -A FORWARD -s 172.16.1.0/24 -d 172.16.2.0/24 -j ACCEPT # Allow traffic between subnets
      sudo iptables -A FORWARD -s 172.16.2.0/24 -d 172.16.1.0/24 -j ACCEPT
    SHELL
  end

  # Web1
  config.vm.define "web1" do |web|
    web.vm.hostname = "web1.local"
    web.vm.network "private_network", ip: "192.168.19.2"
    web.vm.network "private_network", ip: "172.16.1.2"

    # Provisioning script
    web.vm.provision "shell", inline: <<-SHELL
      sudo ip route add 172.16.2.0/24 via 192.168.19.100 # Add route to web2
    SHELL
  end

  # Web2
  config.vm.define "web2" do |web|
    web.vm.hostname = "web2.local"
    web.vm.network "private_network", ip: "192.168.20.2"
    web.vm.network "private_network", ip: "172.16.2.2"

    # Provisioning script
    web.vm.provision "shell", inline: <<-SHELL
      sudo ip route add 172.16.1.0/24 via 192.168.20.100 # Add route to web1
    SHELL
  end

  # Virtualbox configuration
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end
end
```

## Steps to Run the Project

1. **Start the Virtual Machines**:
   - Start all virtual machines defined in the `Vagrantfile`:
     ```bash
     vagrant up
     ```

2. **Access the `bastion` Machine**:
   - Connect to the `bastion` machine using SSH:
     ```bash
     vagrant ssh bastion
     ```

3. **Access `web1` from `bastion`**:
   - From `bastion`, connect to `web1`:
     ```bash
     ssh vagrant@192.168.19.2
     ```
   - When prompted, the default password is `vagrant`.

4. **Access `web2` from `bastion`**:
   - From `bastion`, connect to `web2`:
     ```bash
     ssh vagrant@192.168.20.2
     ```

5. **Verify Connectivity with `ping`**:
   - **From `web1` to `web2`**:
     ```bash
     ping -c 4 172.16.2.2
     ```
   - **From `web2` to `web1`**:
     ```bash
     ping -c 4 172.16.1.2
     ```

6. **Capture Traffic with `tcpdump`**:
   - Capture ICMP traffic on `bastion`:
     ```bash
     sudo tcpdump -i eth1 icmp
     sudo tcpdump -i eth2 icmp
     ```

7. **Final Verification**:
   - Ensure there is no packet loss in the pings and that communication between `web1` and `web2` is working correctly through `bastion`.

## Additional Notes

- **Firewall**: If you experience connectivity issues, ensure that your host system's firewall or antivirus is not blocking network traffic between the virtual machines.

- **Reprovisioning**: If you make changes to the `Vagrantfile`, reprovision the machines with:
  ```bash
  vagrant reload --provision
  ```

- **Logs and Diagnostics**: Check logs and use `tcpdump` to diagnose network issues if you cannot communicate between `web1` and `web2`.

## Contributions

If you wish to contribute to this project, please create a pull request or report an issue on the GitHub repository.

---
