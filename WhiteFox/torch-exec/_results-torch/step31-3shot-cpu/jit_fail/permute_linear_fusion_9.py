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
        x2 = torch.nn.functional.relu(v2)
        v3 = x2.detach()
        v4 = torch.max(v3, dim=-1, keepdim=True)[1]
        v4 = v4.expand(1, 1, 2)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (1) must match the existing size (2) at non-singleton dimension 1.  Target sizes: [1, 1, 2].  Tensor sizes: [1, 2, 1]

jit:
Failed running call_method expand(*(FakeTensor(..., size=(1, 2, 1), dtype=torch.int64), 1, 1, 2), **{}):
expand: attempting to expand a dimension of length 2!

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''