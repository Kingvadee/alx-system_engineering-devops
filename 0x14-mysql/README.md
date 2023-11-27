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
##### ![Image.png](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png)

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
#### **0. Install MySQL**
 * First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
 * 	MySQL distribution must be 5.7.x
 * 	Make sure that `task #3` of your `SSH project` is completed for `web-01` and `web-02`. The checker will connect to your servers to check MySQL status.
 * 	Please make sure you have your `README.md` pushed to `GitHub`.
##### 	EXAMPLE:
   	|-----------------------------------------------------------------------------|
   	| ubuntu@229-web-01:~$ mysql --version					      |
   	| mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper |
   	| ubuntu@229-web-01:~$							      |

#### **1. Let us in!**
 * In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.
 *	 Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
 * 	Make sure that `holberton_user` has permission to check the primary/replica status of your databases.
 * 	In addition to that, make sure that `task #3` of your `SSH project` is completed for `web-01` and `web-02`. **You will likely need to add the public key to `web-02` as you only added it to `web-01` for this project.** The checker will connect to your servers to check MySQL status.
##### 	EXAMPLE:
   	|-------------------------------------------------------------------------------------------------|
   	| ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"|
	| Enter password:										  |
   	| Grants for holberton_user@localhost                             				  |
   	| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' 				  |
   	| ubuntu@229-web-01:~$										  |

#### **2. If only you could see what I've seen with your eyes**
 * 	In order for you to set up replication, you’ll need to have a `database` with at least one table and one row in your primary MySQL server (`web-01`) to replicate from.
 * 	Create a database named `tyrell_corp`.
 * 	Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
 * 	Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.
##### 	EXAMPLE:
  	|-----------------------------------------------------------------------------------------|
 	|ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"|
	|Enter password:									  |
   	| id | name   										  |
   	|----|------------------------------------------------------------------------------------|
  	|  1 | Leon  										  |
   	|----|------------------------------------------------------------------------------------|
   	|ubuntu@229-web-01:~$									  |

#### **3. Quite an experience to live in fear, isn't it?**
 * 	Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.
 * 	The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like.
 * 	`replica_user` must have the appropriate permissions to replicate your primary MySQL server.
 * 	`holberton_user` will need SELECT privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.
##### 	EXAMPLE:
	|--------------------------------------------------------------------------------------------------|
	| ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user' |
	| user             | Repl_slave_priv 								   |
	| root             | Y               								   |
	| mysql.session    | N               								   |
	| mysql.sys        | N               								   |
	| debian-sys-maint | Y               								   |
	| holberton_user   | N               								   |
	| replica_user     | Y               								   |
	|ubuntu@229-web-01:~$										   |

#### **4. Setup a Primary-Replica infrastructure using MySQL**
##### ![image.png](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/09e83e914f0d6865ce320a47f2f14837a5b190b6.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231126T005747Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4969d2d592394c788b8eaf0308ecb962cddbc0cd99d0190492cbed77952e057b)
 * 	Having a replica member on for your MySQL database has 2 advantages:
	* Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data.
	* Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed.
###### Requirements:
	* MySQL primary must be hosted on `web-01` - do not use the `bind-address`, just comment out this parameter
	* MySQL replica must be hosted on `web-02`
	* Setup replication for the MySQL database named `tyrell_corp`
	* Provide your MySQL primary configuration as answer file(`my.cnf` or `mysqld.cnf`) with the name `4-mysql_configuration_primary`
	* Provide your MySQL replica configuration as an answer file with the name `4-mysql_configuration_replica`
###### Tips:bulb:
	* Once MySQL replication is setup, add a new record in your table via MySQL on web-01 and check if the record has been replicated in MySQL web-02. If you see it, it means your replication is working!
	* **Make sure that UFW is allowing connections on port 3306 (default MySQL port) otherwise replication will not work.**

##### EXAMPLE 1:
	| 						**web-01**						|
	|-------------------------------------------------------------------------------------------------------|
	| ubuntu@web-01:~$ mysql -uholberton_user -p								|
	| Enter password: 											|
	| Welcome to the MySQL monitor.  Commands end with ; or \g.						|
	| Your MySQL connection id is 1467									|
	| Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)							|
	| Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.				|
	| Oracle is a registered trademark of Oracle Corporation and/or its					|
	| affiliates. Other names may be trademarks of their respective owners.					|
	| Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.			|
	| mysql> show master status;										|
	| File             | Position | Binlog_Do_DB       | Binlog_Ignore_DB 					|
	| mysql-bin.000009 |      107 | tyrell_corp        |                 					|
	| 1 row in set (0.00 sec)										|
	| mysql>												|
	|-------------------------------------------------------------------------------------------------------|

##### EXAMPLE 2:
	|						**web-02**						|
	|-------------------------------------------------------------------------------------------------------|
	| root@web-02:/home/ubuntu# mysql -uholberton_user -p							|
	| Enter password:											|
	| Welcome to the MySQL monitor.  Commands end with ; or \g.						|
	| Your MySQL connection id is 53									|
	| Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)							|
	| Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.				|
	| Oracle is a registered trademark of Oracle Corporation and/or its affiliates.				|
	| Other names may be trademarks of their respective owners.						|
	| Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.			|
	| mysql> show slave status\G										|
	| *************************** 1. row ***************************					|
	| 		 Slave_IO_State: Waiting for master to send event					|
	| 		    Master_Host: 158.69.68.78								|
	|		    Master_User: replica_user								|
	|		    Master_Port: 3306									|
	|		  Connect_Retry: 60									|
	|		Master_Log_File: mysql-bin.000009							|
	|	    Read_Master_Log_Pos: 107									|
	|   	         Relay_Log_File: mysql-relay-bin.000022							|
	|		  Relay_Log_Pos: 253									|
	|	  Relay_Master_Log_File: mysql-bin.000009							|
	|	       Slave_IO_Running: Yes									|
	| 	      Slave_SQL_Running: Yes									|
