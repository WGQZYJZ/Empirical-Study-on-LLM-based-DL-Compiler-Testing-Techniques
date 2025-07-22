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
        self.m1 = m1()

    def forward(self, x1):
        x2 = self.m1(x1)
        return torch.relu(x2)




func = Model().to('cuda')



x1 = torch.tensor([[[[0.0, 1.0, 2.0], [(- 29.0), (- 2.0), (- 1.0)]], [[3.0, 4.0, 5.0], [6.0, 7.0, 8.0]], [[9.0, 10.0, 11.0], [12.0, 13.0, 14.0]]]])


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1,)), FakeTensor(..., device='cuda:0', size=(1, 3, 2, 3))), **{}):
Unhandled FakeTensor Device Propagation for aten.mul.Tensor, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''