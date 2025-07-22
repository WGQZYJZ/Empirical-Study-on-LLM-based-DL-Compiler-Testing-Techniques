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

    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
        self.other_tensor = other_tensor

    def forward(self, x2):
        v2 = self.linear(x2)
        v3 = (v2 + self.other_tensor)
        return v3



other_tensor = 1

func = Model(other_tensor).to('cuda')



x2 = torch.randn(1, 8, 64, 64)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x64 and 8x16)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
a and b must have same reduction dim, but got [512, 64] X [8, 16].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''