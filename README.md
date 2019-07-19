# mitm-proxy
Using a MITM proxy to add a browser-based keylogger to devices on your local network

# How does it work?

This works by injecting the following Javascript code into every request that takes place on the network.

<p align="center">
<img width=700px src ="static/code.png">
</p>


## Demo

### Client Side

The user browses the web normally and does not experience any warnings/interuptions.

<p align="center">
<img width=500px src ="static/demo.gif">
</p>

### Server Side

On the server side, we have logic that categorizes the keystrokes by the hostname of the site the request is sent from.  It saves the keystrokes by hostname in the root directory of the project.

```bash
$ cat www.ebay.com
raspberry piEnteraphone casesEnter9400Backspace30
```

```bash
$ cat signin.ebay.com
totallynotarealemail@gmail.comfakepasswordEnter
```
