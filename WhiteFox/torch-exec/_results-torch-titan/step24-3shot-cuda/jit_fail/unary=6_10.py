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
        self.max = torch.nn.MaxPool2d(3, stride=1, padding=2)

    def forward(self, x1):
        v1 = (self.max(x1) + 3)
        v2 = torch.clamp(v1, min=0, max=6)
        v3 = torch.mul(v2, 4.0)
        v4 = (v3 / 5)
        return v4




func = Model().to('cuda')



x1 = torch.randn(6, 3, 14, 14)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=2 and kernel_size=3

jit:
Failed running call_module L__self___max(*(FakeTensor(..., device='cuda:0', size=(6, 3, 14, 14)),), **{}):
pad should be at most half of kernel size, but got pad=2 and kernel_size=3

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''