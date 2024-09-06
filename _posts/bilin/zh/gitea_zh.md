好无聊，不想学习，写点流水账。一切的起因是我看到我的GitHub项目太多了，管理起来很麻烦，而且很多是那种管也懒得管，删也不想删的repo。于是决定把一些建库之初就大概知道会烂尾的repo放到其他地方来。



# 云实例创建 & 前摇

选择了免费的Oracle Cloud进行实例创建。Oracle Cloud提供免费的低端云实例如下

```
Shape: VM.Standard.E2.1.Micro
OCPU count: 1
Network bandwidth (Gbps): 0.48
Memory (GB): 1
Local disk: Block storage only
```

配置好SSH登陆即可开始操作

开始前摇

```bash
sudo apt update
sudo apt upgrade
sudo apt install zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
```

顺便在`.zshrc`修改主题为`agnoster`方便看路径。

在Oracle的Ubuntu镜像里，我们需要额外操作一步firewall

```bash
sudo apt install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
sudo firewall-cmd --list-all
```

此时应看到的输出为

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

可见端口没有开启。首先开启3000端口方便未来查看

```bash
sudo firewall-cmd --zone=public --add-port=3000/tcp --permanent
sudo firewall-cmd --reload
```

成功时会返回success。此时重新查看`--list-all`命令会看到开启的3000端口，保险起见可以在另一台机器上用tcping查看

```bash
tcping <your server IP> 3000
```

> Oracle的设备非常不好用，如果网络这里出现了问题，请千万不要怀疑自己的操作有误。这里的最佳操作是进入instances的网页控制台，点选reboot并强制断电。

# Gitea安装

可以用一款简单的脚本实现。

```bash
git clone https://github.com/uvulpos/gitea-installer.git
cd gitea-installer
sudo bash ./gitea-installer-en.sh
```

Database的信息提前保留

```
--- Database ---
username: giteauser
password: \*\*\*\*\*\*
database: giteadb
```

然后访问`http://<Your IP Addr>:3000`，根据上述信息进行安装

> 某些版本中存在邮件通知的连锁bug，此处如无特别需求，不启用邮件通知即可。
>
> 此外不知道是不是gitea自己配置的问题，现在gitea会默认监听tcp6，虽然这对结果几乎不产生影响。
>
> 如果当前系统中没有服务对指定端口监听，那么即使我们开放了端口，tcping之类的测试也并不会返回open的结果。这个并不是大问题，

这一步结束之后就可以通过IP地址:3000端口直接访问Git了，但是如此设计实在不够优雅。我们可以用提前准备的域名来alias一下。

# 解析到域名

假设我们的域名叫做`example.com`。对于一些第三方注册的域名，我们可能首先需要一个解析服务。CloudFlare是一个不错的免费服务提供商，且方案均较为成熟，国内也有阿里腾讯云等对应的产品。如果不在中国大陆境内，CF的效果可能会更好一些。

配置好解析之后，CF会强烈推荐使用https保护之类的方案，看起来似乎会让过程更复杂一些，不过现在确实很少有人还是纯http了。

首先开启端口，并安装nginx等反向代理软件

```bash
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --zone=public --add-port=443/tcp --permanent
sudo firewall-cmd --reload
sudo apt update
sudo apt install nginx
```

进入nginx中进行修改，这里采用了二级域名的方案，并附上最简单的反向代理配置,3000端口是gitea默认端口。

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

结束后创建符号连接，删除`/etc/nginx/sites-available/default`中的内容并检测配置正确性，如果没有报错则对nginx进行配置文件重读取。

```bash
sudo ln -s /etc/nginx/sites-available/git.example.com.conf /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl reload nginx
```

如果没有在cloudflare开启强制https，此时应该已经可以在http界面看到gitea了。接下来进行证书颁发

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d git.example.com
```

应当获取如下输出，并提示该证书将在半年后过期，每半年记得进行一次renew即可，下附

```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/git.example.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/git.example.com/privkey.pem
```

```bash
sudo certbot renew
```

certbot会自动管理nginx的配置文件，通常不需要额外处理。接下来同样进行验证和重新加载即可

```bash
sudo nginx -t
sudo systemctl reload nginx
```

此后nginx会根据配置文件自动监听443端口。



---



