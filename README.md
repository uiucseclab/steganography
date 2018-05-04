# steganography
Steganography is a way to communicate messages through pictures. You simply encode the message within the picture and the receiver will decode the message using the picture. The receiver and recipient must be capable of running the script to communicate. Python Version 2.7 was used to create this application.

## Getting Started
User must have python in order to run the scripts. Any python package not installed on a user's system will give the command line output:

```
No module named: X
```

when running the application. At this point, a user can simply run

```
pip install X
```

to install required package.

If the user wants to use the email functionality, the user must ensure that their email settings allow programs to log into their email account (ex. two-factor authentication on an email will be too secure for this functionality). Fortunately, we have a generic account from which a user can send emails as well.

A video of the functioning application is attached to see its functionality.  Click on Ms. Lisa to get to the tutorial.

[![Steganography Tutorial](http://i63.tinypic.com/2iicwfc.jpg)](https://youtu.be/gRFQSoUDvr0 "Steganography Tutorial")

## Running the Program
Run the steganography.py with

```
./steganography.py
```

from a UNIX command line to see instructions on its use.  The user is first given the option to encode or decode an image.  

If decode is chosen, the user must provide the path to an image to be decoded, and the hidden message is printed to the screen.  If encode is chosen, the user must input the path to an image, path to a text file that holds the desired message to be encoded, and the output filename for the image with the encoded text. Once the image is encoded, the user then has the option to send the image through email programmatically.

## Authors
* **Nomaan Dossaji** - [ndossaji](https://github.com/ndossaji)
* **Joe Vande Vusse** - [joevandevusse](https://github.com/joevandevusse)
* **Taran Saggu** - [tarandeepsaggu](https://github.com/tarandeepsaggu)
