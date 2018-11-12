#-*- encoding: utf-8 -*-
#配置公私钥"""
public_key  = ""
private_key = ""
project_id = "" # 项目ID 请在Dashbord 上获取

base_url    = "https://api.ucloud.cn"


#配置EIP带宽相关参数
region = 'cn-south-02' #可用区，请参考region文件
maxBandwidth = 5  #扩容到的最大带宽
minBandwidth = 1   #缩容到的最小带宽
stepBandwidth = 3 #每次扩容/缩容的带宽大小，单位M
eipIdArray = [] #所有EIPID的存储数组，如不填写，则自动提取，如填写则只操作填写的EIP
noAjustEip = ['eip1'] #手动填写，不参与调整的EIPid，比如这次不参与调整有2个IP
durtime = 300 #下次调整带宽时间间隔，单位秒
