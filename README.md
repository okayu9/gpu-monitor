# GPU Monitor

This is a tool to monitor memory and utilization of the GPUs on the web.

![gpu-monitor-image](https://user-images.githubusercontent.com/2512724/39401448-6b916808-4b80-11e8-8a25-6005a48c995b.png)

## Usage

1. Create config.ini based on config.ini.example
2. Run server.py

## Note

- It is necessary to be able to login to the GPU servers with SSH without a password and passphrase.  
  Therefore, you may need to set ~/.ssh/config file.  
  (This software executes the following command: ssh hostname nvidia-smi ...)
- It is necessary that "nvidia-smi" command is installed on the target GPU servers.
- This software uses Bootstrap as a front-end Web application framework.  
  (You need to use a browser connected to the internet because this software refers to resoures on the Internet.)

