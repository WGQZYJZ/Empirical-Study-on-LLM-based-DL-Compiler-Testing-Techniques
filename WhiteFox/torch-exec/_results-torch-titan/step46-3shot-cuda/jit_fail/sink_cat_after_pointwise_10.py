import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        y1 = torch.cat((x, x), dim=1)
        y2 = y1.view(y1.shape[0], (- 1))
        if (y2.shape != (1, 6)):
            y3 = y2.tanh()
            y4 = torch.cat((y3, y3, y3), dim=1)
            y5 = y4.view(y4.shape[0], (- 1))
        else:
            y6 = torch.tanh(y2)
            y7 = y6.cos()
            y8 = torch.matmul(y7, y6)
            y9 = y8.relu()
            y10 = torch.tanh(y9)
            y11 = y10.cos()
            y12 = torch.matmul(y11, y10)
            y13 = y12.relu()
            y14 = torch.tanh(y13)
            y15 = y14.cos()
            y16 = torch.matmul(y15, y14)
            y17 = y16.relu()
            y18 = torch.tanh(y17)
            y19 = y18.cos()
            y20 = torch.matmul(y19, y18)
            y21 = y20.view(y20.shape[0], (- 1))
            if (y21.shape != (1, 6)):
                y22 = torch.tanh(y21)
                y23 = y22.cos()
                y24 = torch.matmul(y23, y22)
                y25 = y24.relu()
                y26 = torch.tanh(y25)
                y27 = y26.cos()
                y28 = torch.matmul(y27, y26)
                y29 = y28.relu()
                y30 = torch.tanh(y29)
                y31 = y30.cos()
                y32 = torch.matmul(y31, y30)
                y33 = y32.relu()
                y34 = torch.tanh(y33)
                y35 = y34.cos()
                y36 = torch.matmul(y35, y34)
                y37 = y36.relu()
                y38 = torch.tanh(y37)
                y39 = y38.cos()
                y40 = torch.matmul(y39, y38)
                y41 = torch.tanh(y40)
                y42 = y41.cos()
                y43 = torch.matmul(y42, y41)
                y44 = y43.relu()
                y45 = torch.tanh(y44)
                y46 = y45.cos()
                y47 = torch.matmul(y46, y45)
                y48 = y47.relu()
                y49 = torch.tanh(y48)
                y50 = y49.cos()
                y51 = torch.matmul(y50, y49)
                y52 = y51.relu()
            else:
                x_1 = torch.clone(y21)
                x_2 = torch.clone(y21)
                x_3 = torch.clone(y21)
                x_4 = torch.clone(y21)
                x_5 = torch.clone(y21)
                x_6 = torch.clone(y21)
                x_7 = torch.clone(y21)
                x_8 = torch.clone(y21)
                x_9 = torch.clone(y21)
                x_10 = torch.clone(y21)
                x_11 = torch.clone(y21)
                y53 = (torch.cat((x_1, x_2), dim=0) if (x_1.shape != (2, 3)) else x_1)
                y54 = (torch.cat((y53, x_3), dim=0) if (y53.shape != (3, 3)) else y53)
                y55 = (torch.cat((y54, x_4), dim=1) if (y54.shape != (3, 6)) else y54)
                x_12 = torch.clone(y55)
                y56 = (torch.cat((x_5, x_6), dim=1) if (x_5.shape != (1, 6)) else x_5)
                x_13 = torch.clone(y56)
                y57 = (torch.cat((x_7, x_8), dim=1) if (x_7.shape != (1, 6)) else x_7)
                x_14 = torch.clone(y57)
                y58 = (torch.cat((x_9, x_10), dim=0) if (x_9.shape != (2, 3)) else x_9)
                y59 = (torch.cat((y58, x_11), dim=0) if (y58.shape != (3, 3)) else y58)
                y60 = (torch.cat((y59, x_12), dim=1) if (y59.shape != (3, 6)) else y59)
                y61 = (torch.cat((y60, x_13), dim=1) if (y60.shape != (3, 12)) else y60)
                y62 = (torch.cat((y61, x_14), dim=1) if (y61.shape != (3, 18)) else y61)
                y63 = y62.view(y62.shape[0], (- 1))
                if (y63.shape != (1, 18)):
                    y64 = y63.tanh()
                    y65 = y64.cos()
                    y66 = torch.matmul(y65, y64)
                    y67 = y66.relu()
                    x_15 = torch.clone(y67)
                    y68 = torch.tanh(x_15)
                    y69 = y68.cos()
                    y70 = torch.matmul(y69, y68)
                    y71 = y70.relu()
                    x_16 = torch.clone(y71)
                    y72 = torch.tanh(x_16)
                    y73 = y72.cos()
                    y74 = torch.matmul(y73, y72)
                    y75 = y74.relu()
                    x_17 = torch.clone(y75)
                    y76 = torch.tanh(x_17)
                    y77 = y76.cos()
                    y78 = torch.matmul(y77, y76)
                    y79 = y78.relu()
                    y80 = torch.tanh(y79)
                    y81 = y80.cos()
                    y82 = torch.matmul(y81, y80)
                    y83 = y82.relu()
                    y84 = torch.tanh(y83)
                    y85 = y84.cos()
                    y86 = torch.matmul(y85, y84)
                    y87 = y86.relu()
                    y88 = torch.tanh(y87)
                    y89 = y88.cos()
                    y90 = torch.matmul(y89, y88)
                    y91 = y90.relu()
                    y92 = torch.tanh(y91)
                    y93 = y92.cos()
                    y94 = torch.matmul(y93, y92)
                    y95 = y94.relu()
                    y96 = torch.tanh(y95)
                    y97 = y96.cos()
                    y98 = torch.matmul(y97, y96)
                    y99 = y98.relu()
                    y100 = torch.tanh(y99)
                    y101 = y100.cos()
                    y102 = torch.matmul(y101, y100)
                    y103 = y102.relu()
                    y104 = torch.tanh(y103)
                    y105 = y104.cos()
                    y106 = torch.matmul(y105, y104)
                    y107 = y106.relu()
                    y108 = torch.tanh(y107)
                    y109 = y108.cos()
                    y110 = torch.matmul(y109, y108)
                    y111 = y110.relu()
                    y112 = torch.tanh(y111)
                    y113 = y112.cos()
                    y114 = torch.matmul(y113, y112)
                    y115 = y114.relu()
                    y116 = torch.tanh(y115)
                    y117 = y116.cos()
                    y118 = torch.matmul(y117, y116)
                    y119 = y118.relu()
                    y120 = torch.tanh(y119)
                    y121 = y120.cos()
                    y122 = torch.matmul(y121, y120)
                    y123 = y122.relu()
                    y124 = torch.tanh(y123)
                    y125 = y124.cos()
                    y126 = torch.matmul(y125, y124)
                    y127 = y126.relu()
                    y128 = torch.tanh(y127)
                    y129 = y128.cos()
                    y130 = torch.matmul(y129, y128)
                    y131 = y130.tanh()
                    y132 = torch.matmul(y131, y128)
                    y133 = y132.relu()
                    y134 = torch.tanh(y133)
                    y135 = y134.cos()
                    y136 = torch.matmul(y135, y134)
                    y137 = y136.relu()
                    y138 = torch.tanh(y137)
                    y139 = y138.cos()
                    y140 = torch.matmul(y139, y138)
                    y141 = y140.relu()
                    y142 = torch.tanh(y141)
                    y143 = y142.cos()
                    y144 = torch.matmul(y143, y142)
                    y145 = y144.relu()
                    y146 = torch.tanh(y145)
                    y147 = y146.cos()
                    y148 = torch.matmul(y147, y146)
                    y149 = y148.relu()
                else:
                    x_18 = torch.clone(y63)
                    x_19 = torch.clone(y63)
                    x_20 = torch.clone(y63)
                    x_21 = torch.clone(y63)
                    x_22 = torch.clone(y63)
                    x_23 = torch.clone(y63)
                    x_24 = torch.clone(y63)
                    x_25 = torch.clone(y63)
                    x_26 = torch.clone(y63)
                    x_27 = torch.clone(y63)
                    x_28 = torch.clone(y63)
                    x_29 = torch.clone(y63)
                    x_30 = torch.clone(y63)
                    x_31 = torch.clone(y63)
                    x_32 = torch.clone(y63)
                    x_33 = torch.clone(y63)
                    x_34 = torch.clone(y63)
                    x_35 = torch.clone(y63)
                    x_36 = torch.clone(y63)
                    x_37 = torch.clone(y63)
                    x_38 = torch.clone(y63)
                    x_39 = torch.clone(y63)
                    x_40 = torch.clone(y63)
                    x_41 = torch.clone(y63)
                    x_42 = torch.clone(y63)
                    x_43 = torch.clone(y63)
                    x_44 = torch.clone(y63)
                    x_45 = torch.clone(y63)
                    xx_0 = (torch.cat((x_18, x_19), dim=0) if (x_18.shape != (2, 3)) else x_18)
                    xx_1 = (torch.cat((xx_0, x_20), dim=0) if (xx_0.shape != (3, 3)) else xx_0)
                    xx_2 = (torch.cat((xx_1, x_21), dim=1) if (xx_1.shape != (3, 6)) else xx_1)
                    x_46 = xx_2
                    xx_3 = (torch.cat((x_22, x_23), dim=1) if (x_22.shape != (1, 6)) else x_22)
                    x_47 = xx_3
                    xx_4 = (torch.cat((x_24, x_25), dim=1) if (x_24.shape != (1, 6)) else x_24)
                    x_48 = xx_4
                    xx_5 = (torch.cat((x_26, x_27), dim=0) if (x_26.shape != (2, 3)) else x_26)
                    xx_6 = (torch.cat((xx_5, x_28), dim=0) if (xx_5.shape != (3, 3)) else xx_5)
                    xx_7 = (torch.cat((xx_6, x_29), dim=1) if (xx_6.shape != (3, 6)) else xx_6)
                    xx_8 = (torch.cat((xx_7, x_30), dim=0) if (xx_7.shape != (3, 9)) else xx_7)
                    xx_9 = (torch.cat((xx_8, x_31), dim=1) if (xx_8.shape != (3, 15)) else xx_8)
                    xx_10 = (torch.cat((xx_9, x_32), dim=1) if (xx_9.shape != (3, 21)) else xx_9)
                    xx_11 = (torch.cat((xx_10, x_33), dim=0) if (xx_10.shape != (3, 24)) else xx_10)
                    xx_12 = (torch.cat((xx_11, x_34), dim=1) if (xx_11.shape != (3, 27)) else xx_11)
                    x_49 = xx_12
                    xx_13 = (torch.cat((x_35, x_36), dim=1) if (x_35.shape != (1, 6)) else x_35)




func = Model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7c9ed40699e0>(*((1, 1),), **{'dim': 1}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''