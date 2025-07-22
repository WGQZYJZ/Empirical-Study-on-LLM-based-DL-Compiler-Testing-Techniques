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

    def forward(self, x2):
        v1 = torch.addmm(torch.zeros((*x2.shape[:(- 1)], 2)), x2.view((- 1), 3, 3), x2.view((- 1), 3, 3))
        v3 = torch.clamp(v1, min=(- 1), max=1)
        v4 = v3.view(1, (- 1), 2)
        return torch.cat([v2, v4], 0)



func = Model().to('cuda')



x2 = torch.randn(1, 3, 3, 35)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in method addmm of type object at 0x75cd50c699e0>(*(FakeTensor(..., size=(1, 3, 3, 2)), FakeTensor(..., device='cuda:0', size=(35, 3, 3)), FakeTensor(..., device='cuda:0', size=(35, 3, 3))), **{}):
a must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''