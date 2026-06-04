###  Phishing Basics
- Phishing 101
- Payloads, Misdirection and Speedbumps
- Hands-On Credential Phishing
- Phishing attacks are categorized into two main types: broad phishing (mass attacks) and spear phishing (targeted attacks). Spear phishing targets specific individuals with personalized attacks, requiring detailed research.
- Attackers now leverage Generative AI (Gen AI) to improve social engineering tactics. By using AI-augmented technologies such as Large Language Models (LLMs), which process large amounts of public data to identify potential phishing targets
- Attackers have also begun leveraging Generative AI audio models to clone voices and generative video models to create deepfake videos that convincingly replicate an individual’s facial expressions, movements, and voice patterns.


### Phishing 101
- Understanding Email Phishing
- Exploring Smishing, Vishing, and Chatting
- Enhancing Phishing through Social Engineering
- Leveraging LLMs, Generative AI, and Deepfakes

####  Email phishing
- The email text is often crafted with a particular goal, such as convincing the target to perform an action that will execute code. In this case, the attacker will likely include a malicious attachment in the email and persuade the target to open it, which triggers the execution of a specific payload. Malicious attachments can take different forms, including Office documents, PDFs, 7zip/zip archives, shortcut files, and calendar invites.

####  Smishing, vishing, and chatting
- Attackers can also leverage smishing (a portmanteau of "SMS" and "phishing") to phish a target through SMS or other mobile messaging platforms.
- Another category of phishing is voice phishing, sometimes called vishing This is a combination of ‘voice’ and ‘phishing’, in which an attacker calls a target on the phone, and speaks to them directly.
- In an adjacent style of social engineering attack known as SIM swapping, attackers call a mobile network provider and claim to be the owner of a specific mobile phone account. They then convince the network provider to transfer the phone number from the target's SIM card to a SIM card they control. This gives them control over the target's phone number, until the target is able to recover their access.
- It's also worth mentioning whaling, a form of spear phishing that focuses on high-profile individuals. These targeted attacks require more care and attention than a typical phishing campaign. These pretexts are often highly customized and require significant research or inside knowledge of the target.
- 
####  Enhancing phishing through social engineering
- Urgency is a common social engineering technique used by phishers, manipulating targets into acting quickly without questioning the safety of the requested action or critically reflecting on what they're doing. Introducing a sense of urgency works best in organizations which have unhealthy work cultures. If a target often receives urgent requests and is expected to deliver on them without any critical thought, they are much more likely to fall for these kinds of manipulations.
- Another strategy, fear, can cause a target to momentarily suspend their judgment, increasing the likelihood of compliance. Authority, a similar strategy to fear, can amplify the urgency of our request. This often involves taking on the role of a superior, or even the company's CEO. These strategies must be balanced as we consider elements of trust and the benefits of creating a good rapport.
- Finally, we'll often leverage a positive incentive like a reward, in a process known as baiting in which we offer something tangible to lure a target into performing an action. The promise might include a gift card, cash, or another incentive or intangible benefits like gaining favor with a superior. Offering something tangible in exchange for participation in something like a survey is not an uncommon approach for companies in general. This kind of approach might blend into the background noise for some targets.
- The social elements of a phish directly correlate to the success rate of the campaign. Exploiting a trust relationship, and possibly adding other kinds of manipulations along the way, can help a target suspend their judgment, which can improve the effectiveness of a phishing campaign.

#### LLMs, generative AI and deepfakes
- An LLM could assist with Retrieval Augmented Generation (RAG) to process a large amount of publicly-available information about a target, and distill this into material we can turn into a solid pretext. RAG may not even be necessary against high-profile targets, as the model may already have useful information. By creatively leveraging Gen AI, attackers can craft more personalized and convincing attacks.
- Technologies such as voice cloning have become much more available to the general public in recent years. These technologies allow attackers to create a voice model for an individual, based on a relatively small amount of recorded audio. They can then make this model say whatever they want.
- Deepfake videos are also being used in phishing attacks. In 2024, Architecture firm Arup fell prey to a deepfake video scam. During a video call, deepfake clones of the CFO and other staff appeared and acted as actual employees. The deepfaked CFO signed off on a transfer of $25 million, which was then transferred to the attackers.

