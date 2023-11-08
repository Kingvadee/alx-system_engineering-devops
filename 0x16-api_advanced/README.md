# AUTHOR:         DAVID OJEIFO[https://github.com/Kingvadee].
# COHORT:         13.
# Repo:           alx-system_engineering-devops.
# Directory: 	  0x13-firewall

# Tasks :page_with_curl:

#https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png

# Background Context :page_with_curl:


	Questions involving APIs are common for interviews. Sometimes they’re as simple
 as‘write a Python script that queries a given endpoint’, sometimes they require
you to use recursive functions and format/sort the results.
	A great API to use for some practice is the Reddit API. There’s a lot of
endpoints available, many that don’t require any form of authentication, and
there’s tons of information to be parsed out and presented. Getting comfortable
with API calls now can save you some face during technical interviews and even
outside of the job market, you might find personal use cases to make your life a
little bit easier.



# Resources :page_with_curl:


 #Reddit API Documentation[https://www.reddit.com/dev/api/#GET_api_me.json]

 #Query String[https://en.wikipedia.org/wiki/Query_string]

This project will cover:
How to read API documentation to find the endpoints you’re looking for
How to use an API with pagination
How to parse JSON results from an API
How to make a recursive API call
How to sort a dictionary by value


# Requirements :page_with_curl:


Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
Libraries imported in your Python files must be organized in alphabetical order
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use the Requests module for sending HTTP requests to the Reddit API

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files for all tasks. Provided by Holberton
School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File           | Prototype                               |
| -------------- | --------------------------------------- |
| `0-subs.py`    | `def number_of_subscribers(subreddit)`  |
| -------------- | --------------------------------------- |
| `1-top_ten.py` | `def top_ten(subreddit)`                |
| -------------- | --------------------------------------- |
| `2-recurse.py` | `def recurse(subreddit, hot_list=[])`   |
| -------------- | --------------------------------------- |
| `100-count.py` | `def count_words(subreddit, word_list)` |
| -------------- | --------------------------------------- |



| ------------------------------------------------------------------------------|
	* **0. How many subs?**
  * [0-subs.py](./0-subs.py): Python function that returns the total number of
  subscribers for a given subreddit.
  * Returns `0` if an invalid subreddit is given.

* **1. Top Ten**
  * [1-top_ten.py](./1-top_ten.py): Python function that prints the top ten
  hottest posts for a given subreddit.
  * Prints `None` if an invalid subreddit is given.

* **2. Recurse it!**
  * [2-recurse.py](./2-recurse.py): Python function that recursively returns a
  list of titles for all hot articles on a given subreddit.
  * Returns `None` if no results are found on the given subreddit.

* **3. Count it!**
  * [100-count.py](./100-count.py): Python function that recursively prints a
  sorted count of given keywords parsed from titles of all hot articles on a given
  subreddit.
  * Keywords are case-insensitive and delimited by spaces.
  * Results are printed in descending order by count.
  * Words with identical counts are sorted alphabetically.
  * Words with no matches are skipped.
  * Results are based on the number of times a keyword appears - ie.,
  `java java java` counts as three separate instances of `java`.

