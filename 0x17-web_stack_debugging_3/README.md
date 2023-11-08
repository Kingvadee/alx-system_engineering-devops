# AUTHOR:         DAVID OJEIFO[https://github.com/Kingvadee].
# COHORT:         13.
# Repo:           alx-system_engineering-devops.
# Directory: 	  0x17. Web stack debugging #3 :floppy_disk:

# Tasks :page_with_curl:


#For this project, we expect you to look at these concepts
 * Web Server [https://intranet.alxswe.com/concepts/17]
 * Web stack debugging[https://intranet.alxswe.com/concepts/68]


#https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png

 * When debugging, sometimes logs are not enough. Either because the software is breaking in a way that
was not expected and the error is not being logged, or because logs are not providing enough information.
In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

 * Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites…
It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some
point in your career.

 * Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

 * The web stack you are debugging today is a Wordpress website running on a LAMP stack.


#Requirements :page_with_curl:							      | # * Version.       |
 |---------------------------------------------------------------------------------------------------------|
 | 'Functions:'                                                                       | 'Versions'         |
 | 'All your files will be interpreted on'                                            | 'Ubuntu 14.04 LTS' |
 | 'All your files should end with a new line'                                        |                    |  
 | 'A README.md file at the root of the folder of the project is mandatory'           |                    |
 | 'Your Puppet manifests must pass puppet-lint,without any errors'                   | 'version 2.1.1'    |
 | 'Your Puppet manifests must run without error'                                     |                    |
 | 'Your Puppet manifests first line must be a comment explaining what the Puppet'    |                    |
 | 'manifest is about'				      				      |		           |
 | 'Your Puppet manifests files must end with the extension' 			      |       '.pp'        |
 | 'Files will be checked with Puppet'     			 	 	      | 'version 3.4'      |
 |---------------------------------------------------------------------------------------------------------|

#More Info:
#  */ *Install puppet-lint on your local machine using these commanda :floppy_disk:
 * $ apt-get install -y ruby
 * $ gem install puppet-lint -v 2.1.1


#Concepts :page_with_curl:


 *  **The concept for this project are**
   * Web Server [https://intranet.alxswe.com/concepts/17]
   * Web stack debugging[https://intranet.alxswe.com/concepts/68]
   * Non-exhaustive guide to debugging

#School specific :page_with_curl:

 * If you are struggling to get something right that is run on the checker,like a Bash script or a ethe flow by starting a Docker container with the distribution that isspecified in the requirements
concept page for more info.
#https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/45dffb0b1da8dc2ce47e340d7f88b0SBVO6H7D%2F20231108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231108T151558Z&X-Amz-Expirhost&X-A2ba8c61f78cd7914601656a715bf2

#Test and verify your assumptions :page_with_curl:


 * The idea is to ask a set of questions until you find the issue. For example, ifyou installed a wing the IP, here
are some questions you can ask yourself to start debugging:

 * Is the web server started? - You can check using the service manager, also double check by check
 * On what port should it listen? - Check your web server configuration
 * Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see
 * It is listening on the correct server IP? - netstat is also your friend here
 * Is there a firewall enabled?
 * Have you looked at logs? - usually in /var/log and tail -f is your friend
 * Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
