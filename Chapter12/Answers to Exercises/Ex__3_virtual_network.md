__Modern Computer Architecture and Organization Second Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 12, Exercise 3

Create two separate copies of your Ubuntu guest machine in your host system’s VirtualBox environment. Configure both Ubuntu guests to connect to the VirtualBox *internal* network. Set up the two machines with compatible Internet Protocol addresses. Verify each of the machines can receive a response from the other using the *ping* command. By completing this exercise, you will have configured a virtual network within your virtualized environment.

# Answer
1. In your host system VirtualBox, with the Ubuntu machine not running, open the **Settings** dialog for the Ubuntu VM you set up in [Exercise 1](Ex__1_vbox_ubuntu.md) and select the *Network* settings. Set the **Attached to:** network type to *Internal Network**, then click **OK**.

1. Right-click on the Ubuntu VM in the VirtualBox manager and select **Clone...** from the context menu. Click **Next** in the *Clone Virtual Machine* menu. Leave **Full clone** selected and click **Clone**. Wait for the cloning process to complete.

1. Open a command prompt on your host system and navigate to the installation directory for VirtualBox. On Windows, this command takes you to the default installation location:
```
cd "\Program Files\Oracle\VirtualBox"
```

4. Start a DHCP server for the *intnet* VirtualBox network with this command:
```
VBoxManage dhcpserver add --netname intnet --ip 192.168.10.1 --netmask 255.255.255.0 --lowerip 192.168.10.100 --upperip 192.168.10.199 --enable
```

5. Start both of the VMs. Based on the DHCP server settings recommended in the previous step, the VMs might be assigned the IP addresses 192.168.10.100 and 192.168.10.101.

1. Login to both of the running VMs and open a terminal window in each one. Enter the following command in each terminal to display the system IP address:
```
hostname -I
```

1. Ping one machine from the other. For example, if the first machine's IP address is 192.168.10.100 and the second is 192.168.10.101, enter the following command on the first machine:
```
ping 192.168.10.101
```

8. You should see a response similar to the following. Press *Ctrl+C* to stop the updates:
```
osboxes@osboxes:~$ ping 192.168.10.101
PING 192.168.10.101 (192.168.10.101) 56(84) bytes of data.
64 bytes from 192.168.10.101: icmp_seq=1 ttl=64 time=0.372 ms
64 bytes from 192.168.10.101: icmp_seq=2 ttl=64 time=0.268 ms
64 bytes from 192.168.10.101: icmp_seq=3 ttl=64 time=0.437 ms
64 bytes from 192.168.10.101: icmp_seq=4 ttl=64 time=0.299 ms
^C
--- 192.168.10.101 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3054ms
rtt min/avg/max/mdev = 0.268/0.344/0.437/0.065 ms
osboxes@osboxes:~$ 
```

9. Repeat the *ping* command on the second machine, switching the target to the IP address of the first machine.
