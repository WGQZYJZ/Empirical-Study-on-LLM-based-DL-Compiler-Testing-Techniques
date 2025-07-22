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
        x3 = torch.addmm(torch.randn(1), x2, torch.mm(x2, x2))
        x4 = torch.nn.functional.dropout(x3)
        return x4




class m2(torch.nn.Module):

    def __init__(self, p1):
        super().__init__()
        self.p1 = p1

    def forward(self, x1):
        x2 = torch.rand_like(x1)
        x3 = (x2 - x1)
        x4 = (torch.randn(1) - x3)
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
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1,)), FakeTensor(..., device='cuda:0', size=(1, 2, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.sub.Tensor, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''