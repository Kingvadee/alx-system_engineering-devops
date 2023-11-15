# AUTHOR:         [DAVID OJEIFO](https://github.com/Kingvadee).:briefcase:
# COHORT:         13.
# REPO:		  alx-system_engineering-devops.
# DIRECTORY:	  0x0C-web_server.:computer: :rocket: :gear:

# Concept :page_with_curl:

# ![Image.jpeg](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)
 * **For this project, we expect you to look at this concept:**
    * [What is a Child Process?](https://intranet.alxswe.com/concepts/110):book:
 * In this project, some of the tasks will be graded on 2 aspects:
    * 1.	Is your web-01 server configured according to requirements.
    * 2.	Does your answer file contain a Bash script that automatically
    	     	performs commands to configure an Ubuntu machine to fit
		requirements (meaning without any human intervention).
 * *For example, if I need to create a file '/tmp/test' containing the string
   'hello world' and modify the configuration of 'Nginx' to listen on port '8080'
    instead of '80', I can use 'emacs' on my server to create the file and to
    modify the Nginx configuration file '/etc/nginx/sites-enabled/default'.
 * *But my answer file would contain::bulb:
    |----------------------------------------------------------|
    | 'kingdave@ubuntu cat 88-script_example'		       |
    | '#!/usr/bin/env bash'				       |
    | '# Configuring a server with specification XYZ'	       |
    | 'echo hello world > /tmp/test'			       |
    | 'sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default'  |
    | 'kingdave@ubuntu'					       |
    |----------------------------------------------------------|
  
# The server is accessible at [bdbnb.site](http://bdbnb.site).

## Tasks :page_with_curl:

* **0. Transfer a file to your server**
  * [0-transfer_file](./0-transfer_file): Bash script that transfers a file
  from Holberton's client to a server.
  * Accepts four arguments:
    * The path of the file to be transferred.
    * The IP of the server to transfer the file to.
    * The username that `scp` connects with.
    * The path of the SSH privtae key that `scp` uses.
  * `scp` transfers the file to the user home directory `~/`.

* **1. Install nginx web server**
  * [1-install_nginx_web_server](./1-install_nginx_web_server): Bash script
  that configures a new Ubuntu machine with Nginx.
  * Nginx listens on port 80.
  * When querying Nginx at its root `/` with a `curl` GET request,
  it returns a page containing the string `Holberton School`.

* **2. Setup a domain name**
  * [2-setup_a_domain_name](./2-setup_a_domain_name): A text file containing
  the domain name set up for the server through Gandi.

* **3. Redirection**
  * [3-redirection](./3-redirection): Bash script that configures a new Ubuntu
  machine with Nginx.
  * Setup is identical to [1-install_nginx_web_server](./1-install_nginx_web_server)
  plus:
    * The location `/redirect_me` returns a `301 Moved Permanently` redirection
    to another page.

* **4. Not found page 404**
  * [4-not_found_page_404](./4-not_found_page_404): Bash script that configures
  a new Ubuntu machine with Nginx.
  * Setup is identical to [1-install_nginx_web_server](./1-install_nginx_web_server)
  plus:
    * Features a custom 404 page containing the string `Ceci n'est pas une page`.

* **5. Design a beautiful 404 page**
  * A custom-designed 404 error page for my server, accessible at
  [bdbnb.site/404](http://bdbnb.site/404).

* **6. Deploy fast, deploy well**
  * [fabfile.py](./fabfile.py): A Python Fabric configuration file defining
  the following functions:
  * `pack`
    * Usage: `fabric pack`
    * Creates a tar gzipped archive of the current directory named
    `holbertonwebapp.tar.gz` in the local directory.
  * `deploy`
    * Usage: `fabric -H <remote server IP> deploy`
    * Uploads the archive `holbertonwebapp.tar.gz` to the `/tmp`
    directory of the remote server.
    * Creates the directory `/tmp/holbertonwebapp` in the remote server.
    * Untars `holbertonwebapp.tar.gz` in the `/tmp/holbertonwebapp` directory
    of the remote server.
  * `clean`
    * Deletes the archive `holbertonwebapp.tar.gz` in the local directory.
