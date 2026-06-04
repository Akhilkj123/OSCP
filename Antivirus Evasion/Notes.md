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
 
<img width="906" height="594" alt="image" src="https://github.com/user-attachments/assets/159e4b0f-c33e-4936-81ee-2a3e0191a90e" />

<img width="907" height="578" alt="image" src="https://github.com/user-attachments/assets/883c0522-12cc-4b5b-87f8-988e66a724c9" />

###  Bypassing antivirus detections
- Understand On-disk Evasion Techniques
- Understand In-memory Evasion Techniques

#### On-disk evasion
- Instead of hiding malware only while it is running in memory, attackers may disguise the malicious files stored on a system's hard drive. These techniques are designed to make malware more difficult for antivirus (AV) software to identify before execution.
- **Packers** - Packers compress or transform an executable file into a new executable with a different binary structure. When the packed program runs, it automatically unpacks itself and executes the original code. Because the packed file has a different structure and hash value, older signature-based antivirus products may fail to recognize it.
- **Code Obfuscation** - Obfuscators modify a program's code while preserving its functionality. Techniques include replacing instructions with equivalent alternatives, inserting unnecessary instructions (dead code), splitting functions, or rearranging program logic. These modifications make reverse engineering more difficult and can reduce the effectiveness of signature-based malware detection.
- **Crypters** - Crypters encrypt or otherwise transform executable code and add a small decryption component known as a stub. When the program is executed, the stub decrypts the original code directly in memory before running it. Since only the encrypted version exists on disk, antivirus software may have greater difficulty identifying the malware through static file analysis.
- **Software Protectors** - Software protectors combine multiple defensive and obfuscation techniques to make analysis and detection more difficult. They often include encryption, packing, code virtualization, anti-debugging, anti-tampering, and anti-reverse-engineering features.
- **Anti-Debugging** - The malware checks whether it is being examined by a debugger. If debugging tools are detected, the malware may terminate, hide its behavior, alter its execution, or provide misleading information to hinder analysis.
- **Virtual Machine (VM) Detection** – The malware attempts to determine whether it is running inside a virtual machine or sandbox environment commonly used by security analysts. If such an environment is detected, the malware may avoid executing its malicious functions to prevent analysis and detection.
- **Layered Evasion Techniques** - Modern malware often combines packing, obfuscation, encryption, anti-debugging, anti-reversing, and VM detection techniques.

#### In-memory evasion
- Instead of saving malware as a file on the hard drive, the attacker places and runs the malicious code directly in RAM. Since many security tools focus heavily on scanning files stored on disk, this can make detection more difficult. The code usually disappears when the system is rebooted unless another persistence method is used.
- **Remote Process Memory Injection** - The attacker inserts malicious code into the memory space of another legitimate process, such as a trusted application. The malicious code then runs under the identity of that legitimate process. This can help the attacker blend in with normal system activity and avoid some security checks.
- **Reflective DLL Injection** - Normally, a DLL must be loaded from a file stored on disk. In this technique, the DLL is loaded directly from memory using custom code rather than Windows' normal DLL-loading mechanism. As a result, no DLL file needs to be written to disk.
- **Process Hollowing** - A legitimate program is started in a suspended state before it begins executing. The original program code is removed from memory and replaced with malicious code. When the process is resumed, it appears to be the legitimate program, but it is actually running the attacker's code.
- **Inline Hooking** - The attacker modifies a function so that execution is temporarily redirected to malicious code. After the malicious code runs, execution returns to the original function as if nothing unusual happened. This allows the attacker to intercept, monitor, or alter program behavior.
- **Rootkit** - A rootkit is a stealth-focused type of malware designed to hide itself and maintain long-term access to a system. It often modifies operating system components or uses hooking techniques to conceal files, processes, network connections, or other malicious activity. Because of its deep integration with the system, a rootkit can be very difficult to detect and remove.

1) Which on-disk evasion technique makes use of code made by spurious instructions and that is not part of the main execution?
- Packers

2) When performing Remote Process Injection, which API is responsible for copying the shellcode into the target thread?
- WriteProcessMemory

3) Between packers and crypters, which one provides the highest level of stealth?
- Crypters

### AV evasion in practice
- Understand Antivirus Evasion Testing Best Practices
- Manually Evade AV Solutions
- Leverage Automated Tools for AV Evasion

#### Testing for AV evasion
 - SecOps is the teamwork between an organization's IT staff and security team to continuously protect computers and networks from cyber threats.
- For penetration testers, it's important to understand how antivirus (AV) products work. If you upload your malware sample to VirusTotal, the sample is shared with many antivirus companies. They can analyze it    and quickly create signatures to detect it, making your tool ineffective.
- A safer alternative is Kleenscan, which scans files with multiple AV engines but claims not to share the uploaded samples with antivirus vendors.
- However, the best approach is to test your malware in a virtual machine (VM) that closely matches the target company's environment, especially if you know which antivirus product they use. This gives more        accurate results without exposing your tools to AV vendors.
- Regardless of the tested AV product, we should always make sure to disable sample submission so that we don't incur the same drawback as VirusTotal. For instance, Windows Defender's Automatic Sample Submission can be disabled by navigating to Windows Security > Virus & threat protection > Manage Settings and deselecting the relative option as illustrated in the image below.

<img width="935" height="462" alt="image" src="https://github.com/user-attachments/assets/6be4f8f0-e5e9-4a07-b4f3-61c9627fec62" />

#### Evading AV with thread injection
-  Once we connect via RDP with the provided credentials, we'll notice that Avira is already installed and can be launched from the Desktop shortcut. Once started, we can navigate to the Security panel from the left menu and click on Protection Options:

<img width="851" height="570" alt="image" src="https://github.com/user-attachments/assets/c53e0b26-2a61-4e69-8681-89db37d19ec4" />

<img width="1141" height="711" alt="image" src="https://github.com/user-attachments/assets/9f94313b-dde4-4ac2-b5e9-1e14d0fac83b" />

- Use Shellter to inject a Meterpreter reverse shell payload in the Spotify executable, then transfer the binary to your Window 11 client VM #1 and ensure that it is not being detected by the antivirus. After, set up a Meterpreter listener, run the backdoored Spotify installer, and verify that you have obtained an interactive shell. As an additional exercise, attempt to find different executables and inject malicious code into them using Shellter. Which Shellter option is responsible for restoring the execution flow of the backdoored binary and therefore avoids any unwanted suspicion?


