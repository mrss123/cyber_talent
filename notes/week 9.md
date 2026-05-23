## file upload vunl
### file upload functionality
#### common use case
- pp
- document upload 
- email attachment 
- media content 
- software package 
#### why those 
- path trasvesal 
- easily spoofed 
- untrusted files 
- executable  as image 
- uploads dirs
- insufficient validation 
-
#### how it handles 
- content validation 
	- client 
		- html 
		- extensions 
		- file size 
		- JS 
	- server 
		- extension whitelist and blacklist 
		- MIME meta data file format `Multipurpose Internet Mail Extensions`
		- file signature analysis 
		- file rename and stored on disk
		- web server if file is executable 
### common vulns 
- extension only checks
- weak content type verification 
- client side validation trust 
- executable upload directories 
#### file upload types 
**files upload + stored  XSS**
**file upload + HTML injection**
**file upload + information disclosure**


## RCE
remotely running a code 
cvss 9-10 critical (but not always)
no prior creds is asked 
gain admin control
ransomware
usually it is starting point 
might help to compromise the full system 

**how can we assist FILE UPLOAD for RCE**
- use PHP files 
- double extension 
- MIME confusion 
	- check the metadata and not the file content 
- mis-configured web server 

## file upload and web shell 

## file upload prevention 
- allow-list validation
- non-executable storage 
- randomize file name 
- file type limitation 
polyglot payload 
	using 2 different allowed extension on the same file 
