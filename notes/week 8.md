## advanced tricky tips 
- http parameter pollution 
	- sending one parameter twice and the paramater validates the second ID by the first ID 
- UUID 

| Attack              | What is tried          | Against how many accounts | Goal                       |
| ------------------- | ---------------------- | ------------------------- | -------------------------- |
| Brute Force         | Many passwords         | One account               | Break a specific account   |
| Credential Stuffing | Known leaked passwords | Many accounts             | Reuse breached credentials |
| Password Spraying   | One common password    | Many accounts             | Avoid lockouts             |
- broken MFA 
	when attacker bypassing the second or third authenticator 
	password + OTP + biometris 

	methods 
		sim swaping 
		brute-force the OTP
		check if the set session on the to use as a OTP
		find for implementation error 
- session FLAWS 
	- basics
		- HTTP-ONLY
			- to limit JS
			- cookie theft 
		- SECURE 
			- only over HTTPS 
			- might be true or false 
		- SAME SITE 
			- strict - only same-site requests  (if the site sends only)
			- lax - limited cross site ()
			- none - allows cross -site but mus be secure 
	- session hijacking 
		methods 
		- bruteforce 
		- idor 
	- session fixation 
		- when we the authenticate uses same cookie from another user 
		- when the session is not rotated 
		- when the system uses same session even if after login 
## injection 
- don't have a specific part 
	- SQL injection
		- structured query language
		- have CRUD 
		- we usually run around select where the user inputs a data 
		- most common attacking statements are based on the command `where`
		- common places 
			  user agent 
			  login page 
			  search bars 
			  on the url 
		- types 
			- second order 
			- error based SQL 
				- trying to exploit based on the error and it might leak more than intended 
				- show raw database error 
			- boolean based 
				- playing with true or false 
			- out of band 
				- no visible database output attacker infers results indirectly 
			- time based 
				- every tables have different time to response but we don't know whether executes so we will embade different time it it works according to it 
		
		- usage 
			- `  'OR 1=1 --  `    ` ' AND 1=1 -- `
			- `ORDER BY` to see the number of columns
			- `UNION SELECT ` 
				- `UNION SELECT 'X''X''X''X''X'`
				- bring those things in addition to what we asked for 
			- xp command shell
		- prevention 
			- principle of least privilage 
			- error handling
			- prepared statement 
			- prepared statements 
	- XSS  (cross site scripting)
		- malicious JS running on the target
		- TYPES
			- Dom XSS 
				- using document 
			- stored 
				- malicious link stored on the server 
			- reflected
				- reflects immediately 
			- blind 
				- by collaboration 
		- scripts 
			`<script> alert <script>`
			`<img src=x onerror = alert(1)>
			- git hub
			- portswiger `
		- where to see 
			- simple search if it brings what we searched for 
			- any where the user inputs
				- URL (reflected xss)
				- FROM INPUTS ( stored xss)
				- HTTP HEADER 
		- USAGE 
			- password stealing 
			- session hijacking 
			- keyboard logger 
			- phishing 
			- redirect 
			- admin privilege escalation 
		- prevention 
			- out put encoding 
			- input sanitization 
			- contetn security policy 
			- framework protections
			- HTTPOnly cookies 
