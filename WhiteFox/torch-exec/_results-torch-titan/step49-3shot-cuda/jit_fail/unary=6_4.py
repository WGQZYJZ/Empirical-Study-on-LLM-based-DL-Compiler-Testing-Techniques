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
        self.avgpool2d = torch.nn.AvgPool2d(kernel_size=3, stride=2, padding=1)
        self.conv2d = torch.nn.Conv2d(6, 128, kernel_size=1, stride=1)
        self.conv2d_1 = torch.nn.Conv2d(128, 16, kernel_size=1, stride=1)
        self.conv2d_2 = torch.nn.Conv2d(128, 3, kernel_size=1, stride=1)

    def forward(self, x1):
        t1 = self.avgpool2d(x1)
        t2 = self.conv2d(t1)
        t3 = self.conv2d_1(t2)
        t4 = self.conv2d_2(t2)
        t5 = self.avgpool2d(t4)
        t6 = self.conv2d_1(t5)
        t7 = self.avgpool2d(t6)
        t8 = torch.conv2d(t7, t3, padding=1)
        t9 = torch.add(t8, 3)
        t10 = torch.relu6(t9)
        t11 = torch.conv2d(t10, t1, padding=1)
        t12 = torch.add(t11, 3)
        t13 = torch.relu6(t12)
        t14 = torch.conv2d(t13, t7, padding=2)
        t15 = torch.add(t14, 3)
        t16 = torch.relu6(t15)
        t17 = torch.conv2d(t16, t7, padding=3)
        t18 = torch.add(t17, 3)
        t19 = torch.relu6(t18)
        t20 = torch.conv2d(t19, t7, padding=4)
        t21 = torch.add(t20, 3)
        t22 = torch.relu6(t21)
        t23 = torch.conv2d(t22, t7, padding=5)
        t24 = torch.add(t23, 3)
        t25 = torch.relu6(t24)
        t26 = torch.conv2d(t25, t7, padding=6)
        t27 = torch.add(t26, 3)
        t28 = torch.relu6(t27)
        t29 = torch.conv2d(t28, t7, padding=7)
        t30 = (t30 / float(t2))
        t30 = torch.add(t30, 3)
        return torch.relu6(t30)




func = Model().to('cuda')



x1 = torch.randn(1, 6, 96, 96)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 128, 1, 1], expected input[1, 3, 24, 24] to have 128 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2d_1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 24, 24)),), **{}):
Given groups=1, weight of size [16, 128, 1, 1], expected input[1, 3, 24, 24] to have 128 channels, but got 3 channels instead

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''