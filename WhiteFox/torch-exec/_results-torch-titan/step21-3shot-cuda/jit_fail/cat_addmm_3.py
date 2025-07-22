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
        self.layers = nn.Linear(2, 2)

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x), dim=(- 1))
        x = x[:, 0, :, :]
        return x




func = Model().to('cuda')



x = torch.randn(4, 2, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x4 and 2x2)

jit:
Failed running call_module L__self___layers(*(FakeTensor(..., device='cuda:0', size=(4, 2, 4)),), **{}):
a and b must have same reduction dim, but got [8, 4] X [2, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''