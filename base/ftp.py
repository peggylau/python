# coding=utf-8
import ftplib

#ftp匿名登陆,用户名anonymous,密码为邮件地址
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','me@your.com')
        print '\n[*] ' + str(hostname) + \
            ' ftp Anonymous logon succeeded.'

        returnDefault(ftp)

        ftp.quit()
        return True
    except Exception,e:
        print e
        #print '\n[-] ' + str(hostname) + \
            #' ftp Anonymous login failed.'
        return False


#列出FTP目录
def returnDefault(ftp):
    dirList = []
    try:
        dirList = ftp.dir()
        print dirList
        retList = []
        for filename in dirList:
            fn = filename.lower()
            print fn
            if '.php' in fn or '.htm' in fn or '.asp' in fn:
                print '[+] Found default page: ' + filename
                retList.append(filename)
    except Exception,e:
        print e

    return retList

if __name__=='__main__':
    host = '192.168.191.206'
    anonLogin(host)