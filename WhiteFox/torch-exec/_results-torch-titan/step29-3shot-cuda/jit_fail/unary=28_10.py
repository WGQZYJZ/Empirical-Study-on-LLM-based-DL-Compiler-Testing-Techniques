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

    def __init__(self, min_value, max_value):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, torch.rand([1, 1024], dtype=torch.float32), torch.rand([1024], dtype=torch.float32))
        v2 = torch.nn.functional.clamp(v1, min=self.min_value, max=self.max_value)
        v3 = torch.nn.functional.relu(v2)
        return v3



min_value = 1
max_value = 1
func = Model((- 0.5), 1).to('cuda')




x1 = torch.randn(1, 1024, dtype=torch.float32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 1024)), FakeTensor(..., size=(1, 1024)), FakeTensor(..., size=(1024,))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''