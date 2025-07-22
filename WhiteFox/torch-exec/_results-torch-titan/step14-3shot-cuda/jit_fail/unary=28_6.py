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

    def __init__(self, min_value=(- 9.18180582429698e+37), max_value=9.152457547119235e+37):
        super().__init__()
        self.fc = torch.nn.Linear(3, 4)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        return torch.clamp_max(v2, self.max_value)



func = Model(1, 5).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x64 and 3x4)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
a and b must have same reduction dim, but got [192, 64] X [3, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''