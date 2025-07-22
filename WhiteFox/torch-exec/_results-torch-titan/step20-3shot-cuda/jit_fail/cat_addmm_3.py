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
        self.layers = nn.Linear(2, 4)
        self.layers_2 = nn.Linear(4, 4)
        self.layers_3 = nn.Linear(4, 3)

    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x, x), dim=1)
        x = self.layers_2(x)
        x = self.layers_3(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x12 and 4x4)

jit:
Failed running call_module L__self___layers_2(*(FakeTensor(..., device='cuda:0', size=(2, 12)),), **{}):
a and b must have same reduction dim, but got [2, 12] X [4, 4].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''