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

    def __init__(self, negative_slope=0):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = x1.flatten(start_dim=1)
        v2 = torch.nn.functional.linear(v1, torch.tensor([[1.78790387, (- 0.01625918), 0.01750951, 1.26051818, (- 0.49119654), (- 0.50248609), (- 0.50834412), (- 0.00280192)]]))
        v3 = (v2 > 0)
        v4 = (v2 * self.negative_slope)
        v5 = torch.where((v3 > 0), v2, v4)
        v6 = torch.reshape(v5, (2, 8))
        return v6



func = Model().to('cuda')



x1 = torch.randn(2, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(2, 8)), FakeTensor(..., size=(1, 8))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''