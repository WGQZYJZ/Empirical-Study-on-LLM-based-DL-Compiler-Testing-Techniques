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

    def __init__(self, min_value=1.165433630886078, max_value=9.495014390253015):
        super().__init__()
        self.linear = torch.nn.Linear(12, 8)
        self.max_value = max_value
        self.min_value = min_value
        self.relu = torch.nn.ReLU()
        self.t = torch.nn.Conv3d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.relu(v1)
        v3 = self.t(v2)
        v4 = torch.clamp(v3, self.min_value, self.max_value)
        v5 = self.relu(v1)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 12)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 8]

jit:
Failed running call_module L__self___t(*(FakeTensor(..., device='cuda:0', size=(1, 8)),), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 8]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''