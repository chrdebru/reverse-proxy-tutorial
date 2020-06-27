# Serving Linked Data: A Step-by-Step Tutorial

[Christophe Debruyne ](http://christophedebruyne.be/)  
---
[ADAPT](https://www.adaptcentre.ie/), [Trinity College Dublin](https://www.tcd.ie/)  
[WISE](https://wise.vub.ac.be/), [Vrije Universiteit Brussel](https://www.vub.be/)

# 1 Introduction

This 10-minute tutorial aims to demonstrate how reverse proxies can be used to reduce the number of attack vectors in complex networked systems.

This Github repository provides you the files that were used as a running example. The slides of the presentation can be found [here](./2020-06-30-reverse-proxies.pdf).

# 2 Setup
The Apache2 server acting as a reverse proxy is assumed to be listening to port 80. For this tutorial, it does not matter to know the machine's exact IP-address. In a more realistic setting, the IP-address of the server would be registered in a DNS, for example. At the time of writing, my server was running on a machine with IP-address 192.168.0.16.

Also, make sure that the Apache2 server is configured to relate the domains `www.example.org`, `system1.example.org`, `system2.example.org`. You can do this by adding the following lines to your `/etc/hosts` file. Notice that I used 127.0.0.1.

```
127.0.0.1	example.org
127.0.0.1 system1.example.org
127.0.0.1 system2.example.org
```

The repository also provides to simple Flask applications. Run them with the scripts `runsystem1.sh` and `runsystem2.sh`, ideally on (a) different (virtual) machine(s). The first will run the application on port 5000 (Flask's default port), the other will set the port to 5050. As those ports need to be accessed by the reverse proxy, you may need to open those ports for this tutorial. Do not forget to close these ports afterwards. In the slides, the applications run on a machine with IP-address 192.168.0.33.

# 3 Execution

This tutorial assumes you have installed Apache2. The default location of the configuration files is `/etc/apache2/`. Inside that folder, you will be find a folder named `sites-enabled` (on *nix systems). This usually contains a file (symbolic link) called `000-default.conf`.

It is a best practice to put configurations in `sites-available` and creating symbolic links in `sites-enabled`. For the purpose of demonstrating the reverse proxy, you can just drop the files `001-system1.conf` and `002-system2.conf` in the latter. Notice the naming convention. This convention isn't strict. Just make sure that the file `000-default.conf` comes first in alphabetical order, as it will provide parameters "enhireted" by the two virtual hosts.

One the files are in place, make sure that you change the IP-addresses in those to that of the machine running the Flask applications. Restart the Apache2 server (e.g., `$ sudo systemctl restart apache2`) and the reverse proxy should behave as shown on the slides.


# License
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
