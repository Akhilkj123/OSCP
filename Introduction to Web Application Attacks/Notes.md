### Web Application Assessment Tools
#### Fingerprinting Web Servers with Nmap
- Since we found port 80 open on our target, we can proceed with service discovery. To get started, we'll rely on the nmap service scan (-sV) to identify the web server (-p80) banner.

<img width="654" height="144" alt="image" src="https://github.com/user-attachments/assets/0851343a-773c-4c81-990e-dac71d02aede" />

- To take our enumeration further, we can use service-specific Nmap NSE scripts, like http-enum, which performs an initial fingerprinting of the web server.

<img width="629" height="315" alt="image" src="https://github.com/user-attachments/assets/4de31672-8ab7-4d7e-9d9e-8a5c1d14ea75" />

#### Technology Stack Identification with Wappalyzer
- Along with the active information gathering we performed via Nmap, we can also passively fetch a wealth of information about the application technology stack via Wappalyzer.

<img width="670" height="885" alt="image" src="https://github.com/user-attachments/assets/55cc841c-3089-4df6-8cf4-f5f6e78f2432" />

#### Directory Brute Force with Gobuster
- Once we have discovered an application running on a web server, our next step is to map all its publicly accessible files and directories. To do this, we would need to perform multiple queries against the target to discover any hidden paths. Gobuster is a tool (written in Go language) that can help us with this sort of enumeration. It uses wordlists to discover directories and files on a server through brute forcing.

<img width="643" height="561" alt="image" src="https://github.com/user-attachments/assets/20561e9b-9dec-4d16-b726-20bcc2e2271c" />

#### Security Testing with Burp Suite
- Burp Suite is a GUI-based integrated platform for web application security testing. It provides several different tools via the same user interface. While the free Community Edition mainly contains tools used for manual testing, the commercial versions include additional features, including a formidable web application vulnerability scanner. Burp Suite has an extensive feature list and is worth investigating, but we will only explore a few basic functions in this section.

 1) We have been tasked to test the SMS Two-Factor authentication of a newly-developed web application. The SMS verification code is made by four digits. Which Burp tool is most suited to perform a brute force attack against the keyspace?
- Burp Intruder

2) Repeat the steps we covered in this Learning Unit and enumerate the targets via Nmap, Wappalyzer and Gobuster by starting Walkthrough VM 1. When performing a file/directory brute force attack with Gobuster, what is the HTTP response code related to redirection?

<img width="776" height="828" alt="image" src="https://github.com/user-attachments/assets/80af9348-d781-4167-816b-be004c294472" />

<img width="833" height="482" alt="image" src="https://github.com/user-attachments/assets/76b17052-fffc-47ad-85a4-fb14957725e3" />

3) Start up the Walkthrough VM 1 and replicate the steps we covered in this Learning Unit for using Burp Suite.  What is the default port Burp proxy is listening to?

<img width="1815" height="696" alt="image" src="https://github.com/user-attachments/assets/9a917c43-b156-4014-8bbe-a63287609ebb" />

<img width="1545" height="713" alt="image" src="https://github.com/user-attachments/assets/1c4ec80b-47a4-4ae6-b671-013d24afef66" />

<img width="391" height="198" alt="image" src="https://github.com/user-attachments/assets/07defa16-f820-4836-8532-4edae0706d33" />

<img width="1556" height="576" alt="image" src="https://github.com/user-attachments/assets/9fe14f71-91e6-4046-9d2a-21df5aace051" />

4)  We have a lot of mess on our hands, and the new DIRTBUSTER cleaning service is just what we need to help with the cleanup! You can visit their new site on the Module Exercise VM #1, but it is still under development. We wonder where they hid their admin portal.
Once found the admin portal, log-in with the provided credentials to obtain the flag.

<img width="1266" height="825" alt="image" src="https://github.com/user-attachments/assets/c5a9dbaa-7f27-4e3a-ba3d-de89f30b0dee" />

<img width="720" height="442" alt="image" src="https://github.com/user-attachments/assets/dd9d51b2-4862-4075-9986-3e4dca6ce221" />

<img width="1280" height="267" alt="image" src="https://github.com/user-attachments/assets/7a52ede9-7d87-4901-ada6-44736926c32c" />

5) The DIRTBUSTER team finally changed their default credentials, but they are not very original. We complied at http://target_vm/passwords.txt of potential passwords from the DIRTBUSTER employee contact info - I am confident the password is in there somewhere. The username is still admin, and the new login portal is available at the web server root folder on the Module Exercise VM #2.

<img width="1281" height="647" alt="image" src="https://github.com/user-attachments/assets/f586c791-0daa-41b0-a5cc-c5a7ebd3a739" />

<img width="1580" height="575" alt="image" src="https://github.com/user-attachments/assets/709fc3c3-a32c-491d-834a-a5373be0daa1" />

<img width="1714" height="701" alt="image" src="https://github.com/user-attachments/assets/ab35a82f-4685-46fa-ab85-66a624c0a5b7" />

<img width="1273" height="349" alt="image" src="https://github.com/user-attachments/assets/6bdfd695-ca50-48c1-a155-2cb45dbeba04" />

####  Debugging Page Content
- A good place to start our web application information mapping is with a URL address. File extensions, which are sometimes part of a URL, can reveal the programming language the application was written in. Some extensions, like .php, are straightforward, but others are more cryptic and vary based on the frameworks in use. For example, a Java-based web application might use .jsp, .do, or .html. File extensions on web pages are becoming less common, however, since many languages and frameworks now support the concept of routes, which allow developers to map a URI to a section of code. Applications leveraging routes use logic to determine what content is returned to the user, making URI extensions largely irrelevant.

