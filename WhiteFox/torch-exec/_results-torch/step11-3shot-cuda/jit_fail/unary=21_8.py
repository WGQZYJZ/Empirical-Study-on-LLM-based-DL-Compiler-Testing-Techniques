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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.module1 = torch.nn.Sequential(*(torch.nn.Conv2d(in_channels=i, out_channels=i, kernel_size=3, stride=1, padding=1) for i in range(0, 8)))

    def forward(self, x):
        v1 = self.module1(x)
        v2 = torch.tanh(v1)
        return v2



func = ModelTanh().to('cuda')


x = torch.randn(1, 64, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, expected weight to be at least 1 at dimension 0, but got weight of size [0, 0, 3, 3] instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x749c5db96ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(0, 0, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(0,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, expected weight to be at least 1 at dimension 0, but got weight of size [0, 0, 3, 3] instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''