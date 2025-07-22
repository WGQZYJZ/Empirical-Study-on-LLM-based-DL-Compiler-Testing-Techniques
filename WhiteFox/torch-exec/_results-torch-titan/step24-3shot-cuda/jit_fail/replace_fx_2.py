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

    def __init__(self, m2):
        super().__init__()
        self.m2 = m2

    def forward(self, x1):
        x2 = self.m2(x1)
        x3 = torch.rand(1, dtype=torch.float32)
        x4 = (x3 ** x3)
        return x4




class m2(torch.nn.Module):

    def __init__(self, p1):
        super().__init__()

    def forward(self, x1):
        z = 2
        x2 = (z * torch.nn.functional.dropout(x1, p=0.1))
        x3 = torch.randn(1)
        x4 = (x2 + x3)
        x5 = (x4 ** x3)
        return x5



p1 = 1

func = m2(p1).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''