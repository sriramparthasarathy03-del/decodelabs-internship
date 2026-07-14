

# Project 2 - The Server Commander

This project demonstrates launching an AWS EC2 Linux instance, installing the Apache Web Server, and hosting a custom webpage.

## Technologies Used

- AWS EC2
- Amazon Linux 2023
- Apache HTTP Server
- HTML

## Commands Used

```bash
sudo dnf update -y
sudo dnf install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
sudo systemctl status httpd
sudo nano /var/www/html/index.html
```

## Output

A custom webpage displaying:

**Welcome to DecodeLabs**

was successfully hosted on an AWS EC2 instance.
