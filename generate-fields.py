# -*- coding: utf-8 -*-

# 用类似下面的文本来生成一个类的fields.

# account_id	str	账号ID
# account_name	str	账户登录名
# symbol	str	标的代码
# side	int	持仓方向 取值参考 PositionSide
# volume	long	总持仓量; 如果要得到昨持仓量，公式为 (volume - volume_today)
# volume_today	long	今日持仓量
# vwap	float	持仓均价 new_vwap=((position.vwap * position.volume)+(trade.volume*trade.price))/(position.volume+trade.volume)
# amount	float	持仓额 (volume*vwap*multiplier)
# price	float	当前行情价格（回测时值为0）
# fpnl	float	持仓浮动盈亏 ((price - vwap) * volume * multiplier) （基于效率的考虑，回测模式fpnl只有仓位变化时或者一天更新一次,仿真模式3s更新一次）
# cost	float	持仓成本 (vwap * volume * multiplier * margin_ratio)
# order_frozen	int	挂单冻结仓位
# order_frozen_today	int	挂单冻结今仓仓位
# available	long	可平总仓位 ，公式为(volume - order_frozen); 如果要得到可平昨仓位，公式为 (available - available_today)
# available_today	long	可平今仓位，公式为 (volume_today - order_frozen_today)(仅期货)
# last_price	float	上一次成交价（回测时值为0）
# last_volume	long	上一次成交量（回测时值为0）
# last_inout	int	上一次出入持仓量（回测时值为0）
# change_reason	int	仓位变更原因, 取值参考 CashPositionChangeReason
# change_event_id	str	触发资金变更事件的ID
# created_at	datetime.datetime	建仓时间
# updated_at	datetime.datetime	仓位变更时间

import sys

data = sys.stdin.readlines()
output = ""
for line in data:
    parts = line.split()
    print(parts)
    if parts[1] == 'float':
        field = "self.%s = %s\n" % (parts[0], 0.0)
    elif parts[1] == 'long':
        field = "self.%s = %s\n" % (parts[0], 0)
    elif parts[1] == 'int':
        field = "self.%s = %s\n" % (parts[0], 0)
    elif parts[1] == 'datetime.datetime':
        field = "self.%s = None\n" % (parts[0], )
    else:
        field = "self.%s = ''\n" % (parts[0], )

    output = output + field

print(output)
