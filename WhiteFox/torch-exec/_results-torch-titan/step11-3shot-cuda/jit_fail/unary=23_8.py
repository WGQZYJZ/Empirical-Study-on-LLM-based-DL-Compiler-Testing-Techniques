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
        super(Model, self).__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 4, (3, 3), (1, 1))
        self.flatten = torch.nn.Flatten()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.flatten(v1)
        v3 = self.linear(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 4, 120, 120)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x59536 and 4x4)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 59536)),), **{}):
a and b must have same reduction dim, but got [1, 59536] X [4, 4].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''