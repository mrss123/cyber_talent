reverse engineering
reverse engineering research 

---
definition 
	**Reverse engineering** (also known as **backwards engineering** or **back engineering**) is a process or method through which one attempts to understand through  deductive reasoning how a previously made device, process, system, or piece of software accomplishes a task with very little (if any) insight into exactly how it does so. Depending on the system under consideration and the technologies employed, the knowledge gained during reverse engineering can help with repurposing obsolete objects, doing security analysis, or learning how something works

---
three basic steps
	information extraction
	modeling
	review

---
reasons to do reverse E
	analysis of hardware 
	commercial activities ***competitor product analysis***
	re-documentation of a legacy system
	understand system
	recover a lost data 
	sec-analysis ans vul detection 
	maintenance debugging and system improvement 
	
----
levels
	component level 
	pattern level 
	statement level 
	program level : internal data structures (identify and define classes of objects )
		approach: examine each variables 
		common indicators: structures 
							record 
							files 
							list 
							arrays 
	system level : global data structure 
		database structures 
			understanding existing schema before redesigning or migrating them 
			steps 
				build initial object model : create model based on existing DB 
				identify candidate keys : analyse the attributes or know which one calls which
				refine tentative classes : improve and restructure initial object grouping
				define generalization : establish higher-level relationships 

--- 
steps of software RE
	1. collection info 
	2. examine the collected info 
	3. extracting the structure : identifying a routine 
	4. record functionality : processing each module of the structure 
	5. recording Data Flow: set a data flow diagram
	6. record control flow: high level control structure of the software 
	7. review Extracted Design: ensure consistency 
	8. Generate a document

---
common asembly language 
	EIP = where am i  --> the line of code currently running 
	ESP = where are my local variable 
	EAX = what is the result --> out put 

---
Basic Static
	first step followed by dynamic analysis 
	have instructions 
		fixed length (more efficeint to decode for processor and group the instructions) 
		variable length (more difficult to disassemble)
	steps used 
		identify file type and its chars
			`archs, OS, exeutalbe format` 
		extracting strings 
			`commands , passwords, protocol keywords`
		Disassemble 
			`program over view `
			`find and understand important functions`

techniques used
	string extraction 
	im port analysis 
	cross reference **use IDA** 
	control graph **use IDA**

| what is happening                           | command or method used                        |
| ------------------------------------------- | --------------------------------------------- |
| about file                                  | `file`                                        |
| to see what it had                          | `strings`                                     |
| examining the program                       | `readelf`                                     |
| to see used libraries linked                | `ldd` usually for dynamic                     |
| structures used                             | `gdb`                                         |
| to see statically lined programs            | `checksum`                                    |
| function call tree                          | draw a graph to see what calls what           |
| debuging and linking to display symbol info | `nm`                                          |
| translate binary to machine instruction     | disassembly (depends on the difficulty level) |
| to see all the disassembled                 | `odbjump`                                     |
| interactive + disassembled                  | `radare2`                                     |
dynamic analysis
	steps used 
		memory dump -> extract code after decryption 
		library/system call -> determine flow of execution , interact with OS
		debug running process  -> inspect variables , data received by the network
			it inserts target address with an int 0x03
			and interrupt causes signal SIGTRAP
			steps 
				get control and restores original instruction 
				single steps to next instruction
				re-insert break point 
		Network sniffer -> find network activities , understand protocol
techniques used 
	run DIE 
	strings 
	X-res
	find  cm 
	patch 
	test 

| what is happening                                                                                                                   | method or command  |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| general information about process                                                                                                   | `ls /proc/<pid>`   |
| file system interaction                                                                                                             | `lsof`             |
| to see active connections                                                                                                           | `netstat`          |
| to see network traffic                                                                                                              | `tcpdump` `tshark` |
| to see while it is running and have interactive one + cpu and memory regs                                                           | `gdb`              |
| system calls (boundary between user space and kernel)                                                                               | `strace` `ltrace`  |
| parent monitor another process  + when ever the child start a process the parent dir gets a notification + parent can modify memory | `ptrace`           |
|                                                                                                                                     |                    |
tools 
	IDA pro
		both for dynamic and static 
	x64dbg- 64 bit
	ollydbg- 32 bit
	ghidra - static 
	radaere2
	binaray ninja 
	DIE - recomended 
	PE-bear 

malware Analysis 
		rule 1 analysis analzyze inside sandboxed isolated virtual achine . take asnapshot before execution 
		lab setup
			should run on vm
			snapshot analysis 
			no network detection
			fakNet-NG for network simulation 
		IDC to collect 
			file hasjes 
			regestery keys created 
			files dropped on disk 
			network C2 address / domains 
			mutex names process names
		common behaviors 
			persistence 
			privilege  escalation
			cred theft 
			lateral movement 
			cs beacon communication
anti-reversing techniques 
	packing 
		encryption 
		UPX 
		DIE
		unpack first 
	anti debugging 
		tells the software to terminate if the software is on debugging app
		use olly **recommended**
	encryption
		payloads decrypted at runtime 
	obfuscation 
		junk code to kill time 
		misleading variable 
	VM detection 
		makes them to run only on the host
	control flow flatten 
		replace normal flow with a dispatch table 
