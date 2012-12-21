# iougen - IOU License Generator
iougen is a python module/cli script that can be ran to generate IOU license 
keys.

IOU stands for IOS on Unix and is a full IOS environment that can run as a 
Unix process.  IOU requires a valid key to operate and that is where this
module comes in.

The code used for generating the license code came from a user who goes by 
Kel.  Kel ported the code in 2011 from an original C program written in 2006.
I just cleaned it up and made it a package that could be imported for use in 
other projects (like a web front end)

## Installation
If you are using a version of Python prior to 2.7, you first need to install the 
argparse module. Python version 2.7 includes argparse in its  standard library.

	easy_install argparse

Clone the project:

	git clone https://github.com/bennetb01/iougen.git

Install the program

	cd iougen
	python setup.py install


## Command-line interface 
By default if you run the iougen script it will determine the current host's
hostname and hostid.  Just need to execute the script

	$ iougen
	Hostname    : theuglyone
	Host id     : 007f0101
	License Key : 20421f98ee8b3ed7
	
	Add the following text to ~/.iourc:
	[license]
	theuglyone = 20421f98ee8b3ed7;
	
	You can disable the phone home feature with something like:
	 echo '127.0.0.127 xml.cisco.com' >> /etc/hosts

If you are executing the script on a different host than the one you will be
using IOU on then you can manually specify the hostname and hostid via cli
arguments

	$ iougen --hostname theuglyone --hostid 007f0101
	Hostname    : theuglyone
	Host id     : 007f0101
	License Key : 20421f98ee8b3ed7
	
	Add the following text to ~/.iourc:
	[license]
	theuglyone = 20421f98ee8b3ed7;
	
	You can disable the phone home feature with something like:
	 echo '127.0.0.127 xml.cisco.com' >> /etc/hosts


## Using in your python modules
The iou module is very simple.  Please see the source of bin/iougen for a 
sample of how to generate iou licenses in your projects

## Note about IOU
If you run this script it is assumed that you have the legal right to posses 
and/or run IOU and that you have obtained IOU in a legal way.

The author of this script takes no responsibility for illegal actions.

I also do not know how you can obtain IOU so don't even ask!