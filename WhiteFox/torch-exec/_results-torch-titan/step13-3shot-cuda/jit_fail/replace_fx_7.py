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
        self.layer1 = torch.nn.Linear(10, 2)

    def forward(self, x1):
        t1 = self.layer1(x1)
        x1 = torch.rand((t1.shape[0], 4), device='cuda')
        x1 = self.layer1(x1)
        return x1




func = Model().to('cuda')



x1 = torch.rand(1, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x4 and 10x2)

jit:
Failed running call_module L__self___layer1(*(FakeTensor(..., device='cuda:0', size=(1, 4)),), **{}):
a and b must have same reduction dim, but got [1, 4] X [10, 2].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''