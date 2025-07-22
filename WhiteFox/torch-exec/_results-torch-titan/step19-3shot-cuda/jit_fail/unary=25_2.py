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
        self.linear = torch.nn.Linear(9, 1)

    def forward(self, x1):
        x2 = torch.where((x1 < 0), torch.zeros(1), x1)
        x3 = (x2 * 0.1)
        x4 = self.linear(x3)
        return x4



func = Model().to('cuda')



x1 = torch.randn(1, 9)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in method where of type object at 0x7e57b90699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 9), dtype=torch.bool), FakeTensor(..., size=(1,)), FakeTensor(..., device='cuda:0', size=(1, 9))), **{}):
Unhandled FakeTensor Device Propagation for aten.where.self, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''