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
        self.conv = torch.nn.Conv2d(3, 19, 1, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None, padding2=None, padding3=None, other2=None):
        v1 = self.conv(x1)
        if (padding1 == None):
            padding1 = torch.randn(v1.shape)
        if (padding2 == None):
            padding2 = torch.randn(v1.shape)
        if (padding3 == None):
            padding3 = torch.randn(v1.shape)
        if (other2 == None):
            other2 = torch.randn(v1.shape)
        v2 = (v1 + other)
        v3 = torch.cat([padding2, v2])
        v4 = torch.cat([padding1, v3])
        v5 = torch.cat([v3, v4])
        v6 = torch.cat([other2, v3])
        return (v6, v5)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x7adfcd6699e0>(*([FakeTensor(..., size=(1, 19, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 19, 66, 66))],), **{}):
Unhandled FakeTensor Device Propagation for aten.cat.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''