1) What type of phishing attack is performed when the target is a high profile individual?
- Whaling

2) What is the term for phishing over SMS?
- Smishing

3) What is the name of the technique in which the attacker will reach out to a mobile network provided and claim to be the owner of a specific mobile phone account?
- SIM swapping

### Payloads, misdirection, and speedbumps
- Understanding the Role of Inbound email Filters
- Identifying Risks of Malicious Office Macros
- Assess Threats from Malicious Files
- Recognize Malicious Links
- Differentiate Credential Phishing and Multi-Factor Authentication (MFA)

#### Understanding the role of inbound email filters
 - Before discussing payloads, it's important to understand the defenses organizations use against phishing. One of the main defenses is email filtering, which checks incoming emails for signs of malicious activity and blocks suspicious messages.
- Email filters often evaluate the reputation of the sender's domain. They may check whether the domain has been reported before, how old it is, and other trust-related factors.
- Attachments are also closely inspected. File types such as .exe and .scr are commonly treated as dangerous. Other files like Office documents, PDFs, ZIP archives, scripts, and links to downloadable files may also be flagged as suspicious.
- In addition, many organizations label emails from outside the company with warnings such as [EXTERNAL] in the subject line. This helps employees quickly recognize that the email came from an external source, even if it appears to be from a coworker.

####  Identifying risks of malicious Office macros
- Phishers often use Microsoft Office documents because they are commonly used in businesses and can contain features that run code. Attackers may hide malicious code inside Word, Excel, or other Office files and send them through phishing emails.
- Many Office applications support Visual Basic for Applications (VBA), a scripting language that allows documents to use macros. Macros are designed to automate tasks and make documents more interactive.
- Attackers have abused macros for many years to run malicious code. One early example was the Melissa Macro Virus in 1999, which spread through a malicious Word document.
- To reduce these risks, Microsoft introduced several security measures: Macros are disabled by default, so users must manually enable them, Mark of the Web (MotW) is added to files downloaded from the internet, This mark tells Windows that the file came from an external source
- These protections make phishing attacks using Office macros much harder because files received through email are usually marked as coming from the internet.
- Organizations can also strengthen security using Group Policies in Active Directory. Administrators can prevent users from disabling Protected View or running macros altogether. Users cannot override these settings.
- Even though Office macro attacks are less effective today, they still remain a threat. Some organizations use older versions of Office that lack newer security features, while others may not fully enforce security policies.

#### Assess threats from malicious files
- Office macros are not the only way attackers can run malicious code on a victim's computer. While .exe files can execute programs directly, email filters often block them, and most users know they can be dangerous. Because of this, attackers also use other file types such as SCR, HTA, and JScript files.
- Since Microsoft Office documents are commonly used in organizations, attackers often look for weaknesses in Office-related components instead of relying on macros.
- For example:
1) CVE-2017-11882 was a vulnerability in Microsoft's Equation Editor. By opening a specially crafted Office document, an attacker could execute code on the victim's computer.
2) CVE-2023-21716 is a vulnerability in Microsoft Word's RTF file parser that can also be exploited through malicious documents.
- These vulnerabilities allow attackers to run code without requiring macros, but their usefulness decreases as organizations install security updates and patches.
- Microsoft Office is not the only target. Other software, such as PDF readers, can also contain vulnerabilities. For example, CVE-2023-21608 is a flaw in Adobe Acrobat Reader that could allow attackers to execute code through a malicious PDF file.
- Different industries often rely on different software, such as Office applications, PDF readers, email clients, or web browsers. Knowing what software a target uses helps attackers choose the most effective attack method.
- Some advanced attackers search for 0-day vulnerabilities—security flaws that are unknown to the software vendor and have no available patch. These vulnerabilities are often used in spear-phishing attacks because victims have no protection against them.
- However, finding 0-days is expensive and time-consuming, so they are usually used by well-funded attackers.
- Another technique used by advanced attackers is reverse-engineering security patches. By studying recently released patches, they try to discover the underlying vulnerability and exploit systems that have not yet been updated.

