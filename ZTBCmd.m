//
//  ZTBCmd.c
//  ZTBLEDemo
//
//  Created by Mao on 16/03/2018.
//  Copyright © 2018 mao. All rights reserved.
//

#import "ZTBCmd.h"


/*获取电量*/
const UInt8 ZTBCmdGetPower = 0x20;

/*获取版本号*/
const UInt8 ZTBCmdGetVersion = 0x21;

/*设定时间*/
const UInt8 ZTBCmdSetTime = 0x22;

/*发送单色数片*/
const UInt8 ZTBCmdSendPic  = 0x23;

/*获取步数*/
const UInt8 ZTBCmdGetStep  = 0x24;

/*获取当前心率值*/
const UInt8 ZTBCmdGetHeartbeat  = 0x25;

/*删除所有数据-已废弃*/
const UInt8 ZTBCmdDeleteData  =  0x26;

/*设置用户信息*/
const UInt8 ZTBCmdSetUserInfo  = 0x27;

/*设置网关ID*/
const UInt8 ZTBCmdSetGatewayID  = 0x28;

/*获取 mac 地址*/
const UInt8 ZTBCmdGetMacAddress  = 0x29;

//获取历史数据
const UInt8 ZTBCmdGetHistoryDataCount  = 0x30;

/*获取历史数据*/
const UInt8 ZTBCmdGetHistoryData  = 0x31;

/*删除历史数据*/
const UInt8 ZTBCmdDeleteHistoryData  = 0x32;

/*获取睡眠数据条数*/
const UInt8 ZTBCmdGetSleepDataCount = 0x33;

/*获取睡眠数据*/
const UInt8 ZTBCmdGetSleepData = 0x34;

/*删除睡眠数据*/
const UInt8 ZTBCmdDeleteSleepData  = 0x35;

/*获取训练数据条数*/
const UInt8 ZTBCmdGetTrainDataCount = 0x36;

/*获取训练数据*/
const UInt8 ZTBCmdGetTrainData = 0x37;

/*删除历史数据*/
const UInt8 ZTBCmdDeleteTrainData  = 0x38;

/*获取 MTU 和 协议版本*/
const UInt8 ZTBCmdGetMTU  = 0x2a;

/*写入测试数据*/
const UInt8 ZTBCmdWriteTestData  = 0x2b;

/*写入手环编号*/
const UInt8 ZTBCmdWriteBandId = 0x2d;

/*申请绑定指令*/
const UInt8 ZTBCmdApplyBind = 0x42;

/*绑定指令*/
const UInt8 ZTBCmdBind = 0x43;


/*获取历史步数数据条数*/
const UInt8 ZTBCmdGetStepDataCount = 0x44;

/*获取历史步数数据*/
const UInt8 ZTBCmdGetStepData = 0x45;


/*发送QR*/
const UInt8 ZTBCmdSendQR  = 0x49;
