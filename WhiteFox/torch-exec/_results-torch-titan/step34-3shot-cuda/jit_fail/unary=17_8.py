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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, (1, 1), stride=(1, 1))
        self.linear = torch.nn.Linear(3, 4)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.linear(v1)
        v3 = self.relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x1 and 3x4)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 3, 1, 1)),), **{}):
a and b must have same reduction dim, but got [3, 1] X [3, 4].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''