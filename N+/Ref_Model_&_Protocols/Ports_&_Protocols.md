# 1.5 PORTS and PROTOCOLS



## Protocols?

In networking, a protocol is a set of rules for formatting and processing data. Network protocols are like a common language for computers. The computers within a network may use vastly different software and hardware; however, the use of protocols enables them to communicate with each other regardless.

## Ports?

A port is a virtual point where network connections start and end. Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service. Ports allow computers to easily differentiate between different kinds of traffic: emails go to a different port than webpages, for instance, even though both reach a computer over the same Internet connection.

**_Well-Known Ports:_** 0-1023 Offers well-known network services

**_Registered Ports:_** 1024-49151 Registered with the Internet Assigned Numbers Authority(IANA)

**_Ephemeral Ports_**: 49152-65535 (a.k.a. Dynamic Ports or Private Ports)



:warning: FTP (File Transfer Protocol) is a protocol used to transfer files over a network. FTP uses two ports: 20 and 21. TCP Port 20 is used for data transfer and TCP port 21 is the control port used by FTP. TCP port 22 is used by SSH (Secure Shell). Port 12 doesn’t correspond to any protocol.

:bulb: The MTU (Maximum Transmission Unit) is the maximum amount of data that can be transmitted within a single packet. The default MTU size for Ethernet networks is 1500 bytes.





FTP                    20 and 21

SSH                       22

SFTP                      22

Telnet                     23

SMTP                     25

DHCP                     67

HTTP                       80

HTTPS                     443

POP3                        110

NTP                            995

IMAP                           123

