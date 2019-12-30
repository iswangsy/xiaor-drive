#coding:utf-8

'''
文 件 名：_XiaoRGEEK_GLOBAL_variable_.py
功    能：全局变量文件，部分参数可根据需求修改

import _XiaoRGEEK_GLOBAL_variable_ as glo
glo.xx
'''
###########################################################
################可手动修改的参数###########################
import sys
import os
if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
Radar_distence	= 15		#超声波测距
servo_angle_max = 160		#舵机角度上限值，防止舵机卡死，可设置小于180的数值
servo_angle_min = 15		#舵机角度下限值，防止舵机卡死，可设置大于0的数值






###########################################################
################禁止手动修改的参数#########################
###########################################################
motor_flag = 1				#电机接线组合标志位，默认为1；上位机调整方向后，会下发实际标志位（1-8）
BT_Client = False
TCP_Client = False
socket_flag = 0

