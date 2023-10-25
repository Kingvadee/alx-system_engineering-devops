# AUTHOR:         DAVID OJEIFO[https://github.com/Kingvadee].
# COHORT:         13.
# Repo:           alx-system_engineering-devops.
# Directory: 	  0x13-firewall

## Tasks :page_with_curl:

# 0. Block all incoming traffic but
Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:

The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)
Share the ufw commands that you used in your answer file

# 1. Port forwarding
Firewalls can not only filter requests, they can also forward them.

Requirements:

Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
Your answer file should be a copy of the ufw configuration file that you modified to make this happen
Terminal in web-01:
