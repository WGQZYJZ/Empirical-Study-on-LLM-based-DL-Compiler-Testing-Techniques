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
        self.layers = nn.Linear(10, 20)
        self.linear = nn.Linear(10, 20, bias=False)

    def forward(self, x):
        x = self.layers(x)
        x = self.linear(x)
        return x




func = Model().to('cuda')



x = torch.randn(6, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x20 and 10x20)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(6, 20)),), **{}):
a and b must have same reduction dim, but got [6, 20] X [10, 20].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''