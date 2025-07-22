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
        self.conv1 = torch.nn.Conv2d(3, 16, 1)
        self.conv2 = torch.nn.Conv2d(16, 8, 1)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = torch.sigmoid(t1)
        t3 = self.conv1(t2)
        t4 = torch.sigmoid(t2)
        t5 = self.conv2(t4)
        t6 = torch.sigmoid(t5)
        t7 = self.conv2(t6)
        t8 = torch.sigmoid(t7)
        t9 = self.conv2(t8)
        t10 = torch.sigmoid(t9)
        t11 = self.conv2(t10)
        t12 = torch.sigmoid(t11)
        t13 = self.conv2(t12)
        t14 = torch.sigmoid(t13)
        t15 = self.conv2(t14)
        t16 = torch.sigmoid(t15)
        t17 = self.conv2(t16)
        t18 = torch.sigmoid(t17)
        t19 = self.conv2(t18)
        t20 = torch.sigmoid(t19)
        t21 = self.conv2(t20)
        t22 = torch.sigmoid(t21)
        t23 = self.conv2(t22)
        t24 = torch.sigmoid(t23)
        t25 = self.conv1(t24)
        t26 = torch.sigmoid(t25)
        return t26



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 16, 64, 64] to have 3 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79684af96ec0>(*(FakeTensor(..., size=(1, 16, 64, 64)), Parameter(FakeTensor(..., size=(16, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 16, 64, 64] to have 3 channels, but got 16 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''