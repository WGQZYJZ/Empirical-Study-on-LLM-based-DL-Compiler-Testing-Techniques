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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x1, y1):
        x1 = F.max_pool2d(x1, 2, stride=2)
        y1 = F.avg_pool2d(y1, 2, stride=2)
        z0 = torch.cat([x1, y1], 0)
        z1 = self.linear(z0)
        z2 = (z1 * 0.7071067811865476)
        z3 = torch.erf(z2)
        z4 = (z3 + 1)
        z5 = torch.abs(z4)
        return z5



func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)

y1 = 1

test_inputs = [x1, y1]

# JIT_FAIL
'''
direct:
avg_pool2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in function avg_pool2d>(*(1, 2), **{'stride': 2}):
avg_pool2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''