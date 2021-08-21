## DHCP definition

DHCP stands for dynamic host configuration protocol and is a network protocol used on IP networks where a DHCP server automatically assigns an IP address and other information to each host on the network so they can communicate efficiently with other endpoints.

In addition to the IP address, DHCP also assigns the subnet mask, default gateway address, domain name server (DNS) address and other pertinent configuration parameters. Request for comments (RFC) 2131 and 2132 define DHCP as an Internet Engineering Task Force (IETF)- defined standard based on the BOOTP protocol.

![image-20210819120755394](/home/crysp/.config/Typora/typora-user-images/image-20210819120755394.png)

![image-20210819143953359](/home/crysp/.config/Typora/typora-user-images/image-20210819143953359.png)











## Steps of DORA process in DHCP:

Now let’s take a look at what happens when these messages are exchanged between **DHCP Client** and **DHCP Server.**

Two key items should be kept in mind which are also important from interview point of view as well.

These are –

1. ***\*Network layer broadcast and\****
2. **Data Link Layer broadcast.**

### **STEP 1: DHCP DISCOVER**

![img](https://i2.wp.com/ipwithease.com/wp-content/uploads/2020/06/DORA-PROCESS-STEP1.jpg?resize=800%2C455&ssl=1)

DHCP client sends out a DHCP Discover message to find out the DHCP server. DHCP discover message is a layer 2 broadcast as well as layer 3 broadcast.

Fields in DHCP Discover Message:



**Src IP: 0.0.0.0**



**Dst IP: 255.255.255.255**

**Src MAC : DHCP clients MAC address**

**Dst MAC: FF:FF:FF:FF:FF:FF** 



Hence from the above fields it is clear **DHCP Discover message is a Network Layer and Data Link Layer Broadcast.**

### **STEP 2: DHCP OFFER**

![img](https://i2.wp.com/ipwithease.com/wp-content/uploads/2020/06/DORA-PROCESS-STEP2.jpg?resize=800%2C455&ssl=1)



DHCP server receives the DHCP discover a message from the client and sends back the DHCP offer message with field information as below:



**Src IP: DHCP Server** **IP Address**



**Dst IP: 255.255.255.255  #Still Broadcast as Client still has no IP Address#**

**Src MAC : MAC Address of DHCP Server**

**Dst MAC: DHCP clients MAC address**



Hence from above field it is clear that **DHCP offer message is a layer 2 unicast but still as layer 3 broadcast.**

### **STEP 3: DHCP REQUEST**

![img](https://i2.wp.com/ipwithease.com/wp-content/uploads/2020/06/DORA-PROCESS-STEP3.jpg?resize=800%2C455&ssl=1)





DHCP client receives the DHCP offer from DHCP server and sends back a DHCP Request message with following fields:



**Src IP: 0.0.0.0 #As still the IP address hasn’t been assigned to Client#**



**Dst IP: 255.255.255.255  #Still Broadcast as Client must have received Offer from more than one DHCP server in their domain and the DHCP client accepts the Offer that its receives the earliest and by doing a broadcast it intimates the other DHCP server to release the Offered IP address to their available pool again #**

**Src MAC : DHCP clients MAC address**

**Dst MAC: FF:FF:FF:FF:FF:FF**

> 

Above fields concludes that **DHCP request message is also a layer 2 unicast and a layer 3 broadcast.**

 

### **STEP4: DHCP ACK**

![img](https://i0.wp.com/ipwithease.com/wp-content/uploads/2020/06/DORA-PROCESS-STEP4.jpg?resize=800%2C455&ssl=1)

Once the DHCP client sends the request to get the Offered [IP address](https://en.wikipedia.org/wiki/IP_address), DHCP server responds with an acknowledge message towards DHCP client with below fields:



**Src IP: DHCP Server IP Address**



**Dst IP: 255.255.255.255**

**Src MAC : MAC Address of DHCP Server**

**Dst MAC: DHCP clients MAC address**



 From above fields substantiates that **DHCP Acknowledge is a layer 2 unicast but still a layer 3 broadcast.**

For more details on the information you must get familiar with the DHCP header fields. Few important fields from DHCP header for our reference are as below –



**Ciaddr:** Client IP address.**Yiaddr ‘your’** (client) IP address: Server’s response to client.



**Siaddr Server IP address:** Address of sending server or of the next server to use in the next Bootstrap process step.

**Giaddr:** Relay agent IP address, used in booting via a relay agent.

**Chaddr:** Client hardware address.



- **Is DHCP OFFER a Unicast/Multicast?**
- **DHCP OFFER** is a layer3 broadcast as the server doesn’t know client’s IP address. It only knows the client’s MAC address.
- **What is an IP lease in DHCP?**
- DHCP server allocates a dynamic IP address to the client for a period(lease) known as the **IP lease**.
- **What is the default duration of IP lease in DHCP?**
- The default duration of IP lease is **8 days.**
- **What is DHCP port number?**
- DHCP uses UDP port number **67** for the DESTIANTION SERVER and UDP port number **68** for the CLIENT.
- **What do you understand by NACK in DHCP?**
- **DHCP NACK** message is sent to the client to tell that the requested IP address can’t be provided by the DHCP server.
