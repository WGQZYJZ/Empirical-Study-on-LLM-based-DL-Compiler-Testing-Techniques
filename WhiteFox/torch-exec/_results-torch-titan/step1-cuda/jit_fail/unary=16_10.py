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
        self.linear = torch.nn.Linear(3, 9)
        self.linear2 = torch.nn.Linear(8, 9)

    def forward(self, x):
        x = self.linear(x)
        x = self.linear2(torch.relu(x))
        x = torch.relu(x)
        return x



func = Model().to('cuda')



x = torch.randn(1, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x9 and 8x9)

jit:
Failed running call_module L__self___linear2(*(FakeTensor(..., device='cuda:0', size=(1, 9)),), **{}):
a and b must have same reduction dim, but got [1, 9] X [8, 9].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''