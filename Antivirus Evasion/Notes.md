## Antivirus Evasion
- Antivirus Software Key Components and Operations
- Bypassing Antivirus Detections
- Antivirus Evasion in Practice

### Antivirus software key components and operations
- Recognize Known vs Unknown Threats
- Understand AV Key Components
- Understand AV Detection Engines
- Antivirus (AV), is a type of application designed to prevent, detect, and remove malicious software. 

#### Known vs unknown threats
- A signature language is often defined for each AV engine and thus, a signature can represent different aspects of a piece of malware, depending on the AV engine. For example, two signatures can be developed to contrast the exact same type of malware: one to target the malware file on disk and another to detect its network communication.
- In 2014, a signature language named YARA was open-sourced to allow researchers to query the VirusTotal platform or even integrate their own malware signatures into AV products.
- Modern AV solutions, including Windows Defender, are shipped with a Machine Learning (ML) engine that is queried whenever an unknown file is discovered on a system.
- To overcome these AV limitations, Endpoint Detection and Response (EDR) solutions have evolved during recent years. EDR software is responsible for generating security-event telemetry and forwarding it to a Security Information and Event Management (SIEM) system, which collects data from every company host.

#### AV engines and components
- A modern AV is fueled by signature updates fetched from the vendor's signature database that resides on the internet.
- File Engine, Memory Engine, Network Engine, Disassembler, Emulator/Sandbox, Browser Plugin, Machine Learning Engine. Each of the engines above work simultaneously with the signature database to rank specific events as either benign, malicious, or unknown.
- The file engine is responsible for both scheduled and real-time file scans. When the engine performs a scheduled scan, it simply parses the entire file system and sends each file's metadata or data to the signature engine. To detect such operations, the real-time scanners need to identify events at the kernel level via a specially crafted mini-filter driver.  
- The memory engine inspects each process's memory space at runtime for well-known binary signatures or suspicious API calls that might result in memory injection attacks, as we'll find shortly.
- The network engine inspects the incoming and outgoing network traffic on the local network interface. Once a signature is matched, a network engine might attempt to block the malware from communicating with its Command and Control (C2) server.
- Malware often employs encryption and decryption through custom routines to conceal its true nature. AVs counterattack this strategy by disassembling the malware packers or ciphers and loading the malware into a sandbox, or emulator.
- A sandbox is a special isolated environment in the AV software where malware can be safely loaded and executed without causing potential havoc to the system. 
- Heuristic-Based Detection is a detection method that relies on various rules and algorithms to determine if an action is considered malicious.
-  Behavior-Based Detection dynamically analyzes the behavior of a binary file. This is often achieved by executing the file in question in an emulated environment, such as a small virtual machine, or sandbox,and searching for behaviors or actions that are considered malicious.
- Machine-Learning Detection aims to up the game by introducing ML algorithms to detect unknown threats by collecting and analyzing additional metadata. For instance, Microsoft Windows Defender has two ML components: the client ML engine, which is responsible for creating ML models and heuristics, and the cloud ML engine, which is capable of analyzing the submitted sample against a metadata-based model comprised of all the submitted samples.   

#### Detection methods
- In this section, we are going to explore the following AV detection methodologies and explain how they work together.
- Signature-based Detection, Heuristic-based Detection, Behavioral Detection, Machine Learning Detection

1) Which AV engine is responsible for translating machine code into assembly?
- Disassembler engine

2) Which AV detection method makes use of an engine that runs the executable file from inside an emulated sandbox?
- Behavior-Based Detection

3) Start up VM #1 and connect via RDP to the Windows 11 machine with the provided credentials. On the user's desktop you will find a PE file named malware.exe. In order to get the flag, upload the malware sample to http://www.virustotal.com and once the analysis has completed check the metadata present in the BEHAVIOR tab.
- 
