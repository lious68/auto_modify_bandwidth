#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import json


arg_length = len(sys.argv)
ApiClient = UcloudApiClient(base_url, public_key, private_key)
region = 'cn-south-02'


#定义修改带宽的类，并定义一些列的方法。
class modifyBandwidth(object):
	def __init__(self,eipid,addTo,reduceTo):
		self.eipid = eipid
		self.addTo = addTo
		self.reduceTo = reduceTo


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


	def addBandwidth(self): #定义增加带宽的方法
		Parameters = {
			"Action":"ModifyEIPBandwidth",
			"Region":region,
			"EIPId":self.eipid,
			"Bandwidth":self.addTo

		}
		response = ApiClient.get("/", Parameters)
		print response


	def reduceBandwidth(self):  #定义减少带宽的方法
		Parameters = {
			"Action":"ModifyEIPBandwidth",
			"Region":region,
			"EIPId":self.eipid,
			"Bandwidth":self.reduceTo
		}
		response = ApiClient.get("/", Parameters)
		print response


if __name__=='__main__':
	#参数
	targetEip = 'eip-e3vzeb'
	highBandwidth = 5
	lowBandwidth = 1
	
	AutoEIP = modifyBandwidth(targetEip,highBandwidth,lowBandwidth)  #类封装给AutoEIP，并传入参数。
	utilization = AutoEIP.getBandwidth() #带宽使用率，通过类的方法
	curBandwidth = AutoEIP.getEip() #当前带宽，通过类的方法

	print utilization,curBandwidth

	try:
		#当带宽利用率超过70%，并且当前带宽还未到目标带宽，则直接增加到目标带宽。
		if utilization >= 0.7 and curBandwidth != highBandwidth :
			AutoEIP.addBandwidth()
		#当前带宽利用率低于10%，并且当前带宽还未到目的地位带宽，则直接减少到目标低位带宽。
		elif utilization <= 0.1 and curBandwidth != lowBandwidth :
			AutoEIP.reduceBandwidth()
		else:
			print "This the max bandwidth or the min bandwidth ,please ajust"	
	except Exception,e:
		print Exception,":",e
		