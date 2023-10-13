# Solution
The file has a jpg extension, but upon executing `file` command on it, the result is a PDF document.
```
> file liar.jpg
liar.jpg: PDF document, version \020.F
```
We can check the file header for anomalies.
![APDF Header in JPG Image](attachments/image-3.png)

We can see that the Header is that of a PDF file. Yet, there is still the JFIF part of a regular jpeg image.
![JFIF Header](attachments/image.png)

We can edit the content of the header to change it to a regular format.
![Fixed Header](attachments/image-2.png)

We can now open the image correctly:
![Liar](liar-1.jpg)