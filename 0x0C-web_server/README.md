# AUTHOR:         [DAVID OJEIFO](https://github.com/Kingvadee).:briefcase:
# COHORT:         13.
# REPO:		  alx-system_engineering-devops.
# DIRECTORY:	  0x0C-web_server.:computer: :rocket: :gear:

# Concept :page_with_curl:

# ![Image.png](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)
 * **For this project, we expect you to look at this concept:**
    * [What is a Child Process?](https://intranet.alxswe.com/concepts/110):book:
 * In this project, some of the tasks will be graded on 2 aspects:
    * 1.	Is your web-01 server configured according to requirements.
    * 2.	Does your answer file contain a Bash script that automatically
    	     	performs commands to configure an Ubuntu machine to fit
		requirements (meaning without any human intervention).
 * *For example, if I need to create a file `/tmp/test` containing the string
   `hello world` and modify the configuration of 'Nginx' to listen on port `8080`
    instead of `80`, I can use `emacs` on my server to create the file and to
    modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.
 * *But my answer file would contain::bulb:
    |----------------------------------------------------------|
     `kingdave@ubuntu cat 88-script_example`		       
     `#!/usr/bin/env bash`				       
     `# Configuring a server with specification XYZ`	       
     `echo hello world > /tmp/test`			       
     `sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default`
     `kingdave@ubuntu`					       

# ![Image.jpg](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)
 * *As you can tell, I am not using emacs to perform the task in my answer file.
    This exercise is aiming at training you on automating your work. If you can
    automate tasks that you do manually, you can then automate yourself out of
    repetitive tasks and focus your energy on something more interesting.
    For an SRE, that comes very handy when there are hundreds or thousands of
    servers to manage, the work cannot be only done manually. Note that the
    checker will execute your script as the root user, you do not need to use
    the sudo command.*

 * *A good `Software Engineer` is a [lazy Software Engineer.](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb)*
 * **Tips: to test your answer Bash script, feel free to reproduce the checker environment:**
 * 	start a `Ubuntu 16.04` sandbox.
 * 	run your script on it.
 * 	see how it behaves.
##	RESOURCES:book::globe_with_meridians::link:
 * 	[How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works):globe_with_meridians::gear:
 * 	[Nginx](https://en.wikipedia.org/wiki/Nginx)
 * 	[How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
 * 	[Child process concept page](https://intranet.alxswe.com/concepts/110)
 * 	[Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
 * 	[HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
 * 	[HTTP redirection](https://moz.com/learn/seo/redirection)
 * 	[Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
 * 	[Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
###	 For reference:bulb:
 *	 [RFC 7231 HTTP/1.1](https://datatracker.ietf.org/doc/html/rfc7231)
 *	 [RFC 7540 HTTP/2](https://datatracker.ietf.org/doc/html/rfc7540)

 * *man or help:*
    `scp`
    `curl`
## Learning Objectives:
 * **At the end of this project, you are expected to be able to explain to anyone, without the help of [Google](https://www.google.com):**
 * `What is the main role of a web server`
 * `What is a child process`
 * `Why web servers usually have a parent process and child processes`
 * `What are the main HTTP requests`
## **DNS**
 * `What DNS stands for`
 * `What is DNS main role`

# DNS Record Types:bulb::page_with_curl:
 * `A`
 * `CNAME`
 * `TXT`
 * `MX`

### Requirements:
 * Allowed editors: `vi`, `vim`, `emacs`.
 * All your files will be interpreted on `Ubuntu 16.04 LTS`.
 * All your files should end with a new line `\n`.
 * A `README.md` file, at the root of the folder of the project, is mandatory
 * All your `Bash` script files must be `executable` (`chmod`)
 * Your `Bash` script must pass Shellcheck (`version 0.3.7`) without any error
 * The first line of all your `Bash` scripts should be exactly `#!/usr/bin/env bash`
 * The second line of all your Bash scripts should be a `comment` explaining what is the script doing
 * You can’t use `systemctl` for restarting a process

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
## ![image.png](https://media.istockphoto.com/id/1188883674/vector/file-transfer-concept-vector-illustration.jpg?s=1024x1024&w=is&k=20&c=MqAzPzD3eaLdHAZ-RmAIA8kSQbhf6r3KUc2z-7Lwf28=)

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
