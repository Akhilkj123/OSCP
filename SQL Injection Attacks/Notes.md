## SQL Injection Attacks
- SQL Theory and Database Types
- Manual SQL Exploitation
- SQL Attack Automation
- SQL injection (SQLi) is a major web application vulnerability class prevalent in many web applications. It is currently ranked third among OWASP's Top 10 Application Security Risks. It is listed as: A03:2021-Injection

### SQL theory and databases
- Refresh SQL Theory Fundamentals
- Learn About Different DB Types
- Understand the Different SQL Syntax

#### SQL theory refresher
- Structured Query Language (SQL) has been developed specifically to manage and interact with data stored inside relational databases. SQL can be employed to query, insert, modify, or even delete data, and, in some cases, execute operating system commands. Since the SQL instance offers so many administrative privileges, we'll soon observe how arbitrary SQL queries can pose a significant security risk.
- We can use the SELECT statement to instruct the database that we want to retrieve all (*) the records from a specific location defined via the FROM keyword and followed by the target, in this case, the users table. Finally, we'll direct the database to filter only for records belonging to the user leon.
- When the user types leon, the SQL server searches for the username "leon" and returns the result. To search the database, the SQL server runs the query SELECT * FROM users WHERE user_name= leon. If, instead, the user enters "leon '+!@#$", the SQL server will run the query SELECT * FROM users WHERE user_name= leon'+!@#$. Nothing in our code block checks for these special characters, and it's this lack of filtering that causes the vulnerability.

#### DB types and characteristics
- When testing a web application, we sometimes lack prior knowledge of the underlying database system, so we should be prepared to interact with different SQL database variants.

<img width="660" height="707" alt="image" src="https://github.com/user-attachments/assets/f6545c41-e3bb-4b56-9a46-5b69a0946355" />

<img width="866" height="256" alt="image" src="https://github.com/user-attachments/assets/86cff28d-3e77-4a28-a93b-bbfb57616507" />

1) From your Kali Linux VM, connect to the remote MySQL instance on VM 1 and replicate the steps to enumerate the MySQL database. Then explore all values assigned to the user offsec. Which plugin value is used as a password authentication scheme?
- caching_sha2_password

2) From your Kali Linux VM, connect to the remote MSSQL instance on VM 2 and replicate the steps to enumerate the MSSQL database. Then explore the records of the sysusers table inside the master database. What is the value of the first user listed?

<img width="1698" height="652" alt="image" src="https://github.com/user-attachments/assets/f5de3c15-6830-494e-b68e-ffef0d3e47ae" />

3) From your Kali Linux VM, connect to the remote MySQL instance on VM 3 and explore the users table present in one of the databases to get the flag

<img width="1433" height="657" alt="image" src="https://github.com/user-attachments/assets/010f09e1-b8be-42af-8861-e45c090ebe13" />

### Manual SQL exploitation
- Manually Identify SQL Injection Vulnerabilities
- Understand UNION SQLi Payloads
- Learn about Error SQLi Payloads
- Understand Blind SQLi Payloads

#### Identifying SQLi via error-based payloads
- To experiment with this attack against a real application, we can browse to http://192.168.50.16 from our local Kali machine, enter "offsec" and "jam" in the respective username and password fields, and click Submit.

<img width="1142" height="676" alt="image" src="https://github.com/user-attachments/assets/d4938948-e537-417d-9835-35c8fe0f13c5" />

- Because the offsec user's credentials are invalid, we receive an Invalid Password error message. As a next step, let's try to insert any special character inside the Username field to test for any interaction with the underlying SQL server. We'll append a single quote to the username and click Submit again.

<img width="1152" height="664" alt="image" src="https://github.com/user-attachments/assets/b3799dc7-ff2d-4522-945c-705c996ef2ba" />

<img width="1158" height="554" alt="image" src="https://github.com/user-attachments/assets/be230ac9-170f-4daa-a2c2-f8b0781b5a5b" />

<img width="1144" height="568" alt="image" src="https://github.com/user-attachments/assets/0d838e21-e9d3-4959-a4ae-edc9c88f2f10" />

- When we give the query " ' or 1=1 in (SELECT password FROM users) -- //"

<img width="1126" height="721" alt="image" src="https://github.com/user-attachments/assets/8cd056b7-2731-499a-a88c-95d603106469" />

- When we give the query " ' or 1=1 in (SELECT password FROM users WHERE username = 'admin') -- //"

<img width="1091" height="665" alt="image" src="https://github.com/user-attachments/assets/4f9d7a8c-d617-41b2-bb8d-ce615c0ded26" />

1) Boot up VM 1 and replicate the SQLi authentication bypass payload we have explored in this Learning Unit. In this section, which PHP variable is used to store user's input?

<img width="912" height="701" alt="image" src="https://github.com/user-attachments/assets/75056367-01a2-418f-a4da-ada9f823e67e" />

#### UNION-based payloads

- We can interact with the vulnerable application by browsing to http://192.168.50.16/search.php from our Kali machine. Once the page is loaded, we can click SEARCH to retrieve all data from the customers table.

<img width="1150" height="549" alt="image" src="https://github.com/user-attachments/assets/f3f71596-81fd-46fb-9aa0-ea3268a14e82" />

