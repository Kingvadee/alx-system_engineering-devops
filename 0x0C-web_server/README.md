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
## ![image.png](file:///C:/Users/user/OneDrive/Pictures/Screenshots/NGINX_Ubuntu.png)

* **2. Setup a domain name**
  * [2-setup_a_domain_name](./2-setup_a_domain_name): A text file containing
  the domain name set up for the server through Gandi.
## ![image.jpg](https://c8.alamy.com/comp/2PRC3YN/miniature-people-and-toys-word-with-the-word-domain-name-2PRC3YN.jpg)

* **3. Redirection**
  * [3-redirection](./3-redirection): Bash script that configures a new Ubuntu
  machine with Nginx.
  * Setup is identical to [1-install_nginx_web_server](./1-install_nginx_web_server)
  plus:
    * The location `/redirect_me` returns a `301 Moved Permanently` redirection
    to another page.
## ![](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)

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
