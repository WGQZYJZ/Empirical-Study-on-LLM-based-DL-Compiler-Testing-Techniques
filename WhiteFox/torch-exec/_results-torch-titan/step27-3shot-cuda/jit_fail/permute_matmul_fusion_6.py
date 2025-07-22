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
        v1 = x2.permute(2, 1, 0)
        x = torch.randn((2, 2))
        v2 = torch.matmul(x, v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)

jit:
Failed running call_function <built-in method matmul of type object at 0x70f72cc699e0>(*(FakeTensor(..., size=(2, 2)), FakeTensor(..., device='cuda:0', size=(2, 2, 1))), **{}):
Unhandled FakeTensor Device Propagation for aten.bmm.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''