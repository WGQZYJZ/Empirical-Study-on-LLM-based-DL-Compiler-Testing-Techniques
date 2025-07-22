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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.module1 = torch.nn.Sequential(*(torch.nn.Conv2d(in_channels=i, out_channels=i, kernel_size=3, stride=1, padding=1) for i in range(0, 8)))

    def forward(self, x):
        v1 = self.module1(x)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x = torch.randn(1, 64, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, expected weight to be at least 1 at dimension 0, but got weight of size [0, 0, 3, 3] instead

jit:
Failed running call_module L__self___module1_0(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)),), **{}):
Given groups=1, expected weight to be at least 1 at dimension 0, but got weight of size [0, 0, 3, 3] instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''