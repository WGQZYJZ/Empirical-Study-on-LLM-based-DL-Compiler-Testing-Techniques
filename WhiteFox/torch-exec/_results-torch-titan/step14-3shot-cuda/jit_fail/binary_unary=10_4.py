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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + torch.rand(8))
        v3 = v2.relu()
        return v3




class Module2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.module1 = Module1()

    def forward(self, x1):
        v1 = self.module1(x1)
        v2 = v1.relu()
        v3 = (v1 + v2)
        return v3



func = Module2().to('cuda')



x1 = torch.randn(1, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8)), FakeTensor(..., size=(8,))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 37, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''