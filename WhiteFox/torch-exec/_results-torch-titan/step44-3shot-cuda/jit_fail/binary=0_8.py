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
        self.conv1 = torch.nn.Conv2d(5, 5, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(5, 5, 3, stride=1, padding=1)

    def forward(self, x1, other=3, padding1=3):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        if (padding1 == 3):
            padding1 = torch.randn(v1.shape)
        v3 = (v1 + other)
        v4 = (torch.cat([v3, padding1]) + v2)
        return v4




func = Model().to('cuda')



x1 = torch.randn(2, 5, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x7f8618c699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 5, 64, 64)), FakeTensor(..., size=(2, 5, 64, 64))],), **{}):
Unhandled FakeTensor Device Propagation for aten.cat.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''