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



class Module1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.v1 = torch.nn.Linear(1024, 2)

    def forward(self, t):
        v1 = self.v1(t)
        return v1




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.m1 = Module1()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = torch.nn.functional.adaptive_avg_pool2d(x2, [1, 1])
        v1 = v1.reshape(v1.size(0), (- 1))
        v2 = self.m1(v1)
        v3 = torch.cat([v2.unsqueeze(1), x1], dim=1)
        v4 = v3[:, 0, :]
        v5 = self.conv(v4.unsqueeze(1))
        v6 = (v3 * 0.9793241061191791)
        v7 = (v5 * v6)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 128, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3 and 1024x2)

jit:
Failed running call_module L__self___m1_v1(*(FakeTensor(..., device='cuda:0', size=(1, 3)),), **{}):
a and b must have same reduction dim, but got [1, 3] X [1024, 2].

from user code:
   File "<string>", line 38, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''