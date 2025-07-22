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

    def __init__(self, in_features=20, n_class=10, min=0, max=0):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_features, n_class)
        self.m = torch.nn.ReLU6()
        self.fc2 = torch.nn.Linear(n_class, n_class, bias=True)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = self.m(v1)
        v3 = self.fc2(v2)
        v4 = torch.clamp_min(v3, self.min)
        v5 = torch.clamp_max(v4, self.max)
        return v5




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___fc1(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''