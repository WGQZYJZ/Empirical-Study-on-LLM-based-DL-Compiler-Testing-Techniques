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
        x2 = (x1 ** 2)
        x3 = torch.randint(0, 9, (1,))
        with torch.no_grad():
            x4 = torch.rand_like(x3)
        x5 = self.m2(x4)
        return x5




class m2(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = (x1 + torch.randint(0, 9, (1,)))
        x3 = torch.rand_like(x1)
        x4 = torch.nn.functional.dropout((x2 + x3))
        return x4




func = m2().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(1,), dtype=torch.int64)), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''