- Now that we know there are five columns in the original SQL query, the next step is to determine which columns are displayed using the following query. The result of the above query is displayed in the following image, which better visualizes the table’s columns.

<img width="1156" height="533" alt="image" src="https://github.com/user-attachments/assets/66e42a32-d71c-41dc-8efa-2c4e7f4e83c8" />

- With this information in mind, we can attempt our first attack by enumerating the current database name, user, and MySQL version. Since we want to retrieve all the data from the customers table, we'll use the percentage sign followed by a single quote to close the search parameter. Then, we begin our injected query with a UNION SELECT statement that dumps the current database name, the user, and the MySQL version in the first, second, and third columns, respectively, leaving the remaining two null.

<img width="1141" height="530" alt="image" src="https://github.com/user-attachments/assets/5bbee497-b3b5-4cc6-a6ee-6e0b41310cce" />

- With this in mind, let's update our query by shifting all the enumerating functions to the right-most place, avoiding any type mismatches. Since we already verified the expected output, we can omit the percentage sign and rerun our modified query.

<img width="1154" height="456" alt="image" src="https://github.com/user-attachments/assets/1951380e-ac74-4e3f-a050-c1c9b1caa41a" />

- We'll attempt to retrieve the columns table from the information_schema database belonging to the current database. We'll then store the output in the second, third, and fourth columns, leaving the first and fifth columns null.

<img width="1147" height="606" alt="image" src="https://github.com/user-attachments/assets/cf51018c-5401-424e-aa6d-8e02d7c884b5" />

- Let's craft a new query to dump the users table. Using the above statement, we'll again attempt to store the output of the username, password, and description in the web application table.

  <img width="1157" height="517" alt="image" src="https://github.com/user-attachments/assets/19e0f317-49e1-4f84-a8c4-e7184e22f17d" />

2) Continue working on VM 1 and replicate the SQLi UNION-based attack we have discussed in this Learning Unit. For the UNION-based attack to succeed, what other condition needs to be satisfied in addition to having the same data types among the two queries?
-  The injected UNION query must return the same number of columns as the original query.

####  Blind SQL injections
- The SQLi payloads we have encountered are in-band, meaning we're able to retrieve the database content of our query inside the web application. Alternatively, blind SQL injections describe scenarios in which database responses are never returned and behavior is inferred using either boolean- or time-based logic.
- Once we have logged in with the offsec and lab credentials, we'll encounter the following page:

<img width="1147" height="528" alt="image" src="https://github.com/user-attachments/assets/23a06e67-f03c-4063-9f79-d9adb6e959ab" />

<img width="1154" height="490" alt="image" src="https://github.com/user-attachments/assets/525c157d-532b-45ca-a52a-a67da76f61b4" />

3) Replicate the time-based and boolean-based blind SQL injections described in this Learning Unit on VM 1. Blind SQLi are called like this because the database output is never returned to the user. To infer the result of the query, the output of which component is employed instead?
- web application

- In our database, the Administrator user already has the appropriate permissions. Let's enable xp_cmdshell by simulating an SQL injection via the impacket-mssqlclient tool. After logging in from our Kali VM to the MSSQL instance, we can enable show advanced options by setting its value to 1, then applying the changes to the running configuration via the RECONFIGURE statement. Next, we'll enable xp_cmdshell and apply the configuration again using RECONFIGURE. With this feature enabled, we can execute any Windows shell command through the EXECUTE statement followed by the feature name. 

<img width="992" height="386" alt="image" src="https://github.com/user-attachments/assets/88c43a37-5c3e-4650-85f3-ce2afbcc303f" />

4) Connect to the MSSQL VM 1 and enable xp_cmdshell as showcased in this Learning Module. Which MSSQL configuration option needs to be enabled before xp_cmdshell can be turned on?
-  show advanced options

The written PHP code file results in the following: " <? system($_REQUEST['cmd']); ?>" 

<img width="969" height="614" alt="image" src="https://github.com/user-attachments/assets/7abe7d6f-329a-4b02-9e93-bc4fc18e0bca" />

<img width="1153" height="212" alt="image" src="https://github.com/user-attachments/assets/9b42ffca-70e0-4ba3-8d3a-0596d5b3239e" />

5) Connect to the MySQL VM 2 and repeat the steps illustrated in this section to manually exploit the UNION-based SQLi. Once you have obtained a webshell, gather the flag that is located in the same tmp folder.

<img width="1158" height="408" alt="image" src="https://github.com/user-attachments/assets/e7f7468f-782b-4538-ab98-7ba6cb0c6a01" />

6) Connect to the MySQL VM 2 and automate the SQL injection discovery via sqlmap as shown in this section. Then dump the users table by abusing the time-based blind SQLi and find the flag that is stored in one of the table's records.
(Hint : ' UNION SELECT null, username, password, description, null FROM users -- //)
<img width="1152" height="541" alt="image" src="https://github.com/user-attachments/assets/4241d61e-7568-446c-9157-65ebf9f619bd" />

7) Capstone Lab: Enumerate the Learning Module Exercise - VM #1 and exploit the SQLi vulnerability to get the flag.

<img width="1709" height="836" alt="image" src="https://github.com/user-attachments/assets/1dcae2bd-ad2f-415d-bf2d-87b937427d74" />
