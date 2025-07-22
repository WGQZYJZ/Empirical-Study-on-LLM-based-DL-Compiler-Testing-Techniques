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
        self.bias = torch.nn.Parameter(torch.ones(8))
        self.linear = torch.nn.Linear(8, 1)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = (self.bias * const)
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'const' is not defined

jit:
name 'const' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''