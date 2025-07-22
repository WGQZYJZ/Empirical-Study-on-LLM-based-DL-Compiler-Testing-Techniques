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
        self.fc0 = torch.nn.Linear(10, 10)
        self.fc1 = torch.nn.Linear(10, 10)
        self.fc2 = torch.nn.Linear(10, 10)
        self.fc3 = torch.nn.Linear(10, 10)

    def forward(self, x):
        v1 = self.fc0(torch.randn(10))
        v2 = self.fc1(torch.randn(10))
        v3 = self.fc2(torch.randn(10))
        v4 = self.fc3(torch.randn(10))
        v5 = torch.cat([v1, v2], 0)
        v6 = torch.cat([v3, v4], 0)
        return torch.cat([v5, v6], 1)



func = Model().to('cuda')



x = torch.randn(12, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_module L__self___fc0(*(FakeTensor(..., size=(10,)),), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''