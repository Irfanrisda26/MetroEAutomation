# Metro-E Automation
Script for Metro-E Router Automation Based on Python
Beware the command on this script only work on Nokia/Alcatel-lucent Metro-E Router
To use this script on another router you need to change everything on the script and I can't help you with that.

I create this script for the sake to simplify my work as a Network Engineer
Every day I work with a live router at a national level of my country which I believe as a high-risk job.
To Reduce as many as possible of human errors on this job, I tried to create this script to do the job.

While it can reduce errors it also helps me out as I don't need to manually input and configure the router.

## Pre-Act Script Metro-E Router (Alcatel-lucent/Nokia)

Collecting data before doing something on a live router sometimes takes too much time as we need to manually input some parameter, such as:

-Port on the router
Every router has a different number of ports, because of this we need to create a new command for every router we work on. This could be easy if we only work on 1 Router, but if we work on the entire ring of a network, it will take too much time.

-IP Address of far-end router interface
The router will have different IP Addresses on its router interface. Usually, a live router will have more than 3 router interface and for that reason, we need to manually create ping command on every router. This task also takes time if consider work with many routers at one time.

-Multiple routers.
If we work on the entire ring of the network, usually we will collect every state of a router on that ring before doing something. We need constantly log in and logout for every router and then run our command.
-etc

This script can help you out for collecting data on a router, in this case, I am using this script on Metro-E Router (Nokia/Alcatel-lucent).
What this script do are :

0. Automatic login with 'telnet' 
   You need to input username and password for the first time when you ran this script command telnet can be changed if you use another login method such as SSH.
1. Collecting traffic of Port in the specific router automatically
   You don't need to input what port to monitor because this script will scan all ports that available on the router and monitor it for 3 secs interval.
2. Ping IP interface 
   You don't need to manually input the IP interface as this script will scan it and create the ping command itself.
   in this case, this script will calculate the IP interface of the far-end with /30 prefix.
   ex: IP intf on Roouter a
        192.168.0.1/30
        IP intf on Router b
        192.168.0.2/30
3. Every 'show' mandatory command such as :
    - List service
    - List SAP and SDP
    - Router interface
    - System Information 
    - Module detail
    - MPLS Detail
    this command specified only for a metro-e router of Nokia/Alcatel-lucent product
    
How to Use :
1. Put hostname or ip on router.txt (no limitation put as many as you want)
1. Connect to a session.
2. also you need to change your idle string on the script if your session has different than mine looks like this ![string image](https://github.com/ridhoalif/MetroEAutomation/blob/master/string.PNG)
   and for router idle string will be the same if you use Nokia/Alcatel-lucent metro-e Router. You can change this on the script line 26.
3. For Aditional command, you can add it on cm_ceklist.txt
4. I use SecureCRT as a telnet client, so to run a script you just need to click script on the menu bar.
5. The output will be hostname/ip_FULL.txt and hostname/ip_ceklist.txt

## SCRIPT USAGE
Feel free to use this script for educational purposes.
Please contact me if you want to use this script for commercial purpose
   

