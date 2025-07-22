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

    def __init__(self, min_value=(- 6.2), max_value=(- 5.5)):
        super().__init__()
        self.max_pool = torch.nn.MaxPool2d(2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.max_pool(x1)
        v1.retain_grad()
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
can't retain_grad on Tensor that has requires_grad=False

jit:
Failed running call_method retain_grad(*(FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32)),), **{}):
can't retain_grad on Tensor that has requires_grad=False

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''