# Challenge 1

Upon opening the capture in Wireshark, the first thing we can do is look at the protocols used in transfers. We can do this through Statistics -> Protocol Hierarchy window.
![Protocol Hierarchy](attachments/image-1.png)

Here we can see different protocols used used in the capture. However, one protocol in particular catches the eye. It is HTTP.
![HTTP](attachments/image-2.png)

Due to it being in plaintext, we can easily extract information out of it. We can do this through File -> Export Objects -> HTTP window
![Export Objects](attachments/image-3.png)

Looking through the capture we find an image, we can click on preview to look at it.
![Flag](attachments/image.png)

# Challenge 2

As with the first challenge, we find that it HTTP is used somewhere in the capture. We can filter our results to only show HTTP packets.
![HTTP Filter](attachments/image-4.png)

We can see a bunch of HTTP requests and responses. These requests seem interesting, so we will look at their content by following the HTTP stream. Right-click on a packet -> Follow -> HTTP Stream
![Follow HTTP Stream](attachments/image-5.png)
![First Part](attachments/image-6.png)
We can do this for the three parts of the hash.
84d961568a65073a3bcf0eb216b2a576

We can use an online hash cracker to finally crack it.