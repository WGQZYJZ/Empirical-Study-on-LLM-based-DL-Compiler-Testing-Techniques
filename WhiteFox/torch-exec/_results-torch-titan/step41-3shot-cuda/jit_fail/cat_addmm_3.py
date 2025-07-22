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
        self.layers = nn.Linear(10, 5)

    def forward(self, x):
        input = torch.cat((x, x, x, x, x, x, x, x, x, x), dim=1)
        x = self.layers(input)
        return x




func = Model().to('cuda')



x = torch.randn(2, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x100 and 10x5)

jit:
Failed running call_module L__self___layers(*(FakeTensor(..., device='cuda:0', size=(2, 100)),), **{}):
a and b must have same reduction dim, but got [2, 100] X [10, 5].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''