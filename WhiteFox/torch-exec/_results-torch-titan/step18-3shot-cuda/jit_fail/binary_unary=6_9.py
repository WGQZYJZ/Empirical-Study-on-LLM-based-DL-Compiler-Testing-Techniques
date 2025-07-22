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
        self.linear = torch.nn.Linear(10, 100)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v1 - x2)
        v3 = F.relu(v2)



func = Model().to('cuda')



x1 = torch.randn(10, 100)



x2 = torch.randn(10, 100)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x100 and 10x100)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(10, 100)),), **{}):
a and b must have same reduction dim, but got [10, 100] X [10, 100].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''