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
