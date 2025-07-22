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
        self.linears = torch.nn.Sequential(torch.nn.Linear(20, 16), torch.nn.BatchNorm1d(16), torch.nn.ReLU(), torch.nn.Linear(16, 10), torch.nn.BatchNorm1d(10), torch.nn.ReLU())

    def forward(self, x1):
        v1 = self.linears(x1)
        v2 = torch.cat((v1, torch.randn(1, 10)), dim=1)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 20)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x706a6ec699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 10)), FakeTensor(..., size=(1, 10))),), **{'dim': 1}):
Unhandled FakeTensor Device Propagation for aten.cat.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''