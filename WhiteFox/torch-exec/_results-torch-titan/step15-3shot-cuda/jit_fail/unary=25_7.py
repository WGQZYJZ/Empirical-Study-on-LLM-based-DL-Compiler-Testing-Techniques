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



class LeakyRelu(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.lr0 = 0.2

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, torch.ones(1, 96, requires_grad=False))
        v2 = (v1 > 0)
        v3 = (v1 * self.lr0)
        return torch.where(v2, v1, v3)



func = LeakyRelu().to('cuda')



x = torch.randn(1, 96, requires_grad=True)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 96)), FakeTensor(..., size=(1, 96))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''