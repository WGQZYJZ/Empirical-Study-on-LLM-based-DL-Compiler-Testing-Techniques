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
        self.lin = torch.nn.Linear(3, 8)

    def forward(self, x):
        return torch.tanh(self.lin(x))



func = Model().to('cuda')



x = torch.randn(1, 3, 234, 13)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (702x13 and 3x8)

jit:
Failed running call_module L__self___lin(*(FakeTensor(..., device='cuda:0', size=(1, 3, 234, 13)),), **{}):
a and b must have same reduction dim, but got [702, 13] X [3, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''