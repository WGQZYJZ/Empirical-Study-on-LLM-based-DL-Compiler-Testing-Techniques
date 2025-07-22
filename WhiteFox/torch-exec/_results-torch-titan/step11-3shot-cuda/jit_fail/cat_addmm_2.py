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



class ConvLayer(nn.Module):

    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.linear = torch.nn.Linear((in_channels * 2), in_channels)
        self.pool = torch.nn.AdaptiveAvgPool2d((1, 1))

    def forward(self, x1):
        v1 = F.relu(self.linear(x1))
        v2 = self.pool(v1)
        return v2




class Model(nn.Module):

    def __init__(self, block=ConvLayer):
        super(Model, self).__init__()
        self.block = block
        self.conv1 = block(75, 30)
        self.conv2 = block(30, 40)
        self.conv3 = block(40, 50)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        return torch.cat([v1, v2, v3])



func = Model().to('cuda')



x = torch.randn(64, 75)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x75 and 150x75)

jit:
Failed running call_module L__self___conv1_linear(*(FakeTensor(..., device='cuda:0', size=(64, 75)),), **{}):
a and b must have same reduction dim, but got [64, 75] X [150, 75].

from user code:
   File "<string>", line 40, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''