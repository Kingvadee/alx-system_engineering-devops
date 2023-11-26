# AUTHOR:         [DAVID OJEIFO](https://github.com/Kingvadee).:briefcase:
# COHORT:         13.
# REPO:		  alx-system_engineering-devops.
# DIRECTORY:	  0x14-mysql.:computer:

# For this project i will be looking at the following Concept :page_with_curl::link:
 * [Database administration](https://intranet.alxswe.com/concepts/49)
 * [Web stack debugging](https://intranet.alxswe.com/concepts/68)
 * [How to Install mysql 5.7](https://intranet.alxswe.com/concepts/100002)
 * [What is a primary-replica cluster](https://intranet.alxswe.com/rltoken/eojqG9FZbA6QVWN5P9cLzA)
 * [MySQL primary replica setup](https://intranet.alxswe.com/rltoken/z2KVk2UKLMc0RvHMdJmYLg)
 * [Build a robust database backup strategy](https://intranet.alxswe.com/rltoken/BharnxaLb-BDDYFywzME2Q)
# ![Image.png](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png)

 * **man or help:**
 * `mysqldump`

 * At the end of this project, i was able to understand,
 * 	What the main role of a database is.
 * 	What a database replica is.
 * 	The purpose of a database replica.
 * 	Why database backups is needed to be stored in different physical locations.
 * 	What operation i should regularly perform to make sure that my database backup strategy actually works.

#### Requirements:floppy_disk:
 * Allowed editors: `vi`, `vim`, `emacs`
 * All your files will be interpreted on `Ubuntu 16.04 LTS`
 * All your files should end with a new line
 * A `README.md` file, at the `root` of the folder of the project, is mandatory
 * All your `Bash script` files must be `executable`
 * Your `Bash script` must pass `Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get)` without any error
 * The first line of all your `Bash scripts` should be exactly `#!/usr/bin/env bash`
 * The second line of all your `Bash scripts` should be a `comment` explaining what is the `script` doing

## TASKS:book:
 * **0. Install MySQL**
 First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
 * 	MySQL distribution must be 5.7.x
 * 	Make sure that `task #3` of your `SSH project` is completed for `web-01` and `web-02`. The checker will connect to your servers to check MySQL status.
 * 	Please make sure you have your `README.md` pushed to `GitHub`.
 * 	EXAMPLE:
   	ubuntu@229-web-01:~$ mysql --version
   	mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
   	ubuntu@229-web-01:~$
 * **1. Let us in!**
In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.
 *	 Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
 * 	Make sure that `holberton_user` has permission to check the primary/replica status of your databases.
 * 	In addition to that, make sure that `task #3` of your `SSH project` is completed for `web-01` and `web-02`. **You will likely need to add the public key to `web-02` as you only added it to `web-01` for this project.** The checker will connect to your servers to check MySQL status.
#### 	EXAMPLE:
   	|------------------------------------------------------------------------------------------------|
   	|ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"|
	|Enter password:										 |
   	| Grants for holberton_user@localhost                             				 |
   	| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' 				 |
   	|ubuntu@229-web-01:~$										 |

 * **2. If only you could see what I've seen with your eyes**
 * 	In order for you to set up replication, you’ll need to have a `database` with at least one table and one row in your primary MySQL server (`web-01`) to replicate from.
 * 	Create a database named `tyrell_corp`.
 * 	Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
 * 	Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.
#### 	EXAMPLE:
  	|-----------------------------------------------------------------------------------------|
 	|ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"|
	|Enter password:									  |
   	| id | name   										  |
   	|----|------------------------------------------------------------------------------------|
  	|  1 | Leon  										  |
   	|----|------------------------------------------------------------------------------------|
   	|ubuntu@229-web-01:~$									  |

 * **3. Quite an experience to live in fear, isn't it?**
