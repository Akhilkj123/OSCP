##  Password Attacks
### Attacking network services logins
- Attack SSH and RDP logins
- Attack HTTP POST login forms
#### SSH
- In this section, we'll execute dictionary attacks against the common SSH and RDP services using the open-source THC Hydra tool, which can execute a broad variety of password attacks against a variety of network services and protocols. We'll also use the popular rockyou.txt wordlist, which contains over 14 million passwords. Both of these are pre-installed on our Kali machine.

<img width="762" height="203" alt="image" src="https://github.com/user-attachments/assets/64cc473c-e540-493b-b074-004e65578c36" />

<img width="1201" height="81" alt="image" src="https://github.com/user-attachments/assets/9c2a4e88-a359-44dd-86a9-3af74aedeb60" />

<img width="1699" height="202" alt="image" src="https://github.com/user-attachments/assets/570ff089-4b6e-4556-966c-59e61b28bf35" />

1) Follow the steps outlined in this section to leverage a dictionary attack to get access to SSH (port 2222) on Password Attacks - SSH - VM #1. Find the flag in the george user's home directory.

<img width="764" height="489" alt="image" src="https://github.com/user-attachments/assets/17e4b145-1aba-4752-8e72-82d136bb1590" />

#### RDP
- In this next example, we will attempt to use a single password against a variety of usernames in a technique known as password spraying.

1) Follow the steps outlined in this section to leverage a dictionary attack to gain access to RDP on Password Attacks - RDP - VM #1. Find the flag on either one of the user's desktops. To reduce the time it takes to perform the password spraying, you can create a list with the two usernames: justin and daniel.

<img width="193" height="82" alt="image" src="https://github.com/user-attachments/assets/6800ebc9-6c5d-4332-afd1-4fe587adf969" />

<img width="1683" height="222" alt="image" src="https://github.com/user-attachments/assets/30123886-0cd1-4d63-a04a-b1bd6fd9c827" />

<img width="1770" height="529" alt="image" src="https://github.com/user-attachments/assets/df178e79-ba6f-431e-96e2-8f6966e13825" />

2) Enumerate Password Attacks - RDP - VM #1 and find another network service. Use the knowledge from this section to get access as the itadmin user and find the flag.

<img width="777" height="747" alt="image" src="https://github.com/user-attachments/assets/1a49dc98-ea0f-4248-80f6-e2e2e1a5f6ff" />

<img width="1679" height="180" alt="image" src="https://github.com/user-attachments/assets/dce8a427-aa5b-4654-805d-85d569c75179" />

<img width="1842" height="454" alt="image" src="https://github.com/user-attachments/assets/6620bf94-63fc-4a25-8ff8-12b11c451f62" />

<img width="312" height="58" alt="image" src="https://github.com/user-attachments/assets/9dc136a8-81f7-4581-8953-d3fd1f6c1e67" />

#### HTTP POST login form
- In most internal and external assessments, we will face a web service. Depending on the service, we may not be able to interact with it until we log into it. If this is our only vector and we're unable to use default credentials to log in, we should consider using a dictionary attack to gain access. Most web services include a default user account, such as admin. Using this known username for our dictionary attack will dramatically increase our chances of success and reduce the expected duration of our attack. 

<img width="1280" height="705" alt="image" src="https://github.com/user-attachments/assets/d0f01d00-5706-4700-88c3-3f08598622c2" />

- Now we can assemble the pieces to start our Hydra attack. As before, we'll specify -l for the user and -P for the wordlist, set the target IP without any protocol, and provide a new http-post-form argument, which accepts three colon-delimited fields. 
1) Follow the steps from this section to gain access to TinyFileManager on VM #1 (BRUTE). Once logged in, find the flag.

<img width="1674" height="217" alt="image" src="https://github.com/user-attachments/assets/fcf2246e-581a-41c2-ab77-cd565c1e2394" />

<img width="1279" height="469" alt="image" src="https://github.com/user-attachments/assets/3ff17f78-e499-4769-a055-56ab9a031064" />

2) The web page on VM #2 is password protected. Use Hydra to perform a password attack and get access as user admin. Once you have identified the correct password, enter it as the answer to this exercise.

<img width="1671" height="201" alt="image" src="https://github.com/user-attachments/assets/de9f3ce0-c3d3-4f77-88ec-b1cefec9fed9" />
