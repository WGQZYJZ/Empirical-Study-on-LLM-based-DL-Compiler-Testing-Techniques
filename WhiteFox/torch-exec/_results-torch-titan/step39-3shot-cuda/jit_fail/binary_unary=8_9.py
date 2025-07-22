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
        self.conv = torch.nn.Conv2d(3, 3, 2, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.max_pool2d(v1, (3, 3), stride=2, padding=1)
        v3 = torch.max_pool2d(v1, 2, stride=1)
        v4 = torch.max_pool2d(v1, 3, stride=1, padding=0)
        v5 = torch.max_pool2d(v1, 2)
        v6 = torch.max_pool2d(v1)
        v7 = torch.max_pool2d(v1)
        v8 = (((((v2 + v3) + v4) + v5) + v6) + v7)
        v9 = torch.relu(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
max_pool2d() missing 1 required positional arguments: "kernel_size"

jit:
Failed running call_function <built-in method max_pool2d of type object at 0x7f4b9e2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 63, 63)),), **{}):
max_pool2d() missing 1 required positional arguments: "kernel_size"

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''