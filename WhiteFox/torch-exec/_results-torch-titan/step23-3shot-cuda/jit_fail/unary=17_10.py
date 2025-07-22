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
        self.pointwise = torch.nn.ConvTranspose2d(3, 1, 1)
        self.linear = torch.nn.Linear(4304, 10)

    def forward(self, x1):
        v1 = self.pointwise(x1)
        v2 = v1.reshape([v1.size()[0], (- 1)])
        v3 = self.linear(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x784 and 4304x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 784)),), **{}):
a and b must have same reduction dim, but got [1, 784] X [4304, 10].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''