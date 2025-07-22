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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * torch.clamp(torch.min(v1, torch.from_numpy(np.array([6.0]))), max=6))
        v3 = (v2 / 6)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in method min of type object at 0x7b3ce78699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5)), FakeTensor(..., size=(1,), dtype=torch.float64)), **{}):
Unhandled FakeTensor Device Propagation for aten.minimum.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''