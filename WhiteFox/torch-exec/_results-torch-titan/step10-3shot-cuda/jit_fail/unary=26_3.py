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



class CustomModule(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x2 = self.conv_transpose(x)
        x3 = (x2 > 0)
        x4 = (x2 * self.negative_slope)
        x5 = torch.where(x3, x2, x4)
        return x5




class Model(torch.nn.Module):

    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
        self.custom_module = CustomModule()

    def forward(self, x1):
        x2 = (x1 + torch.ones_like(x1))
        x3 = self.conv_transpose(x2)
        x4 = self.custom_module(x3)
        return x4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'CustomModule' object has no attribute 'conv_transpose'

jit:
conv_transpose

from user code:
   File "<string>", line 41, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''