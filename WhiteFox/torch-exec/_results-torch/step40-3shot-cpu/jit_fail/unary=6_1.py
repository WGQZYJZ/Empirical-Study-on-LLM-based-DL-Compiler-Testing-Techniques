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
        self.conv = torch.nn.Conv2d(46, 16, 1, stride=1, padding=0)
        self.dropout = torch.nn.Dropout2d(p=0.75)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.dropout(t1)
        t3 = self.conv(t2)
        t4 = torch.cat([t2, t3], 1)
        t5 = self.conv(t4)
        t6 = torch.randn(1, 3, 224, 224)
        t7 = torch.cat([t5, t6], 1)
        t8 = self.conv(t7)
        t9 = torch.randn(1, 3, 224, 224)
        t10 = torch.cat([t8, t9], 1)
        t11 = self.conv(t10)
        t12 = torch.randn(1, 17, 224, 224)
        t13 = torch.cat([t11, t12], 1)
        t14 = self.conv(t13)
        t15 = self.conv(t14)
        t16 = self.conv(t15)
        t17 = torch.randn(1, 26, 224, 224)
        t18 = torch.cat([t16, t17], 1)
        return self.conv(t18)



func = Model().to('cpu')


x1 = torch.randn(1, 46, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 46, 1, 1], expected input[1, 16, 224, 224] to have 46 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x73d1f5396ec0>(*(FakeTensor(..., size=(1, 16, 224, 224)), Parameter(FakeTensor(..., size=(16, 46, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 46, 1, 1], expected input[1, 16, 224, 224] to have 46 channels, but got 16 channels instead

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