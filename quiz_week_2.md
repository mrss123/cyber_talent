linux user management 
- crud users
	- passwd
	- shadow 
	- group
	- chown 
	- chmod 
what is package installation 
- adding new software 
- configs 
- libs
- documentations 
- sudo apt install 
- chmod + x 
- pacma for arch linux 
script installation 
- installing shell files
- curl
software installation
- git clone 
shell 
- place to tell computer what to do 
  terminal
types 
- or 
-`||`
  do this but if it fails do that instead 
- piping 
  hirarchy send the output of one command to other file as an input 
`cat file name | grep "error "`
`echo txt | base64 -d`

**home work answers** 
**task 1**
- chmod 640 file.txt
- chmod 755 file.txt
- chmod rw-rw-r --> 664 file.txt
- chmod 640 file.txt
- no because the cat permisson is revoked 
- file creation
  touch audit.txt
  chmod 750 audit.txt
- owner have full permission , group can read only , others can execute only
- sets perrmission like -r-x------ to the owner only
- 564

**task 2**

FLAG{ALWAYS_Check_Metadata}
FLAG{Strings_leak_information}
FLAG{appended_zip}     
FLAG{steghide_protected}
