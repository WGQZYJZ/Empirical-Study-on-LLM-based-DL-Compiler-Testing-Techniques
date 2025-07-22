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



class m1(torch.nn.Module):

    def __init__(self, m2, v):
        super().__init__()
        self.m2 = m2
        self.v = v

    def forward(self, x1):
        x2 = self.m2(x1)
        x3 = torch.randint(0, 9, (1,))
        x4 = (x2 ** self.v)
        return x4




class m2(torch.nn.Module):

    def __init__(self, p1):
        super().__init__()
        self.p1 = p1

    def forward(self, x1):
        x2 = self.p1
        x3 = torch.randint(1, 9, (1,))
        x4 = (x1 ** x3)
        return x4




p1 = 1


func = m2(p1).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function pow>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(1,), dtype=torch.int64)), **{}):
Unhandled FakeTensor Device Propagation for aten.pow.Tensor_Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 40, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''