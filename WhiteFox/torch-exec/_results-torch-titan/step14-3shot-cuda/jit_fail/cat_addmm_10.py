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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 4)
        self.layers2 = nn.Linear(2, 4)

    def forward(self, x):
        x = self.layers(x)
        out = torch.cat((x, x, x), dim=1)
        out = self.layers2(out)
        out = self.layers(out)
        out = torch.cat((out, out, out), dim=1)
        return out




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x12 and 2x4)

jit:
Failed running call_module L__self___layers2(*(FakeTensor(..., device='cuda:0', size=(2, 12)),), **{}):
a and b must have same reduction dim, but got [2, 12] X [2, 4].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''