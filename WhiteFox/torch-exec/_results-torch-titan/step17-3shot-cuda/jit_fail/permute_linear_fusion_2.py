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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v1)
        v3 = torch.ones(v2)
        x1 = x1.permute(0, 2, 1)
        v1 = x1.permute(0, 2, 1)
        v4 = torch.sqrt(v1)
        v4 = torch.abs(v1)
        v3 = (v3 * v4)
        v3 = (v3 * 5)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
ones(): argument 'size' (position 1) must be tuple of ints, but found element of type Tensor at pos 0

jit:
Failed running call_function <built-in method ones of type object at 0x7cfd594699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)),), **{}):
ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''