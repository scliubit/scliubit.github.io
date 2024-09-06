So bored, don't feel like studying, so I'll write a bit of a diary.


# Cloud Instance & Preparation

I chose the free Oracle Cloud for instance creation. Oracle Cloud offers the following free low-end cloud instance:

```
Shape: VM.Standard.E2.1.Micro
OCPU count: 1
Network bandwidth (Gbps): 0.48
Memory (GB): 1
Local disk: Block storage only
```

After configuring SSH login, you can start operations. Preparation steps:

```bash
sudo apt update
sudo apt upgrade
sudo apt install zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
```

By the way, modify the theme in `.zshrc` to `agnoster` to make it easier to see the paths.

In Oracle’s Ubuntu image, we need to perform an extra step for the firewall:


```bash
sudo apt install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
sudo firewall-cmd --list-all
```

You should see the following output:


```bash
public (default, active)
  target: default
  ingress-priority: 0
  egress-priority: 0
  icmp-block-inversion: no
  interfaces:
  sources:
  services: dhcpv6-client ssh
  ports:
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

As you can see, no ports are open. First, open port 3000 to make it easier to view later:

```bash
sudo firewall-cmd --zone=public --add-port=3000/tcp --permanent
sudo firewall-cmd --reload
```

You should see a success message. At this point, if you check the `--list-all` command again, you will see that port 3000 is open. To be safe, you can check with tcping from another machine:

```bash
tcping <your server IP> 3000
```

> Oracle's devices are not very easy to use. If you encounter network issues here, don't doubt your own operations. The best action here is to go into the instances' web console, select reboot, and force a power off.

# Gitea Installation

You can use a simple script to accomplish this:

```bash
git clone https://github.com/uvulpos/gitea-installer.git
cd gitea-installer
sudo bash ./gitea-installer-en.sh
```

Save the database information in advance:


```
--- Database ---
username: giteauser
password: \*\*\*\*\*\*
database: giteadb
```

Then visit`http://<Your IP Addr>:3000`and complete the installation using the above information.

> Some versions have a chain bug related to email notifications. If you don't have specific needs, you can skip enabling email notifications.
>
> Also, I’m not sure if this is a Gitea configuration issue, but Gitea now defaults to listening on tcp6, though this almost doesn't affect the result.
>
> If no service is listening on the designated port, even if we open the port, tools like `tcping` won’t return an open result. This is not a big deal.

After this step, you can directly access Git via the IP address on port 3000, but this design is not very elegant. We can use a pre-prepared domain name to create an alias.

# Pointing to a Domain Name

Let's assume our domain name is `example.com`. For some third-party registered domains, we may first need a DNS service. CloudFlare is a good free service provider, and their solutions are relatively mature. There are also corresponding products from Alibaba and Tencent Cloud in China. If you are outside mainland China, CF might work better.

After configuring the DNS, CF will strongly recommend using HTTPS protection, which might seem to complicate the process a bit, but nowadays, very few people use pure HTTP.

First, open the ports and install Nginx or other reverse proxy software:

```bash
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --zone=public --add-port=443/tcp --permanent
sudo firewall-cmd --reload
sudo apt update
sudo apt install nginx
```

Then we enter Nginx to make modifications. Here, I used a subdomain approach with the simplest reverse proxy configuration. Port 3000 is Gitea's default port.

```bash
sudo vim /etc/nginx/sites-available/git.example.com.conf
```

```
server {
    listen 80;
    server_name git.example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

After finishing, create a symbolic link, delete the content in `/etc/nginx/sites-available/default`, and check the configuration for correctness. If there are no errors, reload the Nginx configuration.

```bash
sudo ln -s /etc/nginx/sites-available/git.example.com.conf /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl reload nginx
```

If you didn’t enable forced HTTPS in Cloudflare, you should now be able to see Gitea on the HTTP interface. Next, proceed to issue a certificate:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d git.example.com
```

You should get the following output, indicating that the certificate will expire in six months. Remember to renew it every six months. The command is attached below:

```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/git.example.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/git.example.com/privkey.pem
```

```bash
sudo certbot renew
```

Certbot automatically manages Nginx’s configuration files, so usually, no extra handling is needed. Just verify and reload after:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

After this, Nginx will automatically listen on port `443` according to the configuration file.





