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



class Model1(torch.nn.Module):

    def __init__(self):
        super(Model1, self).__init__()
        self.fc1 = torch.nn.Linear(2, 10)

    def forward(self, x, y, z):
        x = self.fc1(x)
        y1 = (x + y)
        z1 = (x + z)
        return (y1, z1)




class Model2(torch.nn.Module):

    def __init__(self, m, n):
        super(Model2, self).__init__()
        self.model = m
        self.fc1 = torch.nn.Linear(n, 10)

    def forward(self, x):
        y = torch.randn(3, 2)
        z = torch.randn(3, 4)
        return self.model(x, y, z)




m = Model1()

n = 1
func = Model2(m, 10).to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___model_fc1(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 40, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''