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

## what is OSI Model
**The 7 Layers of the OSI Model (Top to Bottom)**

1. **[Application Layer](https://www.google.com/search?client=firefox-b-e&channel=entpr&q=Application+Layer&mstk=AUtExfCJhvRWnDaBs0DsenfBt8v6vZLcwJgA9zroUjpV4Ip-DeVTc7v7MPEZjRMyBA5-LGWR_OyIY4KDPHi1ZYAfvjBf4LSuqWKXvPozIB3PUMicjwFzshTyl7cClASYFDs0FqE&csui=3&ved=2ahUKEwjCuICVrrOTAxXY0AIHHWFEDm0QgK4QegYIAQgCEAE) (Layer 7):** Enables user interaction with network services (e.g., browsers, email).
2. **[Presentation Layer](https://www.google.com/search?client=firefox-b-e&channel=entpr&q=Presentation+Layer&mstk=AUtExfCJhvRWnDaBs0DsenfBt8v6vZLcwJgA9zroUjpV4Ip-DeVTc7v7MPEZjRMyBA5-LGWR_OyIY4KDPHi1ZYAfvjBf4LSuqWKXvPozIB3PUMicjwFzshTyl7cClASYFDs0FqE&csui=3&ved=2ahUKEwjCuICVrrOTAxXY0AIHHWFEDm0QgK4QegYIAQgCEAM) (Layer 6):** Handles data formatting, encryption, and compression.
3. **[Session Layer](https://www.google.com/search?client=firefox-b-e&channel=entpr&q=Session+Layer&mstk=AUtExfCJhvRWnDaBs0DsenfBt8v6vZLcwJgA9zroUjpV4Ip-DeVTc7v7MPEZjRMyBA5-LGWR_OyIY4KDPHi1ZYAfvjBf4LSuqWKXvPozIB3PUMicjwFzshTyl7cClASYFDs0FqE&csui=3&ved=2ahUKEwjCuICVrrOTAxXY0AIHHWFEDm0QgK4QegYIAQgCEAU) (Layer 5):** Manages, maintains, and terminates connections between applications.
4. **[Transport Layer](https://www.google.com/search?client=firefox-b-e&channel=entpr&q=Transport+Layer&mstk=AUtExfCJhvRWnDaBs0DsenfBt8v6vZLcwJgA9zroUjpV4Ip-DeVTc7v7MPEZjRMyBA5-LGWR_OyIY4KDPHi1ZYAfvjBf4LSuqWKXvPozIB3PUMicjwFzshTyl7cClASYFDs0FqE&csui=3&ved=2ahUKEwjCuICVrrOTAxXY0AIHHWFEDm0QgK4QegYIAQgCEAc) (Layer 4):** Ensures accurate, ordered data delivery (e.g., TCP or UDP).
		TCP (Transmission Control Protocol) 
		UDP (User Datagram Protocol) are ==foundational transport-layer protocols for data transmission over networks==.
5. **[Network Layer](https://www.google.com/search?client=firefox-b-e&channel=entpr&q=Network+Layer&mstk=AUtExfCJhvRWnDaBs0DsenfBt8v6vZLcwJgA9zroUjpV4Ip-DeVTc7v7MPEZjRMyBA5-LGWR_OyIY4KDPHi1ZYAfvjBf4LSuqWKXvPozIB3PUMicjwFzshTyl7cClASYFDs0FqE&csui=3&ved=2ahUKEwjCuICVrrOTAxXY0AIHHWFEDm0QgK4QegYIAQgCEAk) (Layer 3):** Determines the best physical path (routing) for data using IP addresses.
6. **[Data Link Layer](https://www.google.com/search?client=firefox-b-e&channel=entpr&q=Data+Link+Layer&mstk=AUtExfCJhvRWnDaBs0DsenfBt8v6vZLcwJgA9zroUjpV4Ip-DeVTc7v7MPEZjRMyBA5-LGWR_OyIY4KDPHi1ZYAfvjBf4LSuqWKXvPozIB3PUMicjwFzshTyl7cClASYFDs0FqE&csui=3&ved=2ahUKEwjCuICVrrOTAxXY0AIHHWFEDm0QgK4QegYIAQgCEAs) (Layer 2):** Facilitates node-to-node data transfer and manages MAC addresses.
7. **[Physical Layer](https://www.google.com/search?client=firefox-b-e&channel=entpr&q=Physical+Layer&mstk=AUtExfCJhvRWnDaBs0DsenfBt8v6vZLcwJgA9zroUjpV4Ip-DeVTc7v7MPEZjRMyBA5-LGWR_OyIY4KDPHi1ZYAfvjBf4LSuqWKXvPozIB3PUMicjwFzshTyl7cClASYFDs0FqE&csui=3&ved=2ahUKEwjCuICVrrOTAxXY0AIHHWFEDm0QgK4QegYIAQgCEA0) (Layer 1):** Transmits raw, unstructured data over physical media (cables, Wi-Fi).
