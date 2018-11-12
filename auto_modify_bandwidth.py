#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys,time,json
from logger import logger,set_log_file


arg_length = len(sys.argv)
ApiClient = UcloudApiClient(base_url, public_key, private_key)


#定义修改带宽的类，并定义一些列的方法。
class modifyBandwidth(object):
	def __init__(self,eipid):
		self.eipid = eipid

	def getBandwidth(self):  #定义获取带宽利用率方法，返回带宽利用率，如，0.313
		Parameters = {
			"Action":"DescribeBandwidthUsage",
			"Region":region,
			"EIPIds.0":self.eipid
		}
		response = ApiClient.get("/", Parameters)
		return response['EIPSet'][0]['CurBandwidth']
		
	def getEip(self):  #定义获取EIP信息方法，返回当前带宽大小。
		Parameters = {
			"Action":"DescribeEIP",
			"Region":region,
			"EIPIds.0":self.eipid
		}
		response = ApiClient.get("/", Parameters)
		return response['EIPSet'][0]['Bandwidth']

	def addBandwidth(self,addTo): #定义增加带宽的方法
		Parameters = {
			"Action":"ModifyEIPBandwidth",
			"Region":region,
			"EIPId":self.eipid,
			"Bandwidth":addTo
		}
		response = ApiClient.get("/", Parameters)
		print response

	def reduceBandwidth(self,reduceTo):  #定义减少带宽的方法
		Parameters = {
			"Action":"ModifyEIPBandwidth",
			"Region":region,
			"EIPId":self.eipid,
			"Bandwidth":reduceTo
		}
		response = ApiClient.get("/", Parameters)
		print response


def getEIPId(): #获取EIP所有信息
		Parameters = {
			"Action":"DescribeEIP",
			"Region":region
		}
		response = ApiClient.get("/", Parameters)
		return response

def listEIP(): #从所有信息里提取EIPid，并存入数组eipIdArray里。
	eipInfor = getEIPId()
	number =  eipInfor['TotalCount']
	for i in range(number):
		eipIdArray.append(eipInfor['EIPSet'][i]['EIPId'])
	return eipIdArray

def adjustBandwidth(eipid): #调整带宽主逻辑
	AutoEIP = modifyBandwidth(eipid)  #类封装给AutoEIP，并传入参数。
	utilization = AutoEIP.getBandwidth() #带宽使用率，通过类的方法
	curBandwidth = AutoEIP.getEip() #当前带宽，通过类的方法
	logger.info("This EIP %s utilization is %f,and the bandwidth is %dM" % (eipid,utilization,curBandwidth))

	try:
		#当带宽利用率超过70%，并且当前带宽还未到最高限制带宽，每次增加设置的步长带宽。
		if utilization >= 0.7 and curBandwidth <= maxBandwidth:
			newBandwidth = curBandwidth + stepBandwidth
			AutoEIP.addBandwidth(newBandwidth)
		#当前带宽利用率低于10%，并且当前带宽还未到最低地位带宽，每次减少设置的步长带宽。
		elif utilization <= 0.1 and curBandwidth > minBandwidth:
			newBandwidth = curBandwidth - stepBandwidth
			AutoEIP.reduceBandwidth(newBandwidth)
		else:
			logger.info("Do nothing,This the max bandwidth or the min bandwidth ,please ajust")
	except Exception,e:
		print Exception,":",e

def main():
	while True:
		if eipIdArray:
			eipIdList = eipIdArray
		else:
			eipIdList = listEIP() #获取所有EIPID

		ajustEip = list(set(eipIdList).difference(set(noAjustEip)))  #剔除不参与的EIP。
		for i in ajustEip:
			adjustBandwidth(i)
		time.sleep(durtime)


if __name__=='__main__':
	main()