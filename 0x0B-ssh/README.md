UTHOR:         [DAVID OJEIFO](https://github.com/Kingvadee).:briefcase:
# COHORT:         13.
# REPO:		  alx-system_engineering-devops.
# DIRECTORY:	  0x0B-ssh :globe_with_meridian: :link: :gear:

##Concept :page_with_curl:

# ![image.gif](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif)

 * Along with this project, you have been attributed an `Ubuntu` server, living in a datacenter far far away. Like level 2 of the application process, you will connect using `ssh`. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of [a previous project](https://intranet.alxswe.com/tasks/1223) shared in your [intranet profile](https://).

 * You can access your server information in the my servers section of the intranet, each line with contains the `IP` and `username` you should use to connect via `ssh`.

 **Note:** Your server is configured with an `Ubuntu 20.04 LTS` environment.

## Resources: :book:
 * [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
 * [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
 * [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
 * [SSH Config File](https://www.ssh.com/academy/ssh/config)
 * [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
 * [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
 * [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc)(Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

### For reference: :bulb:
 * [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
 * [Secure Shell Wiki](https://intranet.alxswe.com/rltoken/SpiYWE79Yfr_vWDg42dzCw)
 * [IETF RFC 4251 (Description of the SSH Protocol)](https://intranet.alxswe.com/rltoken/f2O0OQq9tch2MYeNAzkg5w)
 * [Internet Engineering Task Force](https://intranet.alxswe.com/rltoken/gd1W1UvB0KeJVWwM8BLvhA)
 * [Request for Comments](https://intranet.alxswe.com/rltoken/jb-IrnQnUh-PsEDlbAU0Kw)

* **man or help:**
 `ssh`
 `ssh-keygen`
 `env`

## Learning Objectives: :book: :rocket:
 * What is a Server?
 * Where Servers usually live.
 * What is SSH?
 * How to create an SSH RSA key pair.
 * The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

### Requirements:
Allowed editors: `vi`, `vim`, `emacs`
All your files will be interpreted on `Ubuntu 20.04 LTS`.
All your files should end with a new line(`\n`)
A `README.md` file, at the `root` of the folder of the project, is mandatory
All your `Bash` script files must be `executable`.
The first line of all your `Bash` scripts should be exactly `#!/usr/bin/env bash`
The second line of all your `Bash` scripts should be a `comment` explaining what is the script doing.

## 0. Use a private key
 * Write a `Bash` script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

 *  **Requirements:**
 *   Only use `ssh` single-character `flags`.
 *   You cannot use `-l`
 *   You do not need to handle the case of a private key protected by a `passphrase`

## 1. Create an SSH key pair
 * Write a `Bash` script that creates an `RSA` key pair.

 * **Requirements:**
 * Name of the created private key must be `school`
 * Number of `bits` in the created key to be created `4096`
 * The created key must be protected by the passphrase `betty`
### Example:
kingdave@ubuntu$ ls
1-create_ssh_key_pair
kingdave@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
kingdave@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
kingdave@ubuntu$ 


## 2. Client configuration file
 * Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

 * **Requirements:**
 * Your `SSH` client configuration must be configured to use the private key `~/.ssh/school`
Your `SSH` client configuration must be `configured` to refuse to authenticate using a `password`


## 3. Let me in!
 * Now that you have successfully connected to your `server`, we would also like to join the party.
 * Add the `SSH` public key Provided in this task to your `server` so that we can connect using the `ubuntu` user.


## 4. Client configuration file (w/ Puppet)
 * Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
### Requirements:
Your `SSH` client configuration must be `configured` to use the private key `~/.ssh/school`.
Your `SSH` client configuration must be `configured` to refuse to authenticate using a `password`.
