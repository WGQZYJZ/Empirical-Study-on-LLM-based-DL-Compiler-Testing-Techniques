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
        self.fc = torch.nn.Linear(3, 4)

    def forward(self, x2):
        v2 = self.fc(x2)
        v4 = torch.tanh(v2)
        return v4



func = Model().to('cuda')



x2 = torch.randn(3, 4)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 3x4)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(3, 4)),), **{}):
a and b must have same reduction dim, but got [3, 4] X [3, 4].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''