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

### Password cracking fundamentals
- Understand the Fundamentals of Password Cracking
- Mutate Wordlists
- Explain the Basic Password Cracking Methodology
- Attack Password Manager Key Files
- Attack the Passphrase of Ssh Private Keys

#### Introduction to encryption, hashes and cracking
- In this section, we'll examine the differences between encryption and hash algorithms and discuss password cracking. Then we'll review two popular password cracking tools: Hashcat and John the Ripper (JtR). Finally, we'll calculate the time it takes to crack certain hashes.

1) Answer with true or false: In symmetric encryption, one key is used for both the encryption and decryption process.
- True

2) Answer with true or false: In asymmetric encryption, we can share the private key freely over the network to another person without risking that a third party can capture our key and then decrypt messages which get sent to us.
- False

3) Answer with true or false: A cryptographic hash function is a one-way function. The resulting hash cannot be reversed by reversing the steps used to hash the plain text information.
- True

4) Use the MD5 GPU hash rate from the GPU benchmark of this section and calculate the cracking time in minutes with the following conditions. Use a charset of all lower and upper case letters of the English alphabet and use a password length of 8. Enter the answer as full minutes without seconds.

<img width="331" height="167" alt="image" src="https://github.com/user-attachments/assets/2c15a660-df79-4c4d-901b-e5f7462f50ce" />

<img width="415" height="85" alt="image" src="https://github.com/user-attachments/assets/4d4b66f5-cd48-4a0e-8a15-6f91a9c766ac" />
<img width="525" height="158" alt="image" src="https://github.com/user-attachments/assets/f3c2680a-2a0c-4250-baae-e160981a8f90" />

#### Mutating wordlists
- Password policies often require a minimum password length as well as a combination of uppercase and lowercase letters, special characters, and numbers. Most passwords in the commonly-used wordlists will not fulfill these requirements. If we wanted to use these lists against a target with strong password policies, we would need to manually prepare the wordlist by removing all passwords that do not satisfy the password policy or by manually modifying the wordlist to include appropriate passwords. We can address this by automating the process of changing (or mutating) our wordlist before sending them to this target in what is known as a rule-based attack.

<img width="427" height="266" alt="image" src="https://github.com/user-attachments/assets/37e1edc4-297c-4c2e-9861-974f8a031d21" />

<img width="542" height="443" alt="image" src="https://github.com/user-attachments/assets/06113e66-c031-4e51-bf38-f1a22f3fbba8" />

- In order to demonstrate rule functions such as capitalization, let's copy the 10 passwords from Listing 12 and save them to demo.txt in the newly-created passwordattacks directory. Then, we'll remove all number sequences (which don't fit the password policy) from demo.txt by using sed with ^1 referring to all lines starting with a "1", deleting them with d, and doing the editing in place with -i.

<img width="457" height="238" alt="image" src="https://github.com/user-attachments/assets/9f6d8938-7f09-479d-9eaf-f48073ca2471" />

- Now, we can use hashcat with our wordlist mutation, providing the rule file with -r, and --stdout, which starts Hashcat in debugging mode. In this mode, Hashcat will not attempt to crack any hashes, but merely display the mutated passwords.

<img width="448" height="385" alt="image" src="https://github.com/user-attachments/assets/fdabd4dd-4c47-4a1b-867e-86b083ab7807" />

1) You extracted the MD5 hash "056df33e47082c77148dba529212d50a" from a target system. Create a rule to add "1@3$5" to each password of the rockyou.txt wordlist and crack the hash.

<img width="458" height="203" alt="image" src="https://github.com/user-attachments/assets/2ad6bd39-b93a-4343-bbd8-880674357fe9" />

<img width="1356" height="857" alt="image" src="https://github.com/user-attachments/assets/e38e127e-9663-4929-b8f5-bd34525be956" />

2) You extracted the MD5 hash "19adc0e8921336d08502c039dc297ff8" from a target system. Create a rule which makes all letters upper case and duplicates the passwords contained in rockyou.txt and crack the hash.

<img width="400" height="65" alt="image" src="https://github.com/user-attachments/assets/a64c450b-ac98-4031-a2ac-6345f181b87d" />

<img width="1364" height="852" alt="image" src="https://github.com/user-attachments/assets/91ff2bf9-15ad-402c-94cf-e85dfd39b11e" />

#### Cracking methodology
We can describe the process of cracking a hash with the following steps:
- Extract hashes
- Format hashes
- Calculate the cracking time
- Prepare wordlist
- Attack the hash

1) Identify the hash function of the following hash: "a41e0fdfb57173f8156f58e49628968a8ba782d0cd251c6f3e2426cb36ced3b647bf83057d"

<img width="996" height="138" alt="image" src="https://github.com/user-attachments/assets/15b49eee-9c5f-4f28-b731-4ad9008820b7" />

2) Identify the hash function of the following hash "$2y$10$XrrpX8RD6IFvBwtzPuTlcOqJ8kO2px2xsh17f60GZsBKLeszsQTBC"

<img width="683" height="134" alt="image" src="https://github.com/user-attachments/assets/7aa7551d-66ea-4b91-8d97-fabc1c868ddf" />






