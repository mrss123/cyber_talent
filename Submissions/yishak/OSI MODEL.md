**question** 
what are the 7 OSI model layers and how can they be attacked?

OSI stands for **open system interconnection** 
it is a conceptual frame work that lets a connection be seccesfull

## 1. Application layer 

it directly interacts with end user software appication like web browsers or email clints to initate network services 

it can be attacked by 

- *sql injection*
- *xss*
- *HTTPFlood*
- *DNS poisoning*

## 2. presentation layer 

it translate encrypts commress and formasts data into syntax the application layer can understand 

it can be attacked by 

- *ssl/tls exploit*
- *data interception*

## 3. session layer 

it manages sessions between application and different devices 

it can be attacked by 

 - *session hajacking*
 - *man in the middle*

## 4. transport layer 

 it control communication using TCP and UDP

 it can be attacked by

 - *TCP SYN flood*
 - *UDP Flooding*
 - *port probing*

## 5. Network laver 

it handels logical addressing and routing packets across different networks 

it can be attacked by 

- *Ip spoofing*
- *ICMP flooding or Dos*
- *Route injection*

## 6. data link layer 

it manages a node to node data packet transfer 

it can be attacked by

- *MAC spoofing*
- *ARP spoofing*
- *MAC flooding*

## 7. physical layer 

it handels transmits raw bitstrams (0 and 1) over physical hardware 
- cables
- switches
- network adabters

it can be attacked by

- *Jamming*
- *wire tapping*
- *tampering*