#### Recognize malicious links
- Instead of sending malicious files, attackers may try to trick users into clicking malicious links. This helps them bypass many email security protections that focus on attachments.
- A common method is to create a fake website that looks like a real service, such as: Gmail, Zoom, Microsoft login page
- If the phishing email is convincing, users may enter their real usernames and passwords on the fake site. The attacker can then steal those credentials.
- Password managers can help protect against this because they usually only autofill credentials on the correct website. For example, credentials saved for microsoft.com will not be filled into a fake domain that only looks similar.
- However, password managers are not perfect. Over the years, researchers have found vulnerabilities that allowed attackers to access stored passwords or other sensitive information. Despite these flaws, password managers still provide strong protection against many phishing attacks.
- More advanced phishing attacks may not try to steal passwords directly. Instead, the attacker may send a link to a website that exploits a vulnerability in the user's web browser. If successful, this could allow malicious code to run on the victim's device. However, this type of attack is difficult because it usually requires a browser vulnerability and a specific target environment.
- Another attack method involves Cross-Site Request Forgery (CSRF). In a CSRF attack, a malicious webpage tricks a logged-in user's browser into performing actions on another website without the user's knowledge. For example, it could create an account, change settings, or perform other actions using the victim's existing login session.
- To increase the chance that a victim clicks a link, attackers often use social engineering. They make the link appear important, urgent, or relevant to the victim.
- Attackers may also hide suspicious-looking URLs by: Using URL-shortening services, Creating website addresses that closely resemble legitimate domains
- For example, some fake domains use characters from other alphabets that look nearly identical to normal letters. To a user, the fake website may appear genuine even though it leads somewhere completely different.
- Modern websites usually use HTTPS, so attackers often ensure their fake websites also use valid HTTPS certificates. This helps the site appear more trustworthy and avoids browser security warnings.
- In some cases, clicking a malicious link can cause a computer to automatically attempt authentication. On older Windows systems, this could expose information such as NetNTLMv2 hashes, which attackers may try to capture and abuse. Similar behavior can sometimes be triggered through links to network resources or embedded images.

<img width="648" height="283" alt="image" src="https://github.com/user-attachments/assets/24f2391c-2474-4549-9802-e0b05b966118" />

#### Differentiate credential phishing and multi-factor authentication (MFA)
- Once we have credentials, we may hit another roadblock in the form of Multi-Factor Authentication (MFA). This is another security mechanism which many organizations implement to slow down an attack, even in the event of credential compromise.
- There are several ways we might want to handle this. One common technique is prompt bombing, which targets MFA applications that use push-based authentication prompts. In this strategy, we bombard the target with login attempts, which trigger prompts on their phone asking them to approve the login. This can create a phenomenon known as MFA fatigue, where users assume the authorization requests are legitimate (albeit glitched) and accept one to stop the alerts.
- Another approach to defeat MFA is to add the MFA prompt directly into the credential-stealing website's login flow. This allows us to capture not only the victim's username and password but also their MFA token. However, once we've obtained the token, we must relay it to the legitimate application immediately since MFA tokens typically have a very short lifespan. This means timing is critical. While this approach only gives us single-use access to the target application, it can still be highly effective when used surgically and with detailed planning.
- An alternative method involves a browser-in-the-middle attack, where an attacker proxies a real session to capture authentication details. To the target, it appears they are interacting with the legitimate website, which they are. However, the session they create upon logging in (along with their MFA token) is actually under the attacker's control. Tools like cuddlephish help automate this kind of attack. Using such a tool requires access to a public IP address and can not be easily setup locally. If you're doing an assumed breach type pentest and are attempting to get access to internal web applications then such limitations become important.
- Another technical approach to bypass MFA is brute-forcing. Since an MFA token is often six numbers, we could, at least in theory, attempt to brute-force it. This will obviously take time and bandwidth, assuming the MFA server even allows unlimited attempts and an (extremely long) response window.
- We could also assume a less-technical approach and use social engineering. For example, we could contact a target directly, acting as a trusted figure like the company helpdesk, or a member of the IT department, and ask the target to provide the MFA token. This would generally require a very solid pretext.
- Finally, if an MFA token is delivered by SMS, some criminal actors might also engage in SIM swapping to gain access to a target's phone number, and receive the MFA token themselves. This isn't something we can generally do in legitimate pentesting, due to the legal implications of the attack. However, it's important to understand this tactic as it is leveraged against SMS-based MFA systems.

