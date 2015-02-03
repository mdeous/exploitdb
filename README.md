# exploitdb

Shell-style script to search exploit-db.com exploits.

## Introduction

There is already a similar script shipped with the Kali distribution, but I think it's not
flexible enough. This script is an attempt at providing a more flexible tool, with a fancy
shell-style interface.

## Features

* shell-style interface
* search in any field using
    * substring matching
    * regex matching
* update database and exploit files with the `updatedb` command
* commands completion (also completes values of the `platform`, `type` and `port` fields)
* highlighted search matches

## Usage

Just run the `exploitdb.py` script without any argument, you will be given a pseudo-shell interface.

If you are running the script for the first time, the script will automatically download the latest exploits 
archive at startup.

### Searching exploits

The `search` command allows you to search for a given pattern in any field of the original exploit-db's
CSV file. The search query must be in the form of `field_name:pattern` couples, if no field name is
given, `description` is the default.

Available fields are:
* `id` - the internal exploit's ID
* `file` - the path where the exploit file can be found
* `description` - informations about exploit and targetted software
* `date` - the date the exploit was released
* `author` - well, self-explanatory, huh?
* `platform` - the platform type the exploit runs on
* `type` - exploit classification, possible values are:
    * `local`
    * `shellcode`
    * `dos`
    * `remote`
    * `webapps`

If the pattern you want to search contains spaces, you can quote it using either single or double
quotes (see screenshot below).

It is also possible to search using a regular expression by enclosing your pattern in quotes
(simple or double) and prefixing it with 'r'.

To sum it up, here are the possible search formats:

* `description:zabbix` - single word substring search
* `description:'zabbix 2.'` / `description:"zabbix 2."` - quoted pattern substring search
* `description:r'za\w\wix'` / `description:r"za\w\wix"` - regular expression search

### Getting exploit infos

To show all the available details about an exploit, use the `info` command. This command takes a
single argument, which is the ID of the exploit you want details for.

### Updating database

Running the `updatedb` command will download the latest exploits archive from exploit-db.com and
extract it in an `exploits` folder in current directory.

## Screenshots

### search

![search1](http://i.imgur.com/520Dvoi.png)

![search2](http://i.imgur.com/AgY7lg1.png)

### info

![info](http://i.imgur.com/uSWTXlY.png)

### updatedb

![updatedb](http://i.imgur.com/IRMMgvW.png)

## Licensing

This script is under the FreeBSD (2-clause BSD) License.

