# -*-coding:utf-8-*-
#!/usr/bin/python2.7

import smtplib  
from email.mime.text import MIMEText  
from email.header import Header

#发邮件
def send_email(mail_me, user, pwd, to_list, msg):
    # 登录名，不用修改，自动生成
    mail_loginname = 'aspire' + "\\" + user
    try:  
        server = smtplib.SMTP()  
        # debug
        # server.set_debuglevel(1)
        server.connect('mail.aspirehld.com')  
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(mail_loginname, pwd)  
        server.sendmail(mail_me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False 
 
 #发纯文本邮件
def send_nomal_mail(user, pwd, to_list, subject, plain_text):
    mail_postfix="aspirecn.com"  #发件箱的后缀
    mail_me = "hello"+"<"+user+"@"+mail_postfix+">"   
    message = MIMEText(plain_text, _subtype='plain', _charset='utf-8') 
    message['Subject'] = subject  
    message['From'] = mail_me  
    message['To'] = ";".join(to_list)  
    return send_email(mail_me, user, pwd, to_list, message);

#发html格式的邮件
def send_html_email(user, pwd, to_list, subject, html_text):
    mail_postfix="aspirecn.com"  #发件箱的后缀
    mail_me = "hello"+"<"+user+"@"+mail_postfix+">" 
    message = MIMEText(html_text, 'html', 'utf-8')
    message['From'] = mail_me
    message['To'] =  ";".join(to_list)
    message['Subject'] = Header(subject, 'utf-8')
    return send_email(mail_me, user, pwd, to_list, message);

#解析返回的json
def parse_json(file_name, app_type):
    import json
    d = json.loads(open(file_name).read())['data']
    out  = u' %s %s Beta V%s build %s\n' % (d['appName'], app_type,  d['appVersion'],  d['appBuildVersion']) 
    out += u' 下载地址: http://www.pgyer.com/%s' % (d['appShortcutUrl'])
    return out


import sys

#配置部分====================================================================

# 发件人的域帐号和密码
user = 'maokebing'
# 密码
pwd = 'Kebing%2016'

user_sign = u'''
毛可兵 Kebing
------------------------------------------
教育业务部 
北京市丰台区南四环西路186号汉威国际广场四区12号楼7层
电子邮件：maokebing@aspirecn.com
移动电话：13466531630
公司网站：www.aspirecn.com
'''

#收件人
mailto_list = ['edutest@aspirecn.com']          #测试组(测试人员)
mailto_list.append('educlient@aspirecn.com')    #客户端组(iOS & Andorid 开发人员)


#邮件主题
mail_subject = u'【云南】iOS版本提测'

#配置完成=========================================================================

# print sys.argv[1]
# print sys.argv[2]

# exit()

#邮件内容
mail_content  = u'** 上传成功! **'
mail_content += u'\n'
mail_content += u'==========================================================='
mail_content += u'\n'
mail_content += parse_json('parent.json' , u'家长版')
mail_content += u'\n'
mail_content += parse_json('teacher.json' , u'老师版')
mail_content += '\n'
mail_content += u'==========================================================='
mail_content += u'\n'
mail_content += user_sign

print  '\n'
print  u'**创建邮件**' 
print  u'========================================================\n'
print  u'收件人:\n'
for x in mailto_list:
    print x + '\n'
print  u'邮件主题:' + mail_subject + '\n'
print  u'邮件正文:\n' 
print   mail_content
print  u'========================================================\n'


in_str = raw_input("确认要发送邮件吗?[y/n]")
if in_str != 'y':
    exit(0)

print u"\n发送邮件..." 

 # if send_html_email(user, pwd, mailto_list, mail_subject, mail_content):
if send_nomal_mail(user, pwd, mailto_list, mail_subject, mail_content):
    print u"发送成功!\n"  
else:  
    print u"发送失败\n" 