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

    def __init__(self, min_value=5.191708258785932, max_value=(- 5.181125051492283)):
        super().__init__()
        self.linear = torch.nn.Linear(64, 8)
        self.hardtanh = torch.nn.Hardtanh(inplace=False)
        self.conv2d = torch.nn.Conv2d(8, 3, 1, stride=2, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.hardtanh(v3)
        v5 = self.conv2d(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 8]

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 8)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 8]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''