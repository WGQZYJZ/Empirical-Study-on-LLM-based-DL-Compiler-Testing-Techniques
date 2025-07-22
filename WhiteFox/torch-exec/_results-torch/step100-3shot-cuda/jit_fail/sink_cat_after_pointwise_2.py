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

    def forward(self, x):
        y = torch.arange(24).reshape(2, 3, 4)
        if x.shape[0] > y.shape[0]:
            y = torch.stack([y] * x.shape[0])
        z = torch.cat([x, y], dim=1)
        z1 = z.view(z.shape[0], -1)
        z2 = torch.tanh(z1)
        return z2



func = Model().to('cuda')


x = torch.randn(2, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x78a40f396ec0>(*([FakeTensor(..., device='cuda:0', size=(2, 3)), FakeTensor(..., size=(2, 3, 4), dtype=torch.int64)],), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 2-D tensors, but got 3-D for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''