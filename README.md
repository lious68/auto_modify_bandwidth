用途：自动伸缩EIP带宽  
  
使用方法：  
一、打开config.py文件，配置必要的参数。  
  
#配置公私钥"""  
public_key  = ""  
private_key = ""  
project_id = "" # 项目ID 请在Dashbord 上获取  
base_url    = "https://api.ucloud.cn"  
  
mode = 'alarm' #(auto|manual|alarm)  
#auto 自动获取项目中所有EIP  
#manual 指定EIP方式，指定EIP，放到eipIdArray[]里。  
#alarm 通过告警出来的EIP。  
  
dynamic = 'ON' #(ON|OFF) #动态调整带宽开关，如果ON，则下面的EIP配置带宽stepBandwidth参数无效。  
percent = 0.5 #自动调整带宽的步长，百分比。  
  
 #配置EIP带宽相关参数  
maxBandwidth = 6  #扩容到的最大带宽  
minBandwidth = 1   #缩容到的最小带宽  
stepBandwidth = 1 #每次扩容/缩容的带宽大小，单位M  
  
#全局通用参数  
eipIdArray = [] #只有在manual模式下有效。  
noAjustEip = ['eip1'] #三种模式下都有效。手动填写，不参与调整的EIPid，
durtime = 50 #下次调整带宽时间间隔，单位秒  
region = 'cn-south-02' #可用区，请参考region文件  
