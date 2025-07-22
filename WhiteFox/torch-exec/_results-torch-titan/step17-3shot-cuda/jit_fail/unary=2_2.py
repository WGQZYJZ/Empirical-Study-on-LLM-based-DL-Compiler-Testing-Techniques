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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        v10 = torch.zeros(v9.shape, dtype=torch.bool)
        v11 = torch.logical_and(v10, v9)
        v12 = v11.float()
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 1, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in method logical_and of type object at 0x7661d92699e0>(*(FakeTensor(..., size=(1, 3, 3, 3), dtype=torch.bool), FakeTensor(..., device='cuda:0', size=(1, 3, 3, 3))), **{}):
Unhandled FakeTensor Device Propagation for aten.logical_and.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''