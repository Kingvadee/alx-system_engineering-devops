# AUTHOR:         [DAVID OJEIFO](https://github.com/Kingvadee).:briefcase:
# COHORT:         13.
# REPO:		  alx-system_engineering-devops.
# DIRECTORY:	  Web stack debugging #0.:computer: :gear:

# Concept :page_with_curl:
 * This was the first in a series of web stack debugging projects. In these
projects, I was given broken/bugged webstacks in isolated containers,
and tasked with fixing the web stack to a working state. For each
task, I wrote a script automating the commands necessary to fix the
web stack.
 * RESOURCES FOR THE CONCEPT:bulb: :book: :link:
 * [Network basics](https://intranet.alxswe.com/concepts/33)
 * [Docker](https://intranet.alxswe.com/concepts/65)
 * [Web Stack Debugging](https://intranet.alxswe.com/concepts/68)
### ![image.png](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/265/uWLzjc8.jpg)

### Background Context:book:
 * The Webstack debugging series will train you in the art of debugging.
   Computers and software rarely work the way we want (that’s the `fun`
   part of the job!).
 * Being able to debug a webstack is essential for a Full-Stack Software
   Engineer, and it takes practice to be a master of it.
 * In this debugging series, broken/bugged webstacks will be given to you,
   the final goal is to come up with a Bash script that once executed, will
   bring the webstack to a working state. But before writing this Bash
   script, you should figure out what is going on and fix it manually.

 * Let’s start with a very simple example. My server must:
 * 1.	have a copy of the `/etc/passwd` file in `/tmp`
 * 2.	have a file named `/tmp/isworking` containing the string `OK`.
#### Let’s pretend that without these 2 elements, my web application cannot work.
 * Let’s go through this example and fix the server.
 * 	vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
 * 	Unable to find image 'ubuntu:14.04' locally
 * 	14.04: Pulling from library/ubuntu
 * 	34667c7e4631: Already exists
 * 	d18d76a881a4: Already exists
 * 	119c7358fbfc: Already exists
 * 	2aaf13f3eff0: Already exists
 * 	Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
 * 	Status: Downloaded newer image for ubuntu:14.04
 *	76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
 * 	vagrant@vagrant:~$ docker ps
 * 	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
 * 	76f44c0da25e        ubuntu:14.04        "/bin/bash"         13 seconds ago      Up 12 seconds                           infallible_bhabha
 * 	vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
 * 	root@76f44c0da25e:/# ls /tmp/
 * 	root@76f44c0da25e:/# cp /etc/passwd /tmp/
 * 	root@76f44c0da25e:/# echo OK > /tmp/isworking
 * 	root@76f44c0da25e:/# ls /tmp/
 * 	isworking  passwd
 * 	root@76f44c0da25e:/#
 * 	vagrant@vagrant:~$
 *  Then my answer file would contain:
 * 	sylvain@ubuntu:~$ cat answerfile
 * 	#!/usr/bin/env bash
 * 	# Fix my server with these magic 2 lines
 * 	cp /etc/passwd /tmp/
 * 	echo OK > /tmp/isworking
 * 	sylvain@ubuntu:~$
Note that as you cannot use interactive software such as emacs or vi in your Bash script, everything needs to be done from the command line (including file edition).

## Tasks :page_with_curl:

* **0. Give me a page!**
  * [0-give_me_a_page](./0-give_me_a_page): Bash script that runs Apache on a
  web server and gets it to respond to queries to the root.
