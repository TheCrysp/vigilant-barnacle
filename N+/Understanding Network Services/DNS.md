# What is DNS and how does it work?



DNS is what lets users connect to websites using domain names instead of IP addresses. 



## What is DNS?

The Domain Name System(DNS) is the phone book of the Internet. Humans access information online through domain names, like google.com, espn.com. Web browsers interact through IP addresses. DNS translates domain to IP address so browsers can load Internet resources. 

Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses such as 192.156.1.2 or more complex IP addresses such as 2400:cb00:2048:1::c629:d7a2.

# How DNS works?

The process of DNS resoulation involve converting a hostname(www.espn.com) into a computer-friendly IP address(192.155.3.10). An IP address is given to each device on the Internet, and the address is necessary to find the appropriate Internet device = like a street address is used to find a particular home. 

When a user wants to load a web page, a translation must occur between what a user types into their web browser(example.com) and the machine-friendly address necessary to locate the example.com web page.

In order to understand the process behind the DNS resolution, it’s important to learn about the different hardware components a DNS query must pass between. For the web browser, the DNS lookup occurs “ behind the scenes” and requires no interaction from the user’s computer apart from the initial request.



## There are 4 DNS servers involved in loading a web page:

- **DNS recursor -** The recursor can be thought of as a librarian who is asked to go find a particular book somewhere in a library. The DNS recursor is a server designed to receive queries from client machines through applications such as web browsers. Typically the recursor is then responsible for making additional requests in order to satisfy the client's DNS query. 
- **Root nameserver -** The root server is the first step in translating(resolving) human readable  host names into IP. It can be thought of like an index in a library that points to different racks of books - typically it serves as a reference to other more specific locations.

- **TLD nameserver** - The top level domain server (TLD) can be thought of as a specific rack of books in a library. This nameserver is the next step in the search for a specific IP address, and it hosts the last portion of a hostname (In example.com, the TLD server is “com”).

