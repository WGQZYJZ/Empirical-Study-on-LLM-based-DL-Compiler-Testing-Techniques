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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, input):
        x = self.linear(input)
        y = torch.randint(low=2, high=6, size=(2, 2))
        res1 = torch.mul(x, y)
        z = torch.rand_like(x)
        res2 = torch.sum(x, dim=1, keepdim=True)
        res3 = torch.add(res2, z)
        return x




func = model().to('cuda')



input = torch.randn(1, 2, 2)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in method mul of type object at 0x7d448f8699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(2, 2), dtype=torch.int64)), **{}):
Unhandled FakeTensor Device Propagation for aten.mul.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''