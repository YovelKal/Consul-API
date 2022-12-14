Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8500, host: 8080
  serverIp = "192.168.33.10"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
    vb.memory = "1024"
    vb.cpus = "2"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y apache2
    sudo apt-get install tmux
    sudo apt-get install zip unzip
    cd /usr/local/bin
    echo "Installing the Consul package..."
    sudo wget https://releases.hashicorp.com/consul/1.14.2/consul_1.14.2_linux_amd64.zip
    unzip consul_1.14.2_linux_amd64.zip
    sudo rm -rf consul_1.14.2_linux_amd64.zip

    cd ~ mkdir -p consul-config/server
    sudo apt-get install nano
    sudo nano consul-config/server/config.json


    echo "Adding the Consul service configuration..."
    json='{"bootstrap": true,"server": true,"log_level": "DEBUG","enable_syslog": true,"datacenter": "server1","addresses" : {"http": "0.0.0.0"},"bind_addr": "192.168.33.10","node_name": "Metuka","data_dir": "/home/k/consuldata","acl_datacenter": "server1","acl_default_policy": "allow","encrypt": "5KKufILrf186BGlilFDNig=="}'
    mkdir consul-config
    mkdir consul-config/server
    echo "$json" > consul-config/server/config.json

    echo "installing docker"
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    gpg --dearmor | \
    sudo tee /usr/share/keyrings/docker-ce-archive-keyring.gpg > \
    /dev/null
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-ce-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker-ce.list > /dev/null
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7EA0A9C3F273FCD8
    sudo apt-get update
    sudo apt-get -y install docker-ce=18.06.1~ce~3-0~ubuntu
    sudo chmod 777 /var/run/docker.sock

    echo "Building the API image..."
    cd ../../vagrant
    docker build -t consulapi .

    echo "Starting the Consul service..."
    nohup consul agent -dev -ui -config-dir ~/consul-config/server -bootstrap &

    echo "Running the API..."
    docker run -p 8000:8000 consulapi

  SHELL
end
