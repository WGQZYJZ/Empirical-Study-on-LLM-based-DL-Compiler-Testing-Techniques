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
        self.layers = nn.Linear(1, 2)
        pass

    def forward(self, x):
        y = self.layers(x)
        z = (x + 5)
        w = self.layers(y)
        res = (z + w)
        return res




func = Model().to('cuda')



x = torch.randn(2, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x2)

jit:
Failed running call_module L__self___layers(*(FakeTensor(..., device='cuda:0', size=(2, 2)),), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 2].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''