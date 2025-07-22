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
        self.conv = torch.nn.Conv2d(256, 64, 1, stride=1, padding=0)

    def forward(self, x):
        negative_slope = 1.011716
        v1 = self.conv(x)
        v7 = self.conv(x)
        v8 = torch.sub(1, v7)
        v2 = (v1.type(torch.LongTensor) > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        v5 = (v4 > v8)
        v9 = (v4 * v8)
        v6 = torch.where(v5, v4, v9)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 256, 7, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in method where of type object at 0x784c1da699e0>(*(FakeTensor(..., size=(1, 64, 7, 7), dtype=torch.bool), FakeTensor(..., device='cuda:0', size=(1, 64, 7, 7)), FakeTensor(..., device='cuda:0', size=(1, 64, 7, 7))), **{}):
Unhandled FakeTensor Device Propagation for aten.where.self, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''