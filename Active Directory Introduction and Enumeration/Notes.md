## Active Directory Introduction and Enumeration
- Active Directory (AD) is a Microsoft service that helps organizations manage their network resources. It acts as both a service and a management layer, storing important information about the environment. This information includes users, groups, and computers, which are all referred to as objects. Each object has permissions assigned to it, and these permissions determine what actions the object can perform within the domain. Because AD contains such a large amount of important information, it is a powerful management tool, but it can also create a large attack surface if not configured securely.
- To make administration easier, system administrators organize objects into Organizational Units (OUs). OUs can be compared to folders in a file system because they act as containers that store and organize objects within the domain. By placing users, computers, and other objects into OUs, administrators can manage resources more efficiently and apply policies to specific groups of objects.
- Active Directory contains different types of objects. Computer objects represent actual servers and workstations that have joined the domain, while user objects represent accounts that people use to log in to domain-joined systems. Every object contains attributes, which are pieces of information that describe the object. For example, a user object may have attributes such as first name, last name, username, phone number, and email address. These attributes help administrators identify and manage objects within the directory
- A Domain Controller (DC) is one of the most important components in Active Directory. It serves as the central hub of the domain and stores all OUs, objects, groups, and their attributes. When a user attempts to log in, the request is sent to a Domain Controller. The DC verifies the user's credentials and determines whether the user is allowed to access the domain. Since Domain Controllers contain critical information and control authentication, they are a primary focus during Active Directory enumeration.
- Active Directory allows objects to be assigned to groups so they can be managed as a single unit. Instead of assigning permissions to each user individually, administrators can assign permissions to a group and automatically grant those permissions to all members of that group. For example, a group might be given access to a shared folder, file server, or administrative functions on certain systems. Managing permissions through groups makes administration more efficient and scalable.
- Attackers often focus on high-privileged groups because compromising a single member can provide access to important resources. One of the most important groups is the Domain Admins group. Members of this group have extensive administrative control over the domain. If an attacker compromises a Domain Admin account, they can effectively gain complete control over the domain and its resources. As a result, Domain Admin accounts are considered extremely valuable targets.
- Active Directory enumeration is the process of gathering information about the AD environment. The purpose of enumeration is to understand the structure of the domain, identify important systems and accounts, and discover relationships between objects. Effective enumeration increases the likelihood of success during later phases of a security assessment or attack because it provides a clear picture of the environment.
- Before relying on automated tools, it is important to understand the fundamentals of manual Active Directory enumeration. Manual enumeration helps build a strong understanding of how AD works and what information is being collected. Once these foundational techniques are understood, automated tools can be used to perform enumeration on a much larger scale. These tools often use LDAP and other protocols to quickly gather and analyze information throughout the domain.
- Many Active Directory enumeration techniques rely on the Lightweight Directory Access Protocol (LDAP). LDAP is a protocol used to query and retrieve information from Active Directory. Through LDAP, administrators and security professionals can obtain information about users, groups, computers, Domain Controllers, and other objects stored in the directory. Because LDAP provides access to such valuable information, it is one of the most important protocols used during Active Directory enumeration.

### Active Directory - manual enumeration
- Enumerate Active Directory using legacy Windows applications
- Use PowerShell and .NET to perform additional AD enumeration

####  Active Directory - enumeration using legacy Windows tools

<img width="623" height="391" alt="image" src="https://github.com/user-attachments/assets/46b82427-b5ae-4396-99e0-2fc484a2e75c" />

<img width="976" height="398" alt="image" src="https://github.com/user-attachments/assets/c6d116e8-9f94-4aaf-b288-6557d8dff455" />

<img width="695" height="464" alt="image" src="https://github.com/user-attachments/assets/a05367c0-a6c5-49a4-820b-f757bd9ee6c4" />

<img width="710" height="511" alt="image" src="https://github.com/user-attachments/assets/bdab19e6-b9ef-4a8f-b204-381f347bcdf5" />

<img width="666" height="285" alt="image" src="https://github.com/user-attachments/assets/0b14490c-4ff3-4169-97e5-9c0a9c1803ae" />

1) Which type of server acts as the core and hub of a domain hosted in Active Directory?
- Domin Controller(DC)

2) Start VM Group 1 and log in to CLIENT75 as stephanie. Use net.exe to enumerate the corp.com domain. Which user is a member of the Management Department group?

<img width="989" height="507" alt="image" src="https://github.com/user-attachments/assets/3faeda9c-91bc-43a2-82eb-7fbc45cbe37e" />
 - jen

3) Start VM Group 2 and log in to CLIENT75 as stephanie. Use net.exe to enumerate the users and groups in the modified corp.com domain to obtain the flag.

<img width="698" height="532" alt="image" src="https://github.com/user-attachments/assets/2b12fef8-2c54-4479-b355-5a028fea60c7" />

#### Enumerating Active Directory using PowerShell and .NET classes

