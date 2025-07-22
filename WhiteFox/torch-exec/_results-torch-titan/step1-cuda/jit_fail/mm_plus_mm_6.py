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



class ReshapeWrapper(torch.nn.Module):

    def __init__(self, reshape_size):
        super().__init__()
        self.reshape_size = reshape_size

    def forward(self, x):
        x = x.reshape(self.reshape_size)
        return x




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.block1 = ReshapeWrapper((56, 16, 768))

    def forward(self, x):
        v1 = self.conv(x)
        v3 = self.block1(v1)
        v5 = torch.sum(v3, (- 1))
        v6 = torch.sum(v5, (- 1))
        return v6



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[56, 16, 768]' is invalid for input of size 32768

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), (56, 16, 768)), **{}):
shape '[56, 16, 768]' is invalid for input of size 32768

from user code:
   File "<string>", line 37, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''