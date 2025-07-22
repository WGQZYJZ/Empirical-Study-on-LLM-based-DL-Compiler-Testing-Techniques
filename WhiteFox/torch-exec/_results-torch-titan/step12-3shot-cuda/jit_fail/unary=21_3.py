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



class conv2d_tanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 1, (1,), (1,), 0)

    def forward(self, x):
        tanh = torch.tanh(self.conv(x))
        return tanh




class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.m1 = conv2d_tanh()

    def forward(self, x):
        v1 = self.m1(x)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



tensor = torch.randn((1, 3, 128, 128))


test_inputs = [tensor]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 1 values to match the convolution dimensions, but got padding=[0, 0]

jit:
Failed running call_module L__self___m1_conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 128, 128)),), **{}):
tuple index out of range

from user code:
   File "<string>", line 35, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''