# 2.2 CSMA/CD Vs. CSMA/CA

## CSMA/CD

CSMA/CD (Carrier Sense Multiple Access/ Collision Detection) is a media-access control method that was widely used in Early Ethernet technology/LANs, When there used to be shared 
Bus Topology and each Nodes( Computers) were connected By Coaxial Cables

**How CSMA/CD works?** 

- **Step 1:** Check if the sender is ready for transmitting data packets.
- **Step 2:** Check if the transmission link is idle? 
  Sender has to keep on checking if the transmission link/medium is idle. For this it continuously senses transmissions from other nodes. Sender sends dummy data on the link. If it does not receive any collision signal, this means the link is idle at the moment. If it senses that the carrier is free and there are no collisions, it sends the data. Otherwise it refrains from sending data.
- **Step 3:** Transmit the data & check for collisions. 
  Sender transmits its data on the link. CSMA/CD does not use ‘acknowledgment’ system. It checks for successful and unsuccessful transmissions through collision signals. During transmission, if collision signal is received by the node, transmission is stopped. The station then transmits a jam signal onto the link and waits for random time interval before it resends the frame. After some random time, it again attempts to transfer the data and repeats above process.
- **Step 4:** If no collision was detected in propagation, the sender completes its frame transmission and resets the counters.

## CSMA/CA

CSMA/CA (Carrier Sense Multiple Access/Collision Avoidance) is a [protocol](https://searchnetworking.techtarget.com/definition/protocol) for carrier transmission in [802.11](https://searchmobilecomputing.techtarget.com/definition/80211) networks. Unlike CSMA/CD (Carrier Sense Multiple Access/Collision Detect) which deals with transmissions after a collision has occurred, CSMA/CA acts to prevent collisions before they happen.

In CSMA/CA, as soon as a node receives a packet that is to be sent, it checks to be sure the channel is clear (no other node is transmitting at the time). If the channel is clear, then the packet is sent. If the channel is not clear, the node waits for a randomly chosen period of time, and then checks again to see if the channel is clear. This period of time is called the backoff factor, and is counted down by a backoff counter. If the channel is clear when the backoff counter reaches zero, the node transmits the packet. If the channel is not clear when the backoff counter reaches zero, the backoff factor is set again, and the process is repeated.