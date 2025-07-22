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
        self.layers = nn.Linear(3, 2)

    def forward(self, x):
        x = self.layers(x)
        x = x.transpose(0, 1)
        x = torch.flatten(x, 1)
        x = x.transpose(0, 1)
        return x




func = Model().to('cuda')



x = torch.randn(3, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)

jit:
Failed running call_module L__self___layers(*(FakeTensor(..., device='cuda:0', size=(3, 2)),), **{}):
a and b must have same reduction dim, but got [3, 2] X [3, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''