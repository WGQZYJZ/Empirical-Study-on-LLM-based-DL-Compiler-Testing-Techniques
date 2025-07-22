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
        self.linear = torch.nn.Linear(60, 80)

    def forward(self, x):
        y = self.linear(x)
        y = (y + x)
        return y



func = Model().to('cuda')



x = torch.randn(20, 100)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x100 and 60x80)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(20, 100)),), **{}):
a and b must have same reduction dim, but got [20, 100] X [60, 80].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''