1) What scripting language is natively supported in Microsoft Office?
- Visual Basic for Applications

2) What is the name of the phenomenon in which a user will respond to a flood of MFA requests?
- MFA fatigue

#### Hands-on credential phishing
- Creating a Zoom Credential Phishing Pretext
- Cloning a Legitimate Website
- Cleaning Up the Clone
- Injecting Malicious Elements in the Clone
- Crafting the Phishing email

Browse to the Webmail application located at the http://192.168.X.77/mail/ URL (adjust the IP according to the one assigned to VM #1) with the helpdesk@mail.corp.com account and browse to the Sent folder. How many recipients was the email sent to? Additionally, after determining the number of recipients, use an LLM like ChatGPT to craft a convincing reply based on the Zoom license scenario covered in this Learning Unit.
- 5
<img width="1146" height="723" alt="image" src="https://github.com/user-attachments/assets/366cb2f6-d79c-4e16-8d92-feeda92f1314" />
<img width="1143" height="565" alt="image" src="https://github.com/user-attachments/assets/7c2ca3cc-666e-4b5d-b739-d854a5a8348d" />
<img width="574" height="286" alt="image" src="https://github.com/user-attachments/assets/07449911-8ed4-4640-bb42-a19af708d03f" />

#### Cloning a legitimate website

<img width="587" height="801" alt="image" src="https://github.com/user-attachments/assets/ea42c4ef-2dc0-4cef-b049-662677ce47db" />

Using your Kali VM try to clone the Zoom login page. What wget flag do we need to supply to save everything as a flat structure rather than having various subdirectories?

<img width="860" height="469" alt="image" src="https://github.com/user-attachments/assets/1542b492-91bf-4e5c-935e-1ebdeef26e7c" />

<img width="1150" height="716" alt="image" src="https://github.com/user-attachments/assets/98d93e9a-519a-481b-a4df-bd62bc50f905" />

#### Cleaning up the clone

- Next, we'll create a Python script that performs all of our modifications in one pass. This script will: Remove the broken OneTrust cookie consent banner, Add an onclick handler to the Next button that, triggers our custom password step, Add Enter key support on the email field, Inject a password overlay that mimics Zoom's second login step, Add a working cookie banner that matches the original's appearance

<img width="572" height="336" alt="image" src="https://github.com/user-attachments/assets/2f85ee57-3914-4cbb-a405-4d85ff5c73ba" />

####  Capturing credentials
- Let's create a simple Python credential server. This script will listen for POST requests, extract the email and password from the form data, print them to the terminal, and redirect the victim to the real Zoom login page so they assume the login simply failed.

<img width="864" height="414" alt="image" src="https://github.com/user-attachments/assets/72a26d92-f569-4449-9920-a24f1ee5ecd6" />

<img width="934" height="677" alt="image" src="https://github.com/user-attachments/assets/24e08b75-2c3e-417f-b696-3f507115ef33" />

<img width="500" height="188" alt="image" src="https://github.com/user-attachments/assets/16f334b9-b20e-4207-8ba0-46144375d035" />



- The page now looks identical to the original. The cookie banner appears at the bottom and can be dismissed by clicking Cookies Settings. When we enter an email address and click Next, the page transitions to the password entry step while keeping the header and sidebar image visible.

<img width="930" height="790" alt="image" src="https://github.com/user-attachments/assets/e66dcb25-3d75-4f06-b1a4-127e6578ef81" />

