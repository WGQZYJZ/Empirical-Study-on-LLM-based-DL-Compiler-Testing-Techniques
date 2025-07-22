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

    def forward(self, x1):
        v4 = x1
        v1 = torch.nn.functional.linear(v4, torch.randn(2, 2), torch.randn(2))
        a1 = v1.numpy()
        v2 = a1.permute((0, 2, 1))
        a2 = torch.from_numpy(v2).float()
        return a2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(2,))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''