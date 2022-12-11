# Consul-API

## Getting Started


1. Use 'vagrant up' to build the virtual machine and start the Consul agent.
2. Use 'docker build -t <image_name> .' 
3. Use 'docker run -it -p 8000:8000 <image_name>'



## API EndPoints:


127.0.0.1:8000/v1/api/consulCluster/status
127.0.0.1:8000/v1/api/consulCluster/summary
127.0.0.1:8000/v1/api/consulCluster/members
127.0.0.1:8000/v1/api/consulCluster/systemInfo
