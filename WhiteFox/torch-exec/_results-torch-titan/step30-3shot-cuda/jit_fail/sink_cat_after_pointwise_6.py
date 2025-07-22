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
        super(Model, self).__init__()
        self.linear = linear = nn.Linear(2, 3)
        self.conv = nn.Conv2d(3, 8, 5)

    def forward(self, x):
        out = x.relu()
        out = self.linear(out)
        tmp = out[0]
        out = tmp.clamp(min=0)
        out = self.conv(out)
        out = out.relu()
        out = out[:, (out.shape[1] // 2):]
        out = out.sum(((- 1), (- 2)))
        return out




func = Model().to('cuda')



x = torch.randn(1, 2, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x10 and 2x3)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 2, 10, 10)),), **{}):
a and b must have same reduction dim, but got [20, 10] X [2, 3].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''