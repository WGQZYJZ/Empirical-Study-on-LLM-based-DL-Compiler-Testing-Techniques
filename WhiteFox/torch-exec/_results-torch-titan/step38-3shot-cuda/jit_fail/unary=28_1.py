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

    def __init__(self, min_value=(- 3.0), max_value=10.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        self.linear.bias -= torch.nn.Parameter(torch.tensor([1.0]), requires_grad=False)
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



func = Model(min_value=(- 0.5), max_value=10.0).to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function isub>(*(Parameter(FakeTensor(..., device='cuda:0', size=(10,), requires_grad=True)), Parameter(FakeTensor(..., size=(1,)))), **{}):
Unhandled FakeTensor Device Propagation for aten.sub_.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 24, in <resume in forward>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''