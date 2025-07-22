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
        self.linear = torch.nn.Linear(4, 4, bias=True)

    def forward(self, x):
        y = self.linear(x)
        y = torch.sigmoid(y)
        y = self.linear(torch.cat([x, y], 1))
        y = torch.sigmoid(y)
        y = self.linear(torch.cat([x, y], 1))
        y = torch.sigmoid(y)
        y = self.linear(torch.cat([x, y], 1))
        return y



func = Model().to('cuda')



features = 4


batch_size = 4


x = torch.randn(batch_size, features)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x8 and 4x4)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(4, 8)),), **{}):
a and b must have same reduction dim, but got [4, 8] X [4, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''