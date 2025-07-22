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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v2 = torch.randn(x1.shape[0], 1)
        v3 = self.linear(x1)
        v4 = torch.cat([v2, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x7cf3f72699e0>(*([FakeTensor(..., size=(1, 1)), FakeTensor(..., device='cuda:0', size=(1, 8))],), **{'dim': 1}):
Unhandled FakeTensor Device Propagation for aten.cat.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''