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
        self.layers = nn.ModuleList([nn.Linear(2, 4), nn.Linear(2, 4)])

    def forward(self, x):
        for idx in range(2):
            x = self.layers[idx](x)
            x = torch.cat((x, x, x, x), dim=(- 1))
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x16 and 2x4)

jit:
Failed running call_module sub1_1(*(FakeTensor(..., device='cuda:0', size=(2, 16)),), **{}):
a and b must have same reduction dim, but got [2, 16] X [2, 4].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''