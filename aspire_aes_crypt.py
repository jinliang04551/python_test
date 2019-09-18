#-*-coding:utf-8-*-
#author: maokebing

from Crypto.Cipher import AES 


class AESCrypt():  
    def __init__(self,key,iv):  
        self.key = key  
        self.iv  = iv  
        self.mode = AES.MODE_CBC  
        self.BS = AES.block_size  
        #补位  
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)   
        self.unpad = lambda s : s[0:-ord(s[-1])]  
       
    def encrypt(self,text):  
        text = self.pad(text)  
        cryptor = AES.new(self.key,self.mode,self.iv)  
        ciphertext = cryptor.encrypt(text)  
        return ciphertext  
       
    #解密后，去掉补足的空格用strip() 去掉  
    def decrypt(self,text):  
        cryptor = AES.new(self.key,self.mode, self.iv)  
        plain_text  = cryptor.decrypt(text)  
        return self.unpad(plain_text.rstrip('\0')) 