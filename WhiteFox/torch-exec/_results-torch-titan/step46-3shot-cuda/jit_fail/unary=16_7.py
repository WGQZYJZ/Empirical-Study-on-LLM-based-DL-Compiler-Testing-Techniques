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
        self.net1 = torch.nn.Linear(3, 32)
        self.net2 = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.net1(x1)
        v2 = self.net2(v1)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (15x5 and 3x32)

jit:
Failed running call_module L__self___net1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 5, 5)),), **{}):
a and b must have same reduction dim, but got [15, 5] X [3, 32].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''