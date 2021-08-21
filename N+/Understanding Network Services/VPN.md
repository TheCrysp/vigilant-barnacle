# Virtual Private Server

**A virtual private network, or VPN, is a powerful tool that prevents corporations and cybercriminals from accessing your personal information**. When you use a VPN, your data travels to a remote server via a secure connection. The remote server [masks your IP address](https://www.vpnmentor.com/blog/how-to-really-hide-your-ip-address-with-a-vpn/), so it looks like you are accessing the internet from another location, which also allows you to **bypass geoblocking and censorship**.

Because of this, VPNs have grown in popularity over the past few years, particularly in countries like China, where online censorship is rampant and sometimes dangerous. However, people all over the globe use VPNs to protect their privacy, anonymity, and unrestricted access to the internet. 

## Remote Access VPN

A remote access virtual private network (VPN) enables users who are working remotely to securely access and use applications and data that reside in the corporate data center and headquarters, encrypting all traffic the users send and receive.

The remote access VPN does this by creating a tunnel between an organization’s network and a remote user that is “virtually private,” even though the user may be in a public location. This is because the traffic is encrypted, which makes it unintelligible to any eavesdropper. Remote users can securely access and use their organization’s network in much the same way as they would if they were physically in the office. With remote access VPN, data can be transmitted without an organization having to worry about the communication being intercepted or tampered with.

## Site to Site VPN

A site-to-site virtual private network (VPN) is a connection between two or more networks, such as a corporate network and a branch office network. Many organizations use site-to-site VPNs to leverage an internet connection for private traffic as an alternative to using private [MPLS](https://www.paloaltonetworks.com/cyberpedia/what-is-mpls) circuits.

Site-to-site VPNs are frequently used by companies with multiple offices in different geographic locations that need to access and use the corporate network on an ongoing basis. With a site-to-site VPN, a company can securely connect its corporate network with its remote offices to communicate and share resources with them as a single ne![image-20210818130736900](/home/crysp/.config/Typora/typora-user-images/image-20210818130736900.png)twork.

## Generic Routing Encapsulation Protocol

Generic Routing Encapsulation, or GRE, is a protocol for encapsulating data packets that use one [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) protocol inside the packets of another protocol. "Encapsulating" means wrapping one data packet within another data packet, like putting a box inside another box. GRE is one way to set up a direct point-to-point connection across a network, for the purpose of simplifying connections between separate networks. It works with a variety of [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) protocols.

1. It does not provide any security.
2. Flexible (Any kind of data can be sent.) 

# IPSEC Protocol

***IPSEC stands for Internet Protocol Security.** It is an Internet Engineering Task Force (IETF) suite of protocols between two communication points across the Internet Protocol network that provide data authentication, data integrity, and confidentiality. IPsec is mostly used to set up VPNs, and works by encrypting IP packets, along with authenticating the source where the packets come from.

We have to establish an IPsec tunnel between two IPsec peers before we protect any IP packets. We use protocol called **IKE (Internet Key Exchange)** to establish an IPsec tunnel**.**

IKE consists of 2 phases in order to build an IPsec tunnel. They are:

- **IKE Phase 1**
- **IKE Phase 2**

### IKE Phase 1

The major purpose of IKE phase 1 is to create a secure tunnel so that we it can be used for IKE phase 2.

The following steps are done in IKE phase 1

- **Negotiation**
- **DH Key exchange**
- **Authentication**

### **IKE phase 2**

The IKE phase 2 is used to protect the user data. Quick mode is built in IKE phase 2 tunnel. In IKE phase 2 tunnel negotiation will be done on the following things.

- **IPsec protocol**
- **Encapsulation mode**
- **Encryption**
- **Authentication**
- **Life time**
- **DH Exchange (Optional)**

IKE construct the tunnels but it doesn’t authenticate or encrypt user data. For this we use two other protocols:

- AH (Authentication Header)
- ESP (Encapsulating Security Payload)

Both protocols AH and ESP supports authentication and integrity but ESP supports encryption also. Because of this reason, ESP is the most commonly used protocol nowadays.

The above two protocols support two modes. They are

- **Tunnel Mode**
- **Transport Mode**

One of the main difference between the two modes is that original IP header is used in the Transport mode and new IP header is used in the Tunnel mode.

![img](https://i0.wp.com/ipwithease.com/wp-content/uploads/2020/10/GRE-over-IPsec-vs-IPsec-over-GRE-1.jpg?resize=800%2C455&ssl=1)



The whole process of IPsec is done in five steps. They are as follows

- **Initiation**
- **IKE Phase 1**
- **IKE Phase 2**
- **Data Transfer**
- **Termination**



1. Provides:

   - Confidentiality: Encryption
   - Integrity: Hashing
   - Authentication: PSKs or Digital Signatures
   - Anti- Reply: Applies Serial Numbers to Packets

2. Can encapsulate unicast IP packets

3. Two Modes

   - Transport Mode: Uses Packet's original header
   - Tunnel Mode: Encapsulates entire packet

   

## GRE over IPsec

![image-20210818130456674](/home/crysp/.config/Typora/typora-user-images/image-20210818130456674.png)

1. GRE encapsulates nearly any traffic type into GRE packets, which is unicast IP packets.
2. TheGRE packets are protected over the IPsec tunnel.





