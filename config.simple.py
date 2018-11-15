#-*- encoding: utf-8 -*-
#配置公私钥"""
public_key  = ""
private_key = ""
project_id = "" # 项目ID 请在Dashbord 上获取
base_url    = "https://api.ucloud.cn"

mode = 'alarm' #(auto|manual|alarm)
#auto 自动获取项目中所有EIP
#manual 指定EIP方式，指定EIP，放到eipIdArray[]里。
#alarm 通过告警出来的EIP。

#配置EIP带宽相关参数
maxBandwidth = 5  #扩容到的最大带宽
minBandwidth = 1   #缩容到的最小带宽
stepBandwidth = 1 #每次扩容/缩容的带宽大小，单位M

eipIdArray = [] #只有在manual模式下有效。所有EIPID的存储数组.
noAjustEip = ['eip1'] #三种模式下都有效。手动填写，不参与调整的EIPid，比如这次不参与调整有2个IP
durtime = 300 #下次调整带宽时间间隔，单位秒
region = 'cn-south-02' #可用区，请参考region文件
