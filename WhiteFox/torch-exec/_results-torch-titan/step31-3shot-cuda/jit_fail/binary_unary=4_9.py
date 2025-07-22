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
        self.linear = torch.nn.Linear(535, 379)

    def forward(self, x, weight=None):
        out = (self.linear(x) if (weight is None) else (self.linear(x) + weight))
        return torch.nn.functional.relu(out)



func = Model().to('cuda')



x1 = torch.randn(1, 13, 19)

x = 1

test_inputs = [x1, x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (13x19 and 535x379)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 13, 19)),), **{}):
a and b must have same reduction dim, but got [13, 19] X [535, 379].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''