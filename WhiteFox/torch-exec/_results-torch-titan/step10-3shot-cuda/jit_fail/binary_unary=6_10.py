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
        self.linear = torch.nn.Linear(16, 8, bias=True)

    def forward(self, x2):
        v1 = self.linear(x2)
        other = torch.tensor([(- 0.2)], dtype=torch.float32)
        v2 = (v1 - other)
        v3 = torch.sqrt(v2)
        v4 = torch.relu(v3)
        return v4



func = Model().to('cuda')



x2 = torch.randn(1, 16)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 8)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.sub